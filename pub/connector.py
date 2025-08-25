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
