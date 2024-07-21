import os
from time import sleep

from CRUD.crud_operations import Notes
from contants import *


def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")


def title_screen(title_to_show):
    print(
        f"\n{YELLOW}{'_' * 15}{BRIGHT_BLUE} {title_to_show} {YELLOW}{'_' * 15}{RESET}\n"
    )


def main_menu_options():
    print("1. Add note")
    print("2. Read all notes")
    print("3. Search for a note by title")
    print("4. Delete a note by title")
    print("5. Exit")


def check_input_value(input_choice):
    note = Notes()

    if input_choice == "1":
        clear_screen()
        title_screen("Add Note")
        title = input(f"{PLUS_SIGN} Enter title: ")
        data = input(f"{PLUS_SIGN} Enter note: ")

        note.add_note(title, data)

    elif input_choice == "2":
        clear_screen()
        title_screen("All Notes")
        note.read_all_notes()

    elif input_choice == "3":
        clear_screen()
        title_screen("Search Note")
        title = input(f"{PLUS_SIGN} Enter title: ")
        note.search_note_by_title(title)

    elif input_choice == "4":
        clear_screen()
        title_screen("Delete Note")
        title = input(f"{PLUS_SIGN} Enter title: ")
        note.delete_note_by_title(title)

    elif input_choice == "5":
        clear_screen()
        title_screen("Goodbye")
        sleep(1)
        clear_screen()
        exit()

    else:
        input(
            f"\n{RED}{WARNING_SIGN}{RESET} Invalid choice. Press any key to try again."
        )
        clear_screen()
