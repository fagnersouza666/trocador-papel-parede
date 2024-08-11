from config_loader import ConfigLoader
from image_selector import ImageSelector
from wallpaper_manager import WallpaperManager
from logging_config import LoggerConfig
import platform


def main():
    # Cria uma instância do LoggerConfig e configura o logger.
    logger_config = LoggerConfig(
        log_file="wallpaper_changer.log", max_bytes=1048576, backup_count=3
    )
    logger = logger_config.get_logger()

    # Carrega as configurações do arquivo config.ini
    config_loader = ConfigLoader()
    wallpaper_dir = config_loader.get_wallpaper_dir()

    if not wallpaper_dir:
        logger.error("Diretório do papel de parede não encontrado na configuração.")
        return

    # Seleciona uma imagem aleatória do diretório configurado
    image_selector = ImageSelector(wallpaper_dir)
    selected_image = image_selector.select_random_image()

    if not selected_image:
        logger.error("Nenhuma imagem encontrada.")
        return

    # Aplica o papel de parede de acordo com o sistema operacional
    wallpaper_manager = WallpaperManager(selected_image)
    success = wallpaper_manager.apply_wallpaper()

    if success:
        logger.info("Processo concluído com sucesso.")
    else:
        logger.error("Processo concluído com falhas.")


if __name__ == "__main__":
    main()
