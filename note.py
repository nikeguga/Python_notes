from datetime import datetime

class Note:
    def __init__(self, note_id, title, body, timestamp):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp

    def __str__(self):
        return f"ID: {self.note_id} | Заголовок: {self.title} | Тело: {self.body} | Дата/время: {self.timestamp}"

    def to_dict(self):
        return {
            'note_id': self.note_id,
            'title': self.title,
            'body': self.body,
            'timestamp': self.timestamp
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
