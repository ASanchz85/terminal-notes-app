import pickle

from CRUD.notes import Note


class Notes_management:
    """
    The Note class is used to create a note object that can be used to add, read, search, and delete notes. No required file name is needed to create a note object. The default file name is notes.pkl. The file name must end with .pkl. If other extension is provided, the .pkl extension will be added to the file name.
    """

    def __init__(self, file_name="notes.pkl"):
        self.file_name = file_name if file_name.endswith(".pkl") else f"{file_name}.pkl"

        try:
            with open(self.file_name, "rb") as file:
                self.data = pickle.load(file)

        except FileNotFoundError:
            self.data = []

    def save_notes(self):
        with open(self.file_name, "wb") as file:
            pickle.dump(self.data, file)

    def add_note(self, title: str, content: str):
        self.data.append(Note(title, content))
        self.save_notes()

    def read_all_notes(self):
        pass

    def search_note_by_title(self, title: str):
        pass

    def delete_note_by_title(self, title: str):
        pass
