from fastapi import FastAPI, APIRouter
from os import getenv

base_router = APIRouter()

@base_router.get('/')
async def app_info() -> dict:
    return {
        'app_name': getenv('APP_NAME'),
        'app_version': getenv('APP_VERSION')
    }