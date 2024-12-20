from builtins import str
import pytest
from httpx import AsyncClient
from app.main import app
from app.models.user_model import User, UserRole
from app.utils.nickname_gen import generate_nickname
from app.utils.security import hash_password
from app.services.jwt_service import decode_token  # Import your FastAPI app
from uuid import uuid4

# Example of a test function using the async_client fixture
@pytest.mark.asyncio
async def test_create_user_access_denied(async_client, user_token, email_service):
    headers = {"Authorization": f"Bearer {user_token}"}
    # Define user data for the test
    user_data = {
        "nickname": generate_nickname(),
        "email": "test@example.com",
        "password": "sS#fdasrongPassword123!",
    }
    # Send a POST request to create a user
    response = await async_client.post("/users/", json=user_data, headers=headers)
    # Asserts
    assert response.status_code == 403

# You can similarly refactor other test functions to use the async_client fixture
@pytest.mark.asyncio
async def test_retrieve_user_access_denied(async_client, verified_user, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = await async_client.get(f"/users/{verified_user.id}", headers=headers)
    assert response.status_code == 403

@pytest.mark.asyncio
async def test_retrieve_user_access_allowed(async_client, admin_user, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.get(f"/users/{admin_user.id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == str(admin_user.id)

@pytest.mark.asyncio
async def test_update_user_email_access_denied(async_client, verified_user, user_token):
    updated_data = {"email": f"updated_{verified_user.id}@example.com"}
    headers = {"Authorization": f"Bearer {user_token}"}
    response = await async_client.put(f"/users/{verified_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 403

@pytest.mark.asyncio
async def test_update_user_email_access_allowed(async_client, admin_user, admin_token):
    updated_data = {"email": f"updated_{admin_user.id}@example.com"}
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.put(f"/users/{admin_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["email"] == updated_data["email"]


@pytest.mark.asyncio
async def test_delete_user(async_client, admin_user, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    delete_response = await async_client.delete(f"/users/{admin_user.id}", headers=headers)
    assert delete_response.status_code == 204
    # Verify the user is deleted
    fetch_response = await async_client.get(f"/users/{admin_user.id}", headers=headers)
    assert fetch_response.status_code == 404

@pytest.mark.asyncio
async def test_create_user_duplicate_email(async_client, verified_user):
    user_data = {
        "email": verified_user.email,
        "password": "AnotherPassword123!",
        "role": UserRole.ADMIN.name
    }
    response = await async_client.post("/register/", json=user_data)
    assert response.status_code == 400
    assert "Email already exists" in response.json().get("detail", "")

@pytest.mark.asyncio
async def test_create_user_invalid_email(async_client):
    user_data = {
        "email": "notanemail",
        "password": "ValidPassword123!",
    }
    response = await async_client.post("/register/", json=user_data)
    assert response.status_code == 422

import pytest
from app.services.jwt_service import decode_token
from urllib.parse import urlencode

@pytest.mark.asyncio
async def test_login_success(async_client, verified_user):
    # Attempt to login with the test user
    form_data = {
        "username": verified_user.email,
        "password": "MySuperPassword$1234"
    }
    response = await async_client.post("/login/", data=urlencode(form_data), headers={"Content-Type": "application/x-www-form-urlencoded"})
    
    # Check for successful login response
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

    # Use the decode_token method from jwt_service to decode the JWT
    decoded_token = decode_token(data["access_token"])
    assert decoded_token is not None, "Failed to decode token"
    assert decoded_token["role"] == "AUTHENTICATED", "The user role should be AUTHENTICATED"

@pytest.mark.asyncio
async def test_login_user_not_found(async_client):
    form_data = {
        "username": "nonexistentuser@here.edu",
        "password": "DoesNotMatter123!"
    }
    response = await async_client.post("/login/", data=urlencode(form_data), headers={"Content-Type": "application/x-www-form-urlencoded"})
    assert response.status_code == 401
    assert "Incorrect email or password." in response.json().get("detail", "")

@pytest.mark.asyncio
async def test_login_incorrect_password(async_client, verified_user):
    form_data = {
        "username": verified_user.email,
        "password": "IncorrectPassword123!"
    }
    response = await async_client.post("/login/", data=urlencode(form_data), headers={"Content-Type": "application/x-www-form-urlencoded"})
    assert response.status_code == 401
    assert "Incorrect email or password." in response.json().get("detail", "")

@pytest.mark.asyncio
async def test_login_unverified_user(async_client, unverified_user):
    form_data = {
        "username": unverified_user.email,
        "password": "MySuperPassword$1234"
    }
    response = await async_client.post("/login/", data=urlencode(form_data), headers={"Content-Type": "application/x-www-form-urlencoded"})
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_login_locked_user(async_client, locked_user):
    form_data = {
        "username": locked_user.email,
        "password": "MySuperPassword$1234"
    }
    response = await async_client.post("/login/", data=urlencode(form_data), headers={"Content-Type": "application/x-www-form-urlencoded"})
    assert response.status_code == 400
    assert "Account locked due to too many failed login attempts." in response.json().get("detail", "")
@pytest.mark.asyncio
async def test_delete_user_does_not_exist(async_client, admin_token):
    non_existent_user_id = "00000000-0000-0000-0000-000000000000"  # Valid UUID format
    headers = {"Authorization": f"Bearer {admin_token}"}
    delete_response = await async_client.delete(f"/users/{non_existent_user_id}", headers=headers)
    assert delete_response.status_code == 404

@pytest.mark.asyncio
async def test_update_user_github(async_client, admin_user, admin_token):
    updated_data = {"github_profile_url": "http://www.github.com/kaw393939"}
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.put(f"/users/{admin_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["github_profile_url"] == updated_data["github_profile_url"]

@pytest.mark.asyncio
async def test_update_user_linkedin(async_client, admin_user, admin_token):
    updated_data = {"linkedin_profile_url": "http://www.linkedin.com/kaw393939"}
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.put(f"/users/{admin_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["linkedin_profile_url"] == updated_data["linkedin_profile_url"]

@pytest.mark.asyncio
async def test_update_user_professional_status(async_client, verified_user, admin_token, email_service):
    """Test updating user's professional status as admin"""
    updated_data = {"is_professional": True}
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.put(f"/users/{verified_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["is_professional"] is True

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

@pytest.mark.asyncio
async def test_regular_user_cannot_update_professional_status(async_client, verified_user, user_token):
    """Test that regular users cannot update professional status"""
    updated_data = {"is_professional": True}
    headers = {"Authorization": f"Bearer {user_token}"}
    response = await async_client.put(f"/users/{verified_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 403

@pytest.mark.asyncio
async def test_update_user_profile_fields(async_client, verified_user, user_token):
    """Test updating multiple profile fields at once"""
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

@pytest.mark.asyncio
async def test_update_user_profile_invalid_urls(async_client, verified_user, user_token):
    """Test validation of profile URLs"""
    profile_data = {
        "linkedin_profile_url": "not-a-url",
        "github_profile_url": "also-not-a-url"
    }
    headers = {"Authorization": f"Bearer {user_token}"}
    response = await async_client.put(f"/users/{verified_user.id}/profile", json=profile_data, headers=headers)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_update_user_profile_unauthorized(async_client, verified_user):
    """Test updating profile without authentication"""
    profile_data = {"first_name": "John"}
    response = await async_client.put(f"/users/{verified_user.id}/profile", json=profile_data)
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_update_other_user_profile_forbidden(async_client, verified_user, user_token):
    """Test user cannot update another user's profile"""
    other_user_id = uuid4()
    profile_data = {"first_name": "John"}
    headers = {"Authorization": f"Bearer {user_token}"}
    response = await async_client.put(f"/users/{other_user_id}/profile", json=profile_data, headers=headers)
    assert response.status_code == 403

@pytest.mark.asyncio
async def test_list_users_as_admin(async_client, admin_token):
    response = await async_client.get(
        "/users/",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 200
    assert 'items' in response.json()

@pytest.mark.asyncio
async def test_list_users_as_manager(async_client, manager_token):
    response = await async_client.get(
        "/users/",
        headers={"Authorization": f"Bearer {manager_token}"}
    )
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_list_users_unauthorized(async_client, user_token):
    response = await async_client.get(
        "/users/",
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 403  # Forbidden, as expected for regular user

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

@pytest.mark.asyncio
async def test_regular_user_cannot_update_role(async_client, verified_user, user_token):
    """Test that regular users cannot update the role field"""
    headers = {"Authorization": f"Bearer {user_token}"}
    updated_data = {"role": UserRole.ADMIN.value}
    response = await async_client.put(
        f"/users/{verified_user.id}",
        json=updated_data,
        headers=headers
    )
    assert response.status_code == 403

@pytest.mark.asyncio
async def test_admin_can_update_role(async_client, verified_user, admin_token):
    """Test that admins can update user roles"""
    headers = {"Authorization": f"Bearer {admin_token}"}
    updated_data = {"role": UserRole.MANAGER.value}
    response = await async_client.put(
        f"/users/{verified_user.id}",
        json=updated_data,
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["role"] == UserRole.MANAGER.value

@pytest.mark.asyncio
async def test_manager_can_update_role(async_client, verified_user, manager_token):
    """Test that managers can update user roles"""
    headers = {"Authorization": f"Bearer {manager_token}"}
    updated_data = {"role": UserRole.MANAGER.value}
    response = await async_client.put(
        f"/users/{verified_user.id}",
        json=updated_data,
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["role"] == UserRole.MANAGER.value
