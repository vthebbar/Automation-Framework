import logging

class LogGen:

    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\Logs\\automation.log", force=True,
                            format= '%(asctime)s: %(levelname)s: %(message)s',
                            datefmt= '%d%m%Y %H:%M:%S')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
