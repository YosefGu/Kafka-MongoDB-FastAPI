from kafka import KafkaProducer
import json
import os

class Connector():

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=os.getenv('BOOTSTRP_SERVER'),
            value_serializer=lambda x:
            json.dumps(x).encode('utf-8')
            )
        

    def publish_message(self, topic, message):
        try:
            self.producer.send(topic, message)
            self.producer.flush()
            # print(f"Publis seccessfully to {topic}")
        except Exception as e:
            print("Error publishing")
            print(e)
