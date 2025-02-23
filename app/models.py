from datetime import datetime, timezone


class Forklift:
    def __init__(self, forklift_id: str, name: str, status: dict):
        self.forklift_id = forklift_id
        self.name = name
        self.status = status  # Словарь с данными о состоянии

    def update_status(self, new_status: dict):
        self.status = new_status


class Loader:
    def __init__(self, loader_id):
        self.loader_id = loader_id
        self.status = None  # Стартовый статус
        self.operation_time = None

    def update_status(self, new_status):
        """
        Обновляет статус погрузчика и выполняет соответствующие логические
        функции.
        """
        print(
            f"Погрузчик {self.loader_id}: Изменение статуса с '{self.status}' \
                на '{new_status}'.")

        # Выполнение дополнительных действий при изменении статуса
        if new_status == 'full':
            self.get_container()
        elif new_status == 'empty':
            self.put_container()
        else:
            print(f"Неизвестный статус: {new_status}")

        self.status = new_status

    def set_operation_time(self, operation_time: int):
        self.operation_time = operation_time

    def get_container(self):
        """
        Логика, выполняемая при изменении статуса на 'full'.
        """
        print(f"Погрузчик {self.loader_id}: Взятие контейнера.")
        self.set_operation_time(self.get_timestamp())

    def put_container(self):
        """
        Логика, выполняемая при изменении статуса на 'empty'.
        """
        print(f"Погрузчик {self.loader_id}: Постановка контейнера")
        self.set_operation_time(self.get_timestamp())

    def get_timestamp(self):
        '''
        Return timestamp in server time (unix time +0 timezone)
        '''
        return int(datetime.now(timezone.utc).timestamp())


class LoaderManager:
    def __init__(self):
        self.loaders = {}

    def add_loader(self, loader_id):
        """
        Добавляет новый погрузчик в менеджер.
        """
        if loader_id not in self.loaders:
            self.loaders[loader_id] = Loader(loader_id)
            print(f"Добавлен погрузчик с ID: {loader_id}")

    def get_loader_by_id(self, loader_id):
        """
        Возвращает объект погрузчика по его ID.
        """
        return self.loaders.get(loader_id, None)
