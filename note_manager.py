import json

class NoteManager:
    def __init__(self, file_path='notes.json'):
        self.file_path = file_path
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.file_path, 'r') as file:
                notes_data = json.load(file)
                notes = [Note.from_dict(note) for note in notes_data]
        except FileNotFoundError:
            notes = []
        return notes

    def save_notes(self):
        notes_data = [note.to_dict() for note in self.notes]
        with open(self.file_path, 'w') as file:
            json.dump(notes_data, file, indent=2)
