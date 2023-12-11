from typing import List, Optional
from datetime import timedelta
from pydantic import EmailStr, AnyHttpUrl, validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "YOUR_SECRET_KEY"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str

# Create an instance of the Settings class
settings = Settings()


