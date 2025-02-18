import time
import logging
import json
import paho.mqtt.client as mqtt

from . import mqtt_settings

logger = logging.getLogger(__name__)

class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client(client_id=mqtt_settings.mq_client_id, clean_session=True)
        self.client.username_pw_set(mqtt_settings.mq_user, mqtt_settings.mq_password)
        self.client.on_connect = self._on_connect
        self.client.on_disconnect = self._on_disconnect
        self.last_publish = time.time()
        self.topic = mqtt_settings.mq_topic
        
        try:
            self.client.connect(mqtt_settings.mq_server_url, port=1883, keepalive=60)
            self.client.loop_start()
        except Exception as e:
            logger.error(f"MQTT connection failed: {str(e)}")

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logger.info("Connected to MQTT broker successfully")
        else:
            logger.error(f"MQTT connection failed with code: {rc}")

    def _on_disconnect(self, client, userdata, rc):
        logger.warning(f"Disconnected from MQTT broker with code: {rc}")
        try:
            self.client.reconnect()
        except Exception as e:
            logger.error(f"Reconnection failed: {str(e)}")

    def publish(self, payload):
        self.client.publish(self.topic, json.dumps(payload))