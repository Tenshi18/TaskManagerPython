from typing import List, Dict
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def add_task(tasks: List[Dict], task_data: Dict) -> None:
    try:
        new_id = max(task['id'] for task in tasks) + 1 if tasks else 1

        new_task = {
            'id': new_id,
            'name': task_data['name'],
            'description': task_data['description'],
            'status': 'новая'
        }
        tasks.append(new_task)
        logger.debug(f"Задача {new_task['name']} добавлена")
    except ValueError as e:
        logger.debug(f"Ошибка при добавлении задачи: {e}")
        raise
    except TypeError as e:
        logger.debug(f"Ошибка при добавлении задачи: {e}")
        raise

def change_status(tasks: List[Dict], task_id: int, new_status: str) -> bool:
    try:
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task:
            task['status'] = new_status
            logger.info(f"Статус задачи {task['name']} изменен на {new_status}")
            return True
        else:
            logger.error(f"Задача с ID {task_id} не найдена")
            return False
    except ValueError as e:
        logger.debug(f"Ошибка при изменении статуса задачи: {e}")
        raise
    except TypeError as e:
        logger.error(f"Ошибка при изменении статуса задачи: {e}")
        raise
    except Exception as e:
        logger.error(f"Неизвестная ошибка при изменении статуса задачи: {e}")
        raise

def edit_task(tasks: List[Dict], task_id: int, task_data: Dict) -> bool:
    try:
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task:
            task['name'] = task_data['name']
            task['description'] = task_data['description']
            logger.debug(f"Задача {task['name']} изменена")
            return True
        else:
            logger.error(f"Задача с ID {task_id} не найдена")
            return False
    except ValueError as e:
        logger.error(f"Ошибка при редактировании задачи: {e}")
        raise
    except TypeError as e:
        logger.error(f"Ошибка при редактировании задачи: {e}")
        raise

def delete_task(tasks: List[Dict], task_id: int) -> bool:
    try:
        task = next((task for task in tasks if task['id'] == task_id), None)
        if task:
            tasks.remove(task)
            logger.debug(f"Задача {task['name']} удалена")
            return True
        else:
            logger.error(f"Задача с ID {task_id} не найдена")
            return False
    except ValueError as e:
        logger.error(f"Ошибка при удалении задачи: {e}")
        raise

def bulk_delete_tasks(tasks: List[Dict], task_ids: List[int]) -> bool:
    try:
        for task_id in task_ids:
            delete_task(tasks, task_id)
        logger.info(f"Задачи с ID {task_ids} удалены")
        return True
    except ValueError as e:
        logger.error(f"Ошибка при удалении задач: {e}")
        raise
    except TypeError as e:
        logger.error(f"Ошибка при удалении задач: {e}")
        raise
    except Exception as e:
        logger.error(f"Неизвестная ошибка при удалении задач: {e}")
        raise