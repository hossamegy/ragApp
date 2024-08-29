from fastapi import FastAPI, APIRouter, Depends
from helpers import get_settings, Settings

base_router = APIRouter()

@base_router.get('/')
async def app_info(SETTINGS: Settings = Depends(get_settings)) -> dict:
    SETTINGS = get_settings()
    
    return {
        'app_name': SETTINGS.APP_NAME,
        'app_version': SETTINGS.APP_VERSION
    }