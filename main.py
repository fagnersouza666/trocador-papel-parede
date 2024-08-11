from config_loader import ConfigLoader
from image_selector import ImageSelector
from wallpaper_manager import WallpaperManager
from logging_config import LoggerConfig
import platform


def main():
    # Carrega as configurações do arquivo config.ini
    config_loader = ConfigLoader()
    wallpaper_dir = config_loader.get_wallpaper_dir()

    # Cria uma instância do LoggerConfig e configura o logger.
    logger_config = LoggerConfig(
        log_file=f"{wallpaper_dir}wallpaper_changer.log", max_bytes=1048576
    )
    logger = logger_config.get_logger()

    if not wallpaper_dir:
        logger.error("Diretório do papel de parede não encontrado na configuração.")
        return

    # Gerencia o papel de parede atual
    wallpaper_manager = WallpaperManager()
    current_wallpaper = wallpaper_manager.get_current_wallpaper()

    # Seleciona uma imagem aleatória diferente da atual
    image_selector = ImageSelector(wallpaper_dir, current_wallpaper)
    selected_image = image_selector.select_random_image()

    if not selected_image:
        logger.error("Nenhuma imagem encontrada.")
        return

    # Aplica o novo papel de parede
    success = wallpaper_manager.apply_wallpaper(selected_image)

    if success:
        logger.info("Processo concluído com sucesso.")
    else:
        logger.error("Processo concluído com falhas.")


if __name__ == "__main__":
    main()
