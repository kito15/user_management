# smtp_client.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.utils.logger import logger

class SMTPClient:
    def __init__(self, server: str, port: int, username: str, password: str):
        self.server = server
        self.port = port
        self.username = username
        self.password = password

    def test_connection(self):
        """Test SMTP connection"""
        try:
            with smtplib.SMTP(self.server, self.port) as server:
                server.starttls()
                server.login(self.username, self.password)
                logger.info("SMTP connection test successful")
        except Exception as e:
            logger.error(f"SMTP connection test failed: {e}")
            raise

    def send_email(self, subject: str, content: str, recipient: str):
        """Send email with error handling and logging"""
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.username
            msg['To'] = recipient
            
            html_part = MIMEText(content, 'html')
            msg.attach(html_part)
            
            with smtplib.SMTP(self.server, self.port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)
                
            logger.info(f"Email sent successfully to {recipient}")
            
        except Exception as e:
            error_msg = f"Failed to send email: {str(e)}"
            logger.error(error_msg)
            raise RuntimeError(error_msg) from e
