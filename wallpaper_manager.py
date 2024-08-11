import subprocess
import logging


class WallpaperManager:
    def __init__(self, image_path: str):
        self.image_uri = f"file://{image_path}"

    def _set_wallpaper(self, mode: str = "claro") -> bool:
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
                f"Erro ao tentar trocar o papel de parede para o modo {mode}."
            )
            logging.error(f"Erro: {result.stderr}")
            return False

        logging.info(f"Papel de parede definido para o modo {mode} com sucesso.")
        return True

    def apply_wallpaper(self) -> bool:
        success_light = self._set_wallpaper("claro")
        success_dark = self._set_wallpaper("escuro")
        if success_light and success_dark:
            logging.info("Papel de parede trocado com sucesso para ambos os modos.")
        else:
            logging.error("Falha ao trocar o papel de parede.")
        return success_light and success_dark
