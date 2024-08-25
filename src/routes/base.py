from fastapi import FastAPI, APIRouter
from helper.config import get_settings

base_router = APIRouter()

@base_router.get('/')
async def app_info() -> dict:
    SETTINGS = get_settings()
    
    return {
        'app_name': SETTINGS.APP_NAME,
        'app_version': SETTINGS.APP_VERSION
    }