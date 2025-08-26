from kafka import KafkaConsumer
import json
import os

class KafkaConn():

    def __init__(self, topic):
        self.topic = topic
        self.consumer = KafkaConsumer(
            self.topic,
            group_id=f'{self.topic}-group',
            value_deserializer=lambda m: m.decode('utf-8'),
            bootstrap_servers= os.getenv('BOOTSTRAP_SERVER'),
            )
        
    
    def get_consumer_event(self):
        data = self.consumer.poll(timeout_ms=5000, max_records=10)
        all_messages = []
        for record in data.values():
            all_messages.extend(record)
        return all_messages