import os
from loguru import logger  # pip install loguru
from notifiers.logging import NotificationHandler
from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

params = {
    'token': os.getenv("TOKEN"),
    'chat_id': os.getenv("CHAT_ID")
}

tg_handler = NotificationHandler('telegram', defaults=params)

logger.add(tg_handler, level='CRITICAL')

logger.add('logs/log.log', rotation='10 mb', level='DEBUG')

logger.debug("Переход по ссылке avito.ru/perm")

logger.info("Запуск программы с параметрами price=200")

logger.warning("Не вижу элемента с просмотрами")

logger.error("Не удалось достать кол-во просмотров из строки")

logger.critical("Не загружается страница")
