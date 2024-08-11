import configparser
from typing import Dict


class ConfigLoader:
    def __init__(self, config_file: str = "config.ini"):
        self.config_file = config_file
        self.config = (
            self._load_config()
        )  # Carrega as configurações do arquivo assim que a instância é criada.

    def _load_config(self) -> Dict[str, str]:
        """
        Carrega o arquivo de configuração `config.ini` e retorna um dicionário
        com as configurações da seção 'Config'.
        """
        config = configparser.ConfigParser()
        config.read(self.config_file)
        return config["Config"]

    def get_wallpaper_dir(self) -> str:
        """
        Retorna o diretório configurado para papéis de parede.
        Se a chave 'wallpaper_dir' não existir, retorna None.
        """
        return self.config.get("wallpaper_dir", None)
