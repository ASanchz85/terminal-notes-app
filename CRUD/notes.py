from datetime import date


class Note:
    def __init__(self, title: str, content: str, current_date=date.today()):
        self.note_data = {"date": current_date, "title": title, "content": content}

    def __str__(self):
        return (
            f"\tDate: {self.note_data['date']}\n"
            f"\tTitle: {self.note_data['title']}\n"
            f"\tContent: {self.note_data['content']}\n"
        )
