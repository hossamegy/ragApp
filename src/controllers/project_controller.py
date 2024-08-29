from fastapi import UploadFile
from .base_controller import BaseController
from models import ResponseSignal
import os 

class ProjectController(BaseController):

    def __init__(self):
        super().__init__()

    def get_project_path(self, projectID: str):
        project_path = os.path.join(
            self.file_path,
            projectID
        )

        if not os.path.exists(project_path):
            os.makedirs(project_path)
        
        return project_path