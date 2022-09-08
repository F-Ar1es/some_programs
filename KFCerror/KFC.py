import datetime

class KFCTimeError(Exception):
    def __str__(self):
        error_massge = "\n\033[37;41mGet fxxk of your dxxn IDE.\033[0m"
        state = "\n\033[37;41mToday is KFC Carzy Thursday V me 50 \033[0m"

        return  error_massge + state


def holy(test):
    if type(test) == int and datetime.datetime.today().weekday()+1 == 4:
        raise KFCTimeError()