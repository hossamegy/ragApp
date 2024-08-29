from .base_controller import BaseController
from .project_controller import ProjectController
from models import ResponseSignal
from fastapi import UploadFile
import re
import os

class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.scale =1048576

    def check_validation_uploadFile(self, file: UploadFile):
        if file.content_type not in self.settings.FILE_ALLOWED_TYPES:
            print("text: ", file.content_type )
            print("2 pdf: ", self.settings.FILE_ALLOWED_TYPES )

            return ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        
        if file.size > self.settings.FILE_MAX_SIZE * self.scale:
            print("text: ", file.content_type )
            print("text: ", self.settings.FILE_MAX_SIZE * self.scale )
            return ResponseSignal.FILE_SIZE_EXCEEDED.value
        
        return True, ResponseSignal.FILE_VALIDATED_SUCCESS.value
    
    def generate_unique_name(self, orig_file_name: str, proj_id: str):
        def generate_new_path():
            random_key = self.generate_random_string(11)
            project_path = ProjectController().get_project_path(projectID=proj_id)

            cleaned_file_name = self.get_clean_file_name(
                orig_file_name=orig_file_name
            )

            return os.path.join(
                project_path,
                random_key + '_' + cleaned_file_name
            )
        
        final_new_path = generate_new_path()

        while os.path.exists(final_new_path):
              generate_new_path()

        return final_new_path
    
    def get_clean_file_name(self, orig_file_name: str):
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_file_name.strip())
        return cleaned_file_name.replace(' ', '_')