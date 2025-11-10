from ui import show_menu, get_task_input, display_tasks, get_task_id, get_task_ids, get_new_status
from logic import add_task, change_status, edit_task, delete_task, bulk_delete_tasks
from data import load_tasks, save_tasks

def main():
    tasks = load_tasks()
    while True:
        choice = show_menu()
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            task_data = get_task_input()
            add_task(tasks, task_data)
            save_tasks(tasks)
        elif choice == '3':
            task_id = get_task_id()
            new_status = get_new_status()
            change_status(tasks, task_id, new_status)
            save_tasks(tasks)
        elif choice == '4':
            task_id = get_task_id()
            task_data = get_task_input()
            edit_task(tasks, task_id, task_data)
            save_tasks(tasks)
        elif choice == '5':
            task_id = get_task_id()
            delete_task(tasks, task_id)
            save_tasks(tasks)
        elif choice == '6':
            task_ids = get_task_ids()
            bulk_delete_tasks(tasks, task_ids)
            save_tasks(tasks)
        elif choice == '7':
            break
        else:
            print("Неверный выбор. Попробуйте снова.\n")

if __name__ == "__main__":
    main()