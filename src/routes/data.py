from fastapi import APIRouter, UploadFile, Depends, status
from fastapi.responses import JSONResponse
from helpers import get_settings,  Settings
from controllers import DataController, ProjectController
from models import ResponseSignal
import os
import aiofiles

data_router = APIRouter()

@data_router.post('/upload/{projectID}')
async def upload_file(projectID: str, file: UploadFile, 
                settings: Settings = Depends(get_settings)):
    
    data_controller = DataController()
    is_valid, result_signal = data_controller.check_validation_uploadFile(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'signal': result_signal
            }
        )
    project_path = ProjectController().get_project_path(projectID=projectID)
    file_path = data_controller.generate_unique_name(
        orig_file_name=file.filename,
        proj_id=projectID,
        
    )

    async with aiofiles.open(file_path, 'wb') as f:
        while chunk := await file.read(settings.FILE_CHUNK_SIZE):
            await f.write(chunk)
       
        return JSONResponse(
            content={
                'signal': ResponseSignal.FILE_UPLOAD_SUCCESS.value
            }
        )