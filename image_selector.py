import os
import random
from typing import Optional


class ImageSelector:
    def __init__(self, directory: str):
        self.directory = directory

    def _is_valid_image(self, file_name: str) -> bool:
        valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}
        _, ext = os.path.splitext(file_name)
        return ext.lower() in valid_extensions

    def select_random_image(self) -> Optional[str]:
        if not os.path.isdir(self.directory):
            return None

        images = [
            os.path.join(self.directory, f)
            for f in os.listdir(self.directory)
            if os.path.isfile(os.path.join(self.directory, f))
            and self._is_valid_image(f)
        ]

        if not images:
            return None

        return random.choice(images)
