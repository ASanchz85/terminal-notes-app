from datetime import date


class Note:
    def __init__(self, title: str, content: str, current_date=date.today()):
        self.note_data = {"title": title, "content": content, "date": current_date}

    def __str__(self):
        return f"{self.note_data['title']}: {self.note_data['content']} - {self.note_data['current_date']}"
