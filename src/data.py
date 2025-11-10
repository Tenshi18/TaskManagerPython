import json
from typing import List
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def load_tasks() -> List[dict]:
    try:
        with open('tasks.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error("Файл tasks.json не найден")
        return []
    except json.JSONDecodeError:
        logger.error("Ошибка при парсинге tasks.json")
        return []

def save_tasks(tasks: List[dict]) -> None: 
    try:
        with open('tasks.json', 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
    except PermissionError:
        logger.error("Ошибка: Нет прав на запись в файл tasks.json")
    except OSError:
        logger.error("Ошибка при записи в файл tasks.json")