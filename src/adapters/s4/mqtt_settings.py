import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

mq_server_url = "10.0.20.26"
mq_client_id = "pirowflo"
mq_device_name = "Waterrower data publisher"
mq_user = os.environ.get("MQ_USER") # multipass.read('secret/etl/mq/user')['data']['user']
mq_password = os.environ.get("MQ_PASSWORD") # multipass.read('secret/etl/mq/password')['data']['password']
mq_topic = "waterrower/data"

