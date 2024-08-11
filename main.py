from config_loader import ConfigLoader
from image_selector import ImageSelector
from wallpaper_manager import WallpaperManager


def main():
    config_loader = ConfigLoader()
    wallpaper_dir = config_loader.get_wallpaper_dir()

    if not wallpaper_dir:
        print("Diretório do papel de parede não encontrado na configuração.")
        return

    image_selector = ImageSelector(wallpaper_dir)
    selected_image = image_selector.select_random_image()

    if not selected_image:
        print("Nenhuma imagem encontrada.")
        return

    wallpaper_manager = WallpaperManager(selected_image)
    success = wallpaper_manager.apply_wallpaper()

    if success:
        print("Papel de parede trocado com sucesso.")
    else:
        print("Falha ao trocar o papel de parede.")


if __name__ == "__main__":
    main()
