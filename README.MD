# PiRowFlo MQTT for Waterrower

This is a clone of inonoob's most excellent [pirowflo](https://github.com/inonoob/pirowflo/) repo modified to add MQTT support.  Aside from a few minor tweaks, the rest of PiRowFlo's functionality remains largely unchanged.  If you're not interested in MQTT support, best to stick with the original.    

##### Why MQTT support?  
Mainly to support my own personal data visualization projects.  I wanted to make my own charts and dashboards rather than use an app to track my workouts.  


##### Installation
Install remains pretty much the same.  See [the original README](README-ORIGINAL.MD) for additional details.  

On a fresh install of RaspbianOS:
```bash
sudo apt-get install git
cd ~/
git clone https://github.com/inonoob/pirowflo.git
cd pirowflo
sudo chmod +x install.sh
sudo ./install.sh
```

Before running PiRowFlo MQTT you'll need to edit a couple of config files required for the MQTT service:  

*.env*   
Location:  ~/pirowflo_mqtt/src/adapters/s4/.env
```
MQ_USER='MQTT_PUBLISHER_USERNAME'
MQ_PASSWORD='MQTT_PUBLISHER_PASSWORD'
```

*mqtt_settings.py*  
Location:  ~/pirowflo_mqtt/src/adapters/s4/mqtt_settings.py
```
mq_server_url = "10.0.20.26"
mq_client_id = "pirowflo"
mq_device_name = "Waterrower data publisher"
mq_user = os.environ.get("MQ_USER")
mq_password = os.environ.get("MQ_PASSWORD")
mq_topic = "waterrower/data"
```

