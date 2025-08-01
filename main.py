import paho.mqtt.client as mqtt
import time
import traceback
import os

BROKER = os.getenv("MQTT_BROKER", "z05c66ff.ala.eu-central-1.emqxsl.com")
PORT = int(os.getenv("MQTT_PORT", "8883"))
TOPIC = os.getenv("MQTT_TOPIC", "myapp/feedback")
USERNAME = os.getenv("MQTT_USERNAME", "fb")
PASSWORD = os.getenv("MQTT_PASSWORD", "junhj14")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT broker")
        client.subscribe(TOPIC)
    else:
        print("❌ Connection failed with code", rc)

def on_message(client, userdata, msg):
    try:
        print(f"📩 Message received on {msg.topic}: {msg.payload.decode()}")
    except Exception:
        print("⚠️ Error processing message:")
        traceback.print_exc()

while True:
    try:
        client = mqtt.Client()
        client.username_pw_set(USERNAME, PASSWORD)
        client.tls_set()  # 기본 시스템 인증서 사용
        client.tls_insecure_set(True)  # 인증서 검증 생략 (테스트용)

        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(BROKER, PORT)
        client.loop_forever()
    except Exception:
        print("🔁 MQTT client error, retrying in 5 seconds...")
        traceback.print_exc()
        time.sleep(5)
