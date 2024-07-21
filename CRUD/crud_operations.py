class Note:
    def __init__(self, file_name="notes.pkl"):
        """
        The Note class is used to create a note object that can be used to add, read, search, and delete notes. No required file name is needed to create a note object. The default file name is notes.pkl. The file name must end with .pkl. If other extension is provided, the .pkl extension will be added to the file name.
        """

        self.file_name = file_name if file_name.endswith(".pkl") else f"{file_name}.pkl"
        self.title = ""
        self.data = ""

    def __str__(self):
        return f"{self.title}: {self.data}"

    def add_note(self, title: str, note: str):
        pass

    @staticmethod
    def read_all_notes():
        pass

    def search_note_by_title(self, title: str):
        pass

    def delete_note_by_title(self, title: str):
        pass
