import logging
from logging.handlers import RotatingFileHandler


class LoggerConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LoggerConfig, cls).__new__(cls)
        return cls._instance

    def __init__(
        self,
        log_file: str = "wallpaper_changer.log",
        max_bytes: int = 1048576,
        backup_count: int = 3,
    ):
        if not hasattr(
            self, "initialized"
        ):  # Verifica se já foi inicializado para evitar duplicação
            self.log_file = log_file
            self.max_bytes = max_bytes
            self.backup_count = backup_count
            self._setup_logger()
            self.initialized = True

    def _setup_logger(self):
        handler = RotatingFileHandler(
            self.log_file, maxBytes=self.max_bytes, backupCount=self.backup_count
        )
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[handler],
        )
        console_handler = logging.StreamHandler()
        logging.getLogger().addHandler(console_handler)

    def get_logger(self):
        return logging.getLogger()
