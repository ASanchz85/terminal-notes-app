from time import sleep

from CRUD.crud_operations import CRUD_management
from menu.menu import Terminal_Menu
from config.constants import *
from utils.utils import *


def check_input_value(input_choice):
    note = CRUD_management()

    if input_choice == "1":
        clear_screen()
        Terminal_Menu.title_screen("Add Note")
        title = input(f"{PLUS_SIGN} Enter title: ")
        content = input(f"{PLUS_SIGN} Enter note: ")

        total_notes = len(note.data)
        note.add_note(title, content)

        if total_notes < len(note.data):
            print(f"\n{GREEN}{PLUS_SIGN}{RESET} Note added successfully.")

    elif input_choice == "2":
        clear_screen()
        Terminal_Menu.title_screen("All Notes")
        all_notes = note.read_all_notes()

        printing_notes(all_notes)

    elif input_choice == "3":
        clear_screen()
        Terminal_Menu.title_screen("Search Note")
        query = input(f"{PLUS_SIGN} Enter the title you are looking for: ")
        searched = note.search_note_by_title(query)

        printing_notes(searched)

    elif input_choice == "4":
        clear_screen()
        Terminal_Menu.title_screen("Search Note")
        query = input(
            f"{PLUS_SIGN} Enter the word of the content you are looking for: "
        )
        searched = note.search_note_by_content(query)

        printing_notes(searched)

    elif input_choice == "5":
        clear_screen()
        Terminal_Menu.title_screen("Delete Note")
        index = input(f"{PLUS_SIGN} Enter the note's index you want to delete: ")

        try:
            index = int(index) - 1
            note.delete_note_by_title(index)
            print(f"\n{GREEN}{PLUS_SIGN}{RESET} Note deleted successfully.")
        except ValueError:
            print(f"\n{RED}{WARNING_SIGN}{RESET} Invalid index")

    elif input_choice == "q" or input_choice == "Q":
        Terminal_Menu.keep_using(False)

    else:
        print(f"\n{RED}{WARNING_SIGN}{RESET} Invalid choice")
        sleep(0.5)
        input(f"\n{RED}{WARNING_SIGN}{RESET} Press any key to try again.")
        clear_screen()
