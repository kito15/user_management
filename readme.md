# User Management System

This project is a user management system built using FastAPI, a modern Python web framework. It provides essential features for user registration, authentication, role-based access control, and profile management. This README provides details about the features implemented for this project, with links to issues and tests.

## Implemented Feature: Enhanced User Profile Management

The main focus of this contribution was to implement and enhance the user profile management feature. This feature includes:

*   **Profile Update API:** An endpoint (`/users/{user_id}`) that allows authenticated users to update their own profile information and for admins/managers to update any user's information.
*   **Professional Status Updates:** Admins and managers can now upgrade and downgrade users to professional status.
*   **Email Notifications:** Users receive email notifications upon profile updates and when their professional status is changed.
*   **Input Validation:** Strict URL validation for LinkedIn and GitHub profiles is implemented using regular expressions. The bio field is sanitized to prevent XSS attacks using html stripping.
*  **Audit Trail**: Every profile change is tracked using a database table.

## Resolved Issues

The following issues were identified and resolved during the project:

1.  **Admin Role Loss:** [https://github.com/kito15/user_management/issues/1](https://github.com/kito15/user_management/issues/1) - Admin users were incorrectly downgraded to "authenticated" upon email verification.
2.  **Missing Email Template Error Handling**: [https://github.com/kito15/user_management/issues/2](https://github.com/kito15/user_management/issues/2) - Profile update email template failures are not handled gracefully
3.  **XSS Vulnerability:** [https://github.com/kito15/user_management/issues/3](https://github.com/kito15/user_management/issues/3) - The bio field was vulnerable to Cross-Site Scripting (XSS) attacks
4.  **URL Validation:** [https://github.com/kito15/user_management/issues/4](https://github.com/kito15/user_management/issues/4) - The LinkedIn and GitHub profile URLs accepted invalid formats
5. **Missing Profile History** [https://github.com/kito15/user_management/issues/5](https://github.com/kito15/user_management/issues/5) - A lack of audit history made it impossible to track profile changes.

## New Tests Implemented

Ten new unit tests were implemented using Pytest to ensure the new functionality works as expected.

1.  **Update LinkedIn URL:** [tests/test_api/test_users_api.py#L163](tests/test_api/test_users_api.py#L163)
    ```python
    @pytest.mark.asyncio
    async def test_update_user_linkedin(async_client, admin_user, admin_token):
        updated_data = {"linkedin_profile_url": "http://www.linkedin.com/kaw393939"}
        headers = {"Authorization": f"Bearer {admin_token}"}
        response = await async_client.put(f"/users/{admin_user.id}", json=updated_data, headers=headers)
        assert response.status_code == 200
        assert response.json()["linkedin_profile_url"] == updated_data["linkedin_profile_url"]
    ```

2.  **Update Multiple Profile Fields:** [tests/test_api/test_users_api.py#L215](tests/test_api/test_users_api.py#L215)
    ```python
    @pytest.mark.asyncio
    async def test_update_user_profile_fields(async_client, verified_user, user_token):
        profile_data = {
            "first_name": "John",
            "last_name": "Smith",
            "bio": "Software Developer with 5 years experience",
            "linkedin_profile_url": "https://linkedin.com/in/johnsmith",
            "github_profile_url": "https://github.com/johnsmith"
        }
        headers = {"Authorization": f"Bearer {user_token}"}
        response = await async_client.put(f"/users/{verified_user.id}/profile", json=profile_data, headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data["first_name"] == profile_data["first_name"]
        assert data["last_name"] == profile_data["last_name"]
        assert data["bio"] == profile_data["bio"]
        assert data["linkedin_profile_url"] == profile_data["linkedin_profile_url"]
        assert data["github_profile_url"] == profile_data["github_profile_url"]
    ```

3.  **Invalid Profile URLs:** [tests/test_api/test_users_api.py#L235](tests/test_api/test_users_api.py#L235)
    ```python
    @pytest.mark.asyncio
    async def test_update_user_profile_invalid_urls(async_client, verified_user, user_token):
        profile_data = {
            "linkedin_profile_url": "not-a-url",
            "github_profile_url": "also-not-a-url"
        }
        headers = {"Authorization": f"Bearer {user_token}"}
        response = await async_client.put(f"/users/{verified_user.id}/profile", json=profile_data, headers=headers)
        assert response.status_code == 422
    ```
4.  **Unauthorized Profile Update:** [tests/test_api/test_users_api.py#L246](tests/test_api/test_users_api.py#L246)
    ```python
    @pytest.mark.asyncio
    async def test_update_user_profile_unauthorized(async_client, verified_user):
        profile_data = {"first_name": "John"}
        response = await async_client.put(f"/users/{verified_user.id}/profile", json=profile_data)
        assert response.status_code == 401
    ```

5.  **Forbidden Profile Update:** [tests/test_api/test_users_api.py#L253](tests/test_api/test_users_api.py#L253)
    ```python
    @pytest.mark.asyncio
    async def test_update_other_user_profile_forbidden(async_client, verified_user, user_token):
        other_user_id = uuid4()
        profile_data = {"first_name": "John"}
        headers = {"Authorization": f"Bearer {user_token}"}
        response = await async_client.put(f"/users/{other_user_id}/profile", json=profile_data, headers=headers)
        assert response.status_code == 403
    ```
6.  **Admin Upgrades User to Pro Status** [tests/test_api/test_users_api.py#L171](tests/test_api/test_users_api.py#L171)
    ```python
    @pytest.mark.asyncio
    async def test_update_user_professional_status(async_client, verified_user, admin_token, email_service):
        updated_data = {"is_professional": True}
        headers = {"Authorization": f"Bearer {admin_token}"}
        response = await async_client.put(f"/users/{verified_user.id}", json=updated_data, headers=headers)
        assert response.status_code == 200
        assert response.json()["is_professional"] is True
    ```
7.  **Regular User Fails to Update Pro Status** [tests/test_api/test_users_api.py#L217](tests/test_api/test_users_api.py#L217)
     ```python
    @pytest.mark.asyncio
    async def test_regular_user_cannot_update_professional_status(async_client, verified_user, user_token):
        """Test that regular users cannot update professional status"""
        updated_data = {"is_professional": True}
        headers = {"Authorization": f"Bearer {user_token}"}
        response = await async_client.put(f"/users/{verified_user.id}", json=updated_data, headers=headers)
        assert response.status_code == 403
     ```
8.  **Downgrade Pro Status** [tests/test_api/test_users_api.py#L180](tests/test_api/test_users_api.py#L180)
    ```python
     @pytest.mark.asyncio
    async def test_update_user_professional_status_downgrade(async_client, verified_user, admin_token, email_service, db_session):
        """Test downgrading user's professional status as admin"""
        # First set the user as professional
        verified_user.is_professional = True
        await db_session.commit()
        await db_session.refresh(verified_user)
        assert verified_user.is_professional is True

        # Now downgrade the status
        updated_data = {"is_professional": False}
        headers = {"Authorization": f"Bearer {admin_token}"}
        response = await async_client.put(
            f"/users/{verified_user.id}", 
            json=updated_data, 
            headers=headers
        )
        
        # Verify API response
        assert response.status_code == 200
        assert response.json()["is_professional"] is False

        # Verify database state
        await db_session.refresh(verified_user)
        assert verified_user.is_professional is False
        assert verified_user.professional_status_updated_at is not None
    ```

9.  **Empty Payload Test** [tests/test_api/test_users_api.py#L287](tests/test_api/test_users_api.py#L287)
    ```python
    @pytest.mark.asyncio
    async def test_update_user_empty_payload(async_client, verified_user, admin_token):
        """Test that sending an empty update payload returns the original user data"""
        headers = {"Authorization": f"Bearer {admin_token}"}
        response = await async_client.put(
            f"/users/{verified_user.id}",
            json={},
            headers=headers
        )
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == str(verified_user.id)
        assert data["email"] == verified_user.email
        assert data["nickname"] == verified_user.nickname
    ```

10. **Invalid UUID Test** [tests/test_api/test_users_api.py#L302](tests/test_api/test_users_api.py#L302)
    ```python
     @pytest.mark.asyncio
    async def test_update_user_invalid_uuid(async_client, admin_token):
        """Test that attempting to update a user with invalid UUID returns 404"""
        invalid_uuid = "invalid-uuid"
        headers = {"Authorization": f"Bearer {admin_token}"}
        response = await async_client.put(
            f"/users/{invalid_uuid}",
            json={"email": "test@example.com"},
            headers=headers
        )
        assert response.status_code == 422  # Invalid UUID format
    ```

## Code Snippets

Here are some of the key code snippets:

### Sanitization Utility ([app/utils/sanitizer.py](app/utils/sanitizer.py))

```python
    import re
    from typing import Optional

    def sanitize_html(text: Optional[str]) -> Optional[str]:
        """
        Sanitize HTML content by removing script tags and other potentially harmful elements
        """
        if not text:
            return text

        # Remove script tags and their contents
        text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL)
        
        # Remove onclick and other event handlers
        text = re.sub(r' on\w+="[^"]*"', '', text)
        
        # Remove javascript: URLs
        text = re.sub(r'javascript:[^"\']*', '', text)
        
        # Only allow specific safe tags
        allowed_tags = ['p', 'br', 'b', 'i', 'u', 'em', 'strong']
        pattern = r'<[/]?([^> ]+)[^>]*>'
        
        def tag_filter(match):
            tag = match.group(1).lower()
            if tag in allowed_tags:
                return f'<{tag}>'  # Return basic tag without attributes
            return ''  # Remove non-allowed tags
        
        text = re.sub(pattern, tag_filter, text)
        
        return text
```

### User Schema with Sanitization ([app/schemas/user_schemas.py](app/schemas/user_schemas.py))

```python
   from app.utils.sanitizer import sanitize_html
    
    # ...existing imports...

    class UserProfileUpdate(BaseModel):
        # ...existing fields...
        bio: Optional[str] = Field(None, max_length=500)
        
        @validator('bio')
        def sanitize_bio(cls, v):
            if v is not None:
                return sanitize_html(v)
            return v

    class UserUpdate(UserBase):
        # ...existing fields...
        bio: Optional[str] = Field(None, example="Experienced software developer specializing in web applications.")
        
        @validator('bio')
        def sanitize_bio(cls, v):
            if v is not None:
                return sanitize_html(v)
            return v
```

### URL Validation in Schemas ([app/schemas/user_schemas.py](app/schemas/user_schemas.py))

```python
    import re

    def validate_linkedin_url(url: Optional[str]) -> Optional[str]:
        """Validate LinkedIn profile URL format"""
        if url is None:
            return url
        pattern = r'^https://(www\.)?linkedin\.com/in/[a-zA-Z0-9_-]+/?$'
        if not re.match(pattern, url):
            raise ValueError('URL is not a valid LinkedIn profile URL')
        return url

    def validate_github_url(url: Optional[str]) -> Optional[str]:
        """Validate GitHub profile URL format"""
        if url is None:
            return url
        pattern = r'^https://(www\.)?github\.com/[a-zA-Z0-9_-]+/?$'
        if not re.match(pattern, url):
            raise ValueError('URL is not a valid GitHub profile URL')
        return url
```
