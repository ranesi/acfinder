import db, sys, ui


def main() -> None:
    """
        Main loop of program. Terminates until either:
        1) 'q' input entered by user, or
        2) keyboard interrupt
    """
    while True:
        ui.mainloop()
        c = input()
        if valid_int(c):
            loc = db.get_location(c)
            if loc is not None:
                ui.print_location(loc)
            else:
                ui.error()
        else:
            if c.lower() == 'q':
                break
            else:
                continue


def valid_int(x) -> bool:
    """
        Returns true if passed value is a valid integer
    """
    i = 0
    try:
        i = int(x)
        return True
    except:
        return False


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
