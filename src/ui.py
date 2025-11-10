from typing import Dict, List

def show_menu() -> str:
    print("1. Просмотреть список задач")
    print("2. Добавить задачу")
    print("3. Изменить статус задачи")
    print("4. Редактировать задачу")
    print("5. Удалить задачу")
    print("6. Массовое удаление задач")
    print("7. Выход из приложения")
    print("Выберите опцию\n> ", end='')
    return input()

def get_task_input() -> Dict:
    name = input("Введите название задачи\n> ")
    description = input("Введите описание задачи (опционально)\n> ")
    return {
        'name': name,
        'description': description
    }

def display_tasks(tasks: List[Dict]) -> None:
    if not tasks:
        print("Список задач пуст\n")
        return
    print("-----------Список задач-----------")
    for task in tasks:
        print(f"ID: {task['id']}, Название: {task['name']}, Описание: {task['description']}, Статус: {task['status']}")
    print("----------------------------------\n")


def get_task_ids() -> List[int]:
    return [int(id) for id in input("Введите ID задач через пробел\n> ").split()]

def get_new_status() -> str:
    print("Введите новый статус задачи\n> ", end='')
    return input()