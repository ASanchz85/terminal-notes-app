import os

from config.constants import *


def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")


def printing_notes(notes):
    if not notes:
        print(f"\n{RED}{WARNING_SIGN}{RESET} No notes found.")
    else:
        for index, note in enumerate(notes, 1):
            print(f"{index}. {note}")
