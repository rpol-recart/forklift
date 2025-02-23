import pytest
from kafka import KafkaProducer, KafkaConsumer
import time


@pytest.fixture(scope="function")
def kafka_producer():
    """Fixture for creating a Kafka producer."""
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        api_version=(0, 11)  # Ensure compatibility with your Kafka version
    )
    yield producer
    # Cleanup after test execution
    producer.close()


@pytest.fixture(scope="function")
def kafka_consumer():
    """Fixture for creating a Kafka consumer."""
    consumer = KafkaConsumer(
        'test-topic',  # Replace with your test topic
        bootstrap_servers='81.94.156.249:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=False,
        api_version=(0, 11)  # Ensure compatibility with your Kafka version
    )
    yield consumer
    # Cleanup after test execution
    consumer.close()


def test_kafka_integration(kafka_producer, kafka_consumer):
    """Test sending and receiving a message from Kafka."""
    # Send a message
    future = kafka_producer.send('test-topic', value=b'test-message')
    future.get(timeout=10)  # Ensure the message is sent
    print(future)
    time.sleep(3)
    # Consume messages
    records = list(kafka_consumer.poll(20, max_records=1,update_offsets=False))
    print(records)
    assert len(records) == 1, "No message was received from Kafka."

    for record in records:
        assert record.value == b'test-message', f"Expected 'test-message' but got {record.value}"
