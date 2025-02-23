from kafka.admin import KafkaAdminClient


def get_all_kafka_topics():
    try:
        # Connect to Kafka cluster using admin client
        with KafkaAdminClient(
            bootstrap_servers='localhost:9092',
            api_version=(0, 11)
        ) as admin_client:

            # Retrieve list of topics
            topics = admin_client.list_topics()
            return topics

    except Exception as e:
        print(f"Error while fetching Kafka topics: {e}")
        return None


# Test the function and display results
all_topics = get_all_kafka_topics()
if all_topics is not None:
    print("List of Kafka topics:", all_topics)
else:
    print("Failed to retrieve Kafka topics.")
