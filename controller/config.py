from ConfigParser import ConfigParser

DEFAULT_CONFIG_FILE_PATH = '../config/config.ini'


class Config:
    config_var = None

    def __init__(self, config_file_path=DEFAULT_CONFIG_FILE_PATH):
        parser = ConfigParser()
        parser.read(config_file_path)

        self.config_var = parser

    def get_corpus_dir(self):
        return self.config_var.get('CORPUS', 'CORPUS_DIR')

    def get_db_name(self):
        return self.config_var.get('DB-MONGO', 'DB_NAME')
