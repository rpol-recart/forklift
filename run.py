from flask import Flask
from app.routes import monitoring_bp
from app.models import LoaderManager
from app.consumer import KafkaConsumerThread


server = Flask(__name__)
server.register_blueprint(monitoring_bp, url_prefix='/api')

if __name__ == '__main__':
    # Список топиков для监听
    topics = ['loader_status_updates', 'another_topic']

    # Параметры Kafka
    bootstrap_servers = 'localhost:9092'

    # Создаем менеджера погрузчиков и добавляем погрузчики
    loader_manager = LoaderManager()
    loader_manager.add_loader('loader_001')
    loader_manager.add_loader('loader_002')
    server.loader_manager = loader_manager
    # Создаем и запускаем поток для слушания Kafka
    consumer_thread = KafkaConsumerThread(
        topics=topics,
        bootstrap_servers=bootstrap_servers,
        loader_manager=loader_manager
    )
    consumer_thread.start()
    print("Поток запущен. Для остановки нажмите Ctrl+C.")

    # Запуск сервера
    server.run(debug=True)
