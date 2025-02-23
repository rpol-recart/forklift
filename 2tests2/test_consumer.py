from unittest.mock import patch
import pytest


@pytest.mark.asyncio
async def test_process_messages():
    with patch('app.consumer.KafkaConsumer') as mock_consumer:
        # Настройте мок для возврата определенных сообщений
        mock_consumer.return_value = [b'{"id": 1, "name": "Test"}']

        from app import consumer
        await consumer.process_messages()

        # Проверьте, что методы были вызваны правильно
        mock_consumer.assert_called_once()
