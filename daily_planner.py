n = int(input("Сколько дел у вас запланировано на сегодня? "))
todo = []
for i in range(n):
    task = input(f"Введите дело №{i + 1}: ")
    todo.append(task)

print("\nВаш список дел на сегодня:")
for i, task in enumerate(todo, start=1):
    print(f"{i}. {task}")

todo[0] = input("\nВведите новое описание для первого дела: ")
todo.pop(-1)

print("\nОбновлённый список дел:")
for i, task in enumerate(todo, start=1):
    print(f"{i}. {task}")
