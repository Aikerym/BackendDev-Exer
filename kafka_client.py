import requests
from dataclasses import asdict

class KafkaClient:
    def __init__(self, host: str) -> None:
        self.host = host
    
    def send(self, topic: str, message) -> None:
        url = self.host + '/api/kafkauniversal/write'
        response = requests.post(
            url=url,
            json={
                "businessKey": "aikerim1",
                "channelId": "aikerim1",
                "commitWhenRead": True,
                "guarantedWrite": True,
                "processName": "aikerim1",
                "topic": topic,
                "message": message,
            }
        )
        print(response.json())
