import pickle

from CRUD.notes import Note


class CRUD_management:
    """
    The CRUD_management class is used to create a note object that can be used to add, read, search, and delete notes. No required file name is needed to create a note object. The default file name is notes.pkl. The file name must end with .pkl. If other extension is provided, the .pkl extension will be added to the file name.
    """

    def __init__(self, file_name="notes.pkl"):
        self.file_name = file_name if file_name.endswith(".pkl") else f"{file_name}.pkl"

        try:
            with open(self.file_name, "rb") as file:
                self.data = pickle.load(file)

        except FileNotFoundError:
            self.data = []

    def _save_notes(self):
        with open(self.file_name, "wb") as file:
            pickle.dump(self.data, file)

    def add_note(self, title: str, content: str):
        self.data.append(Note(title, content))
        self._save_notes()

    def read_all_notes(self):
        return self.data

    def search_note_by_title(self, query: str):
        return [item for item in self.data if query in item.note_data["title"]]

    def search_note_by_content(self, query: str):
        return [item for item in self.data if query in item.note_data["content"]]

    def delete_note_by_title(self, query: str):
        pass
