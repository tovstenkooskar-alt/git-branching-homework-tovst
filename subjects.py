# subjects.py
SUBJECTS = [
    "конфигурирование windows 10",
    "ОИТ",
    "Python",
]

def print_subjects():
    print("\nДисциплины:")
    for number, subject in enumerate(SUBJECTS, start=1):
        print(f"{number}. {subject}")