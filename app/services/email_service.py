# email_service.py
from builtins import ValueError, dict, str
from settings.config import settings
from app.utils.smtp_connection import SMTPClient
from app.utils.template_manager import TemplateManager
from app.models.user_model import User
from app.utils.logger import logger
import os

class EmailService:
    def __init__(self, template_manager: TemplateManager):
        self.smtp_client = SMTPClient(
            server=settings.smtp_server,
            port=settings.smtp_port,
            username=settings.smtp_username,
            password=settings.smtp_password
        )
        self.template_manager = template_manager
        self._test_smtp_connection()
        
    def _test_smtp_connection(self):
        """Test SMTP connection during initialization"""
        try:
            self.smtp_client.test_connection()
            logger.info("SMTP connection test successful")
        except Exception as e:
            logger.error(f"SMTP connection test failed: {e}")
            raise

    def _validate_template(self, template_name: str) -> bool:
        """Validate that a specific template exists"""
        template_path = os.path.join("email_templates", f"{template_name}.md")
        exists = os.path.exists(template_path)
        if not exists:
            logger.error(f"Missing email template: {template_path}")
        else:
            logger.info(f"Found template: {template_name}")
        return exists

    async def send_user_email(self, user_data: dict, email_type: str):
        logger.info(f"Sending {email_type} email to {user_data.get('email')}")
        try:
            template_path = os.path.join("email_templates", f"{email_type}.md")
            logger.info(f"Using template: {template_path}")
            
            if not os.path.exists(template_path):
                logger.error(f"Template not found: {template_path}")
                raise ValueError(f"Email template not found: {email_type}")

            with open(template_path, 'r') as file:
                template_content = file.read()

            # Simple template variable replacement
            content = template_content
            for key, value in user_data.items():
                content = content.replace(f"{{{key}}}", str(value))

            logger.info(f"Rendered email content: {content[:100]}...")  # Log first 100 chars

            self.smtp_client.send_email(
                subject=f"User Management System - {email_type.replace('_', ' ').title()}",
                content=content,
                recipient=user_data['email']
            )
            logger.info(f"Email sent successfully to {user_data['email']}")

        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")
            logger.error(f"User data: {user_data}")
            raise

    async def send_verification_email(self, user: User):
        verification_url = f"{settings.server_base_url}verify-email/{user.id}/{user.verification_token}"
        await self.send_user_email({
            "name": user.first_name or user.nickname,
            "verification_url": verification_url,
            "email": user.email
        }, 'email_verification')

    async def send_professional_status_email(self, user: User, is_professional: bool):
        """Send professional status update email"""
        try:
            logger.info(f"Starting professional status email send for {user.email}")
            logger.info(f"Professional status value: {is_professional}")
            
            template_path = os.path.join("email_templates", "professional_status_updated.md")
            
            if not os.path.exists(template_path):
                logger.error(f"Template not found at path: {template_path}")
                raise ValueError("Professional status email template not found")
            
            logger.info("Found template file, reading content")
            with open(template_path, 'r') as file:
                template_content = file.read()
                
            # Prepare email data
            email_data = {
                "name": user.first_name or user.nickname or "User",
                "professional_status": "professional" if is_professional else "non-professional",
                "email": user.email
            }
            logger.info(f"Prepared email data: {email_data}")

            # Replace template variables
            for key, value in email_data.items():
                template_content = template_content.replace(f"{{{key}}}", str(value))
            
            logger.info("Template variables replaced, sending email")
            self.smtp_client.send_email(
                subject="Professional Status Update",
                content=template_content,
                recipient=user.email
            )
            logger.info(f"Professional status email sent successfully to {user.email}")
            
        except Exception as e:
            logger.error(f"Error in send_professional_status_email: {str(e)}")
            logger.error(f"User data: {user.__dict__}")
            raise