import threading
from kafka import KafkaConsumer
import json
#from models import Forklift
import logging


class KafkaConsumerThread(threading.Thread):
    def __init__(self, topics, bootstrap_servers, loader_manager):
        super().__init__()
        self.topics = topics
        self.bootstrap_servers = bootstrap_servers
        self.loader_manager = loader_manager
        self.consumer = None

    def run(self):
        # Инициализация consumer
        self.consumer = KafkaConsumer(
            *self.topics,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True
        )

        for message in self.consumer:
            # Обработка сообщения
            self.handle_message(message)

    def handle_message(self, message):
        """
        Обрабатывает полученное сообщение и обновляет статус соответствующего \
             погрузчика.
        """
        try:
            # Извлекаем данные из сообщения (например, в формате JSON)
            data = json.loads(message.value.decode('utf-8'))

            # Определяем ID погрузчика из данных
            loader_id = data.get('loader_id')

            if not loader_id:
                print(f"Ошибка: Не найден loader_id в сообщении: {data}")
                return

            # Получаем объект погрузчика из менеджера
            loader = self.loader_manager.get_loader(loader_id)

            if not loader:
                print(f"Ошибка: Погрузчик с ID {loader_id} не найден.")
                return

            # Обновляем статус погрузчика
            new_status = data.get('status')
            if new_status:
                loader.update_status(new_status)
            else:
                print(
                    f"Ошибка: Не указан новый статус в сообщении для \
                        погрузчика {loader_id}.")

        except Exception as e:
            print(f"Произошла ошибка при обработке сообщения: {e}")
