class KFCTimeError(Exception):
    def __str__(self):
        error_massge = "\033[37;41m KFC Carzy Thursday V me 50￥ \033[0m"
        
        return error_massge


def print(string):
    if string:
        raise KFCTimeError()