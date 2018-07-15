import api, datetime, os


def mainloop() -> None:

    cls()
    print('Enter area code and press enter. \'Q\' to quit.\n')


def line() -> str:

    ret = '=' * 60
    return ret


def print_location(loc: dict) -> None:

    cls()
    s = "{}\nAreacode {}\n{}\nLOCATION\t\t{}, {}\nCOORDINATES\t\t{}, {}\n{}".format(
        line(), loc['areacode'], line(), loc['city'], loc['state'], loc['lat'],
        loc['lon'], line())
    print(s)
    # Google Time Zone API call
    api.get_tz(loc['lat'], loc['lon'])
    print('\nPress ENTER to continue ...')
    input()


def print_tz(id: str, name: str, ltime: datetime) -> None:

    # Formatting for strftime function (hours, minutes, seconds)
    format = '%H:%M:%S'

    s = 'TIMEZONE ID\t\t{}\nTIMEZONE NAME\t\t{}\n{}\nLocal time is {}'.format(
        id, name, line(), ltime.strftime(format))

    print(s)


def error() -> None:

    cls()
    print('Error! Areacode not found!\n')
    print('\nPress ENTER to continue...')
    input()


def cls() -> None:

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
