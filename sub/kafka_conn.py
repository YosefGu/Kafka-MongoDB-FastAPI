from kafka import KafkaConsumer
import json
import os

class KafkaConn():

    def __init__(self, topic):
        self.topic = topic
        
    
    def get_consumer_event(self):
        consumer_event = KafkaConsumer(
            self.topic,
            group_id=f'{self.topic}-group',
            value_deserializer=lambda m: m.decode('utf-8'),
            bootstrap_servers= os.getenv('BOOTSTRP_SERVER'),
            consumer_timeout_ms=60000)
        return consumer_event