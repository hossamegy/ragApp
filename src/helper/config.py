from pydantic_settings import BaseSettings

##############################################################################
# Configuration settings for the application are managed using Pydantic.
# The Settings class reads configuration values from environment variables, 
# typically loaded from a .env file.
#############################################################################

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    GOOGLE_API_KEY: str

    class Config:
        env_file = '.env'

def get_settings():
    return Settings()