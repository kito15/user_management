import pytest
from app.schemas.user_schemas import UserProfileUpdate, UserUpdate
from pydantic import ValidationError

def test_user_profile_update_sanitizes_bio():
    profile = UserProfileUpdate(
        bio='<script>alert("XSS")</script><p>Test</p>'
    )
    assert profile.bio == '<p>Test</p>'

def test_user_update_sanitizes_bio():
    update = UserUpdate(
        email="test@example.com",
        role="AUTHENTICATED",
        bio='<script>alert("XSS")</script><p>Test</p>'
    )
    assert update.bio == '<p>Test</p>'

def test_user_profile_update_allows_safe_html():
    profile = UserProfileUpdate(
        bio='<p>Test</p><b>Bold</b><i>Italic</i>'
    )
    assert profile.bio == '<p>Test</p><b>Bold</b><i>Italic</i>'

def test_user_profile_update_without_bio():
    profile = UserProfileUpdate(
        first_name="John",
        last_name="Doe"
    )
    assert profile.bio is None
