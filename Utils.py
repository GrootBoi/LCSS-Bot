from typing import Union

class Utils:
    @staticmethod
    def log_info(message: Union[str, int, Exception]) -> None:
        FGBlue = '\x1b[34m'
        reset = '\x1b[0m'
        print(f'{FGBlue}ℹ️[ INFO ]: {reset}{message}')

    @staticmethod
    def log_warning(message: Union[str, int, Exception]) -> None:
        FGYellow = '\x1b[33m'
        reset = '\x1b[0m'
        print(f'{FGYellow}⚠️[ WARNING ]: {reset}{message}')

    @staticmethod
    def log_error(message: Union[str, int, Exception]) -> None:
        FGRed = '\x1b[31m'
        reset = '\x1b[0m'
        print(f'{FGRed}⛔[ ERROR ]: {reset}{message}')

