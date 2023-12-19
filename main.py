from note import Note
from note_manager import NoteManager
from datetime import datetime

def display_notes(notes):
    if not notes:
        print("Список заметок пуст.")
        return

    for note in notes:
        print(str(note))

def add_note(note_manager, title, body):
    note_id = len(note_manager.notes) + 1
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_note = Note(note_id, title, body, timestamp)
    note_manager.notes.append(new_note)
    note_manager.save_notes()
    print("Заметка добавлена.")

def edit_note(note_manager, note_id, title, body):
    for note in note_manager.notes:
        if note.note_id == note_id:
            note.title = title
            note.body = body
            note.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            note_manager.save_notes()
            print("Заметка отредактирована.")
            return
    print("Заметка не найдена.")

def delete_note(note_manager, note_id):
    for note in note_manager.notes:
        if note.note_id == note_id:
            note_manager.notes.remove(note)
            note_manager.save_notes()
            print("Заметка удалена.")
            return
    print("Заметка не найдена.")

def main():
    note_manager = NoteManager()

    while True:
        print("\nВыберите действие:")
        print("1. Вывести список заметок")
        print("2. Просмотреть заметку по ID")
        print("3. Добавить заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("0. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            display_notes(note_manager.notes)
        elif choice == '2':
            note_id = int(input("Введите ID заметки для просмотра: "))
            for note in note_manager.notes:
                if note.note_id == note_id:
                    print(str(note))
                    break
            else:
                print("Заметка не найдена.")
        elif choice == '3':
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            add_note(note_manager, title, body)
        elif choice == '4':
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            edit_note(note_manager, note_id, title, body)
        elif choice == '5':
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_manager, note_id)
        elif choice == '0':
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите число от 0 до 5.")

if __name__ == "__main__":
    main()
