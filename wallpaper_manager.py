import subprocess
import logging
import platform
import ctypes
import os
from typing import Optional


class WallpaperManager:
    def __init__(self):
        pass

    def _get_current_wallpaper_linux(self) -> Optional[str]:
        command = ["gsettings", "get", "org.gnome.desktop.background", "picture-uri"]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            wallpaper_uri = result.stdout.strip().strip("'")
            return wallpaper_uri.replace("file://", "")
        else:
            logging.error("Erro ao obter o papel de parede atual no Linux.")
            return None

    def _get_current_wallpaper_windows(self) -> Optional[str]:
        try:
            return ctypes.windll.user32.SystemParametersInfoW(0x0073, 0, None, 0)
        except Exception as e:
            logging.error(f"Erro ao obter o papel de parede atual no Windows: {str(e)}")
            return None

    def get_current_wallpaper(self) -> Optional[str]:
        system_name = platform.system().lower()
        if system_name == "linux":
            return self._get_current_wallpaper_linux()
        elif system_name == "windows":
            return self._get_current_wallpaper_windows()
        else:
            logging.error(f"Sistema operacional {system_name} não suportado.")
            return None

    def _set_wallpaper_linux(self, mode: str = "claro") -> bool:
        key = "picture-uri" if mode == "claro" else "picture-uri-dark"
        command = [
            "gsettings",
            "set",
            "org.gnome.desktop.background",
            key,
            self.image_uri,
        ]
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            logging.error(
                f"Erro ao tentar trocar o papel de parede para o modo {mode} no Linux."
            )
            logging.error(f"Erro: {result.stderr}")
            return False

        logging.info(
            f"Papel de parede definido para o modo {mode} no Linux com sucesso."
        )
        return True

    def _set_wallpaper_windows(self) -> bool:
        SPI_SETDESKWALLPAPER = 20
        try:
            result = ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER, 0, self.image_path, 3
            )
            if not result:
                logging.error("Erro ao tentar trocar o papel de parede no Windows.")
                return False
            logging.info("Papel de parede definido com sucesso no Windows.")
            return True
        except Exception as e:
            logging.error(
                f"Erro ao tentar trocar o papel de parede no Windows: {str(e)}"
            )
            return False

    def apply_wallpaper(self, image_path: str) -> bool:
        self.image_path = image_path
        self.image_uri = f"file://{image_path}"

        system_name = platform.system().lower()
        if system_name == "linux":
            success_light = self._set_wallpaper_linux("claro")
            success_dark = self._set_wallpaper_linux("escuro")
            return success_light and success_dark
        elif system_name == "windows":
            return self._set_wallpaper_windows()
        else:
            logging.error(f"Sistema operacional {system_name} não suportado.")
            return False
