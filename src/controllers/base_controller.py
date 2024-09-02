from helpers import get_settings, Settings
import os
import random
import string

class BaseController:
    
    def __init__(self):
        self.settings = get_settings()
        self.base_path = os.path.dirname(os.path.dirname(__file__))
        self.file_path = os.path.join(
            self.base_path,
            "asset/files"
        )

    def generate_random_string(self, length: int = 12):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    
    