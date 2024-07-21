from contants import PLUS_SIGN
from utils.check_input_value import *


def main():
    clear_screen()

    while True:
        title_screen("Menu")
        main_menu_options()

        choice = input(f"\n{PLUS_SIGN} Enter your choice: ")

        check_input_value(choice)


if __name__ == "__main__":
    main()
