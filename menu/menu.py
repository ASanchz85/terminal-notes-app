from time import sleep
from contants import *
from utils.utils import clear_screen


class Terminal_Menu:
    def __init__(self):
        self.menu = [
            "1. Add a new note",
            "2. Display all notes",
            "3. Search for a note by title",
            "4. Search for a note by content",
            "5. Delete a note",
            "Q. Exit",
        ]

    def display_menu(self):
        for option in self.menu:
            print(option)

    def get_user_choice(self):
        choice = input(f"\n{PLUS_SIGN} Enter your choice: ")
        return choice

    @staticmethod
    def title_screen(title_to_show):
        print(
            f"\n{YELLOW}{'_' * 15}{BRIGHT_BLUE} {title_to_show} {YELLOW}{'_' * 15}{RESET}\n"
        )

    @staticmethod
    def keep_using(is_using=True):
        if not is_using:
            clear_screen()
            Terminal_Menu.title_screen("Goodbye")
            sleep(1)
            clear_screen()
            exit()

        answer = input(
            f"\n{GREEN}{PLUS_SIGN}{RESET} Would you like to keep using the program? Press [Y (yes) / N (no)]."
        )
        if answer.lower() == "y":
            clear_screen()
        else:
            Terminal_Menu.keep_using(False)
