from helpers.check_input_value import check_input_value
from menu.menu import Terminal_Menu
from utils.utils import clear_screen


def main():
    clear_screen()
    menu = Terminal_Menu()

    while True:
        menu.title_screen("Menu")
        menu.display_menu()

        choice = menu.get_user_choice()

        check_input_value(choice)


if __name__ == "__main__":
    main()
