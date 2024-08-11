import subprocess


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
            print(f"Erro ao tentar trocar o papel de parede para o modo {mode}.")
            print("Erro:", result.stderr)

        return result.returncode == 0

    def apply_wallpaper(self) -> bool:
        success_light = self._set_wallpaper("claro")
        success_dark = self._set_wallpaper("escuro")
        return success_light and success_dark
