from kafka import KafkaConsumer
import json
import os

class KafkaConn():

    def __init__(self, topic):
        self.topic = topic
        
    
    def get_consumer_event(self):
        consumer_events = KafkaConsumer(
            self.topic,
            group_id=f'{self.topic}-group',
            value_deserializer=lambda m: json.loads(m.decode('ascii')),
            bootstrap_servers= os.getenv('BOOTSTRP_SERVER'),
            consumer_timeout_ms=10000)
        return consumer_events