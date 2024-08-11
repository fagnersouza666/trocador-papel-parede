import logging
from logging.handlers import RotatingFileHandler


class LoggerConfig:
    def __init__(
        self,
        log_file: str = "wallpaper_changer.log",
        max_bytes: int = 1048576,
        backup_count: int = 3,
    ):
        """
        Inicializa a configuração do logger com rotação de arquivos.

        Args:
            log_file (str): Caminho para o arquivo de log.
            max_bytes (int): Tamanho máximo do arquivo de log em bytes antes de rotacionar. Default é 1MB.
            backup_count (int): Número de arquivos de log de backup a serem mantidos. Default é 3.
        """
        self.log_file = log_file
        self.max_bytes = max_bytes
        self.backup_count = backup_count
        self._setup_logger()

    def _setup_logger(self):
        """
        Configura o logger com o RotatingFileHandler.
        """
        # Cria o manipulador de rotação de arquivo.
        handler = RotatingFileHandler(
            self.log_file, maxBytes=self.max_bytes, backupCount=self.backup_count
        )

        # Configuração básica do logger.
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[handler],
        )

        # Adiciona o manipulador para o console também (opcional).
        console_handler = logging.StreamHandler()
        logging.getLogger().addHandler(console_handler)

    def get_logger(self):
        """
        Retorna o logger configurado.
        """
        return logging.getLogger()
