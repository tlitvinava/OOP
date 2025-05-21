# presentation/main.py

from application.student_service import StudentService
from domain.dtos import StudentDTO

def main():
    service = StudentService()
    
    while True:
        print("\n--- Меню ---")
        print("1. Добавить студента")
        print("2. Просмотреть студентов")
        print("3. Выход")
        choice = input("Выберите опцию: ").strip()

        if choice == "1":
            name = input("Введите имя студента: ").strip()
            try:
                grade = float(input("Введите оценку студента: ").strip())
            except ValueError:
                print("Неверный формат оценки!")
                continue

            student_dto = StudentDTO(name, grade)
            try:
                quote = service.add_student_with_quote(student_dto)
                print("Студент успешно добавлен!")
                print(f"Мотивационная цитата: \"{quote.content}\" – {quote.author}")
            except Exception as e:
                print("Ошибка при добавлении студента:", e)

        elif choice == "2":
            students = service.get_all_students()
            if not students:
                print("Нет студентов для отображения.")
            for idx, s in enumerate(students, start=1):
                print(f"{idx}. {s['name']}, оценка: {s['grade']}")
                if "quote" in s:
                    quote = s["quote"]
                    print(f"   Цитата: \"{quote['content']}\" - {quote['author']}")
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверная опция!")

if __name__ == "__main__":
    main()
