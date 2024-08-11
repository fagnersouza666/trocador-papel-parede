import subprocess
import logging
import platform
import ctypes
import os


class WallpaperManager:
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image_uri = f"file://{image_path}"

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

    def apply_wallpaper(self) -> bool:
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
