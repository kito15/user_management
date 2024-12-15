from builtins import ValueError, any, bool, str
from pydantic import BaseModel, EmailStr, Field, HttpUrl, validator, root_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum
import uuid
import re
from app.models.user_model import UserRole
from app.utils.nickname_gen import generate_nickname
from app.utils.sanitizer import sanitize_html

def validate_url(url: Optional[str]) -> Optional[str]:
    if url is None:
        return url
    url_regex = r'^https?:\/\/[^\s/$.?#].[^\s]*$'
    if not re.match(url_regex, url):
        raise ValueError('Invalid URL format')
    return url

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

class UserBase(BaseModel):
    email: EmailStr = Field(..., example="john.doe@example.com")
    nickname: Optional[str] = Field(None, min_length=3, pattern=r'^[\w-]+$', example=generate_nickname())
    first_name: Optional[str] = Field(None, example="John")
    last_name: Optional[str] = Field(None, example="Doe")
    bio: Optional[str] = Field(None, example="Experienced software developer specializing in web applications.")
    profile_picture_url: Optional[str] = Field(None, example="https://example.com/profiles/john.jpg")
    linkedin_profile_url: Optional[str] =Field(None, example="https://linkedin.com/in/johndoe")
    github_profile_url: Optional[str] = Field(None, example="https://github.com/johndoe")
    role: UserRole

    _validate_urls = validator('profile_picture_url', 'linkedin_profile_url', 'github_profile_url', pre=True, allow_reuse=True)(validate_url)
 
    class Config:
        from_attributes = True

class UserCreate(UserBase):
    email: EmailStr = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="Secure*1234")

class UserProfileUpdate(BaseModel):
    first_name: Optional[str] = Field(None, min_length=2, max_length=100)
    last_name: Optional[str] = Field(None, min_length=2, max_length=100)
    bio: Optional[str] = Field(None, max_length=500)
    linkedin_profile_url: Optional[str] = Field(None, 
        example="https://linkedin.com/in/johndoe",
        description="LinkedIn profile URL"
    )
    github_profile_url: Optional[str] = Field(None, 
        example="https://github.com/johndoe",
        description="GitHub profile URL"
    )

    @root_validator(pre=True)
    def check_at_least_one_value(cls, values):
        if not any(values.values()):
            raise ValueError("At least one field must be provided for update")
        return values

    @validator('bio')
    def sanitize_bio(cls, v):
        if v is not None:
            return sanitize_html(v)
        return v

    @validator('linkedin_profile_url')
    def validate_linkedin(cls, v):
        return validate_linkedin_url(v)

    @validator('github_profile_url')
    def validate_github(cls, v):
        return validate_github_url(v)

class UserUpdate(UserBase):
    email: Optional[EmailStr] = Field(None, example="john.doe@example.com")
    nickname: Optional[str] = Field(None, min_length=3, pattern=r'^[\w-]+$', example="john_doe123")
    first_name: Optional[str] = Field(None, example="John")
    last_name: Optional[str] = Field(None, example="Doe")
    bio: Optional[str] = Field(None, example="Experienced software developer specializing in web applications.")
    profile_picture_url: Optional[str] = Field(None, example="https://example.com/profiles/john.jpg")
    linkedin_profile_url: Optional[str] =Field(None, example="https://linkedin.com/in/johndoe")
    github_profile_url: Optional[str] = Field(None, example="https://github.com/johndoe")
    role: Optional[str] = Field(None, example="AUTHENTICATED")
    is_professional: Optional[bool] = Field(None, example=True, description="Professional status of the user")

    @root_validator(pre=True)
    def check_at_least_one_value(cls, values):
        if not any(values.values()):
            raise ValueError("At least one field must be provided for update")
        return values

    @validator('bio')
    def sanitize_bio(cls, v):
        if v is not None:
            return sanitize_html(v)
        return v

    @validator('linkedin_profile_url')
    def validate_linkedin(cls, v):
        return validate_linkedin_url(v)

    @validator('github_profile_url')
    def validate_github(cls, v):
        return validate_github_url(v)

class UserResponse(UserBase):
    id: uuid.UUID = Field(..., example=uuid.uuid4())
    email: EmailStr = Field(..., example="john.doe@example.com")
    nickname: Optional[str] = Field(None, min_length=3, pattern=r'^[\w-]+$', example=generate_nickname())    
    is_professional: Optional[bool] = Field(default=False, example=True)
    role: UserRole

class LoginRequest(BaseModel):
    email: str = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="Secure*1234")

class ErrorResponse(BaseModel):
    error: str = Field(..., example="Not Found")
    details: Optional[str] = Field(None, example="The requested resource was not found.")

class UserListResponse(BaseModel):
    items: List[UserResponse] = Field(..., example=[{
        "id": uuid.uuid4(), "nickname": generate_nickname(), "email": "john.doe@example.com",
        "first_name": "John", "bio": "Experienced developer", "role": "AUTHENTICATED",
        "last_name": "Doe", "bio": "Experienced developer", "role": "AUTHENTICATED",
        "profile_picture_url": "https://example.com/profiles/john.jpg", 
        "linkedin_profile_url": "https://linkedin.com/in/johndoe", 
        "github_profile_url": "https://github.com/johndoe"
    }])
    total: int = Field(..., example=100)
    page: int = Field(..., example=1)
    size: int = Field(..., example=10)
