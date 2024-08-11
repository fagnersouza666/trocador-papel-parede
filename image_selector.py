import os
import random
from typing import Optional
import logging


class ImageSelector:
    def __init__(self, directory: str, current_image: Optional[str] = None):
        self.directory = directory
        self.current_image = current_image

    def _is_valid_image(self, file_name: str) -> bool:
        valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif"}
        _, ext = os.path.splitext(file_name)
        return ext.lower() in valid_extensions

    def select_random_image(self) -> Optional[str]:
        if not os.path.isdir(self.directory):
            logging.error(f"Diretório não encontrado: {self.directory}")
            return None

        images = [
            os.path.join(self.directory, f)
            for f in os.listdir(self.directory)
            if os.path.isfile(os.path.join(self.directory, f))
            and self._is_valid_image(f)
            and os.path.join(self.directory, f) != self.current_image
        ]

        if not images:
            logging.warning(
                f"Nenhuma imagem válida encontrada no diretório: {self.directory}"
            )
            return None

        selected_image = random.choice(images)
        logging.info(f"Imagem selecionada: {selected_image}")
        return selected_image
