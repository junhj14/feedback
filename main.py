import paho.mqtt.client as mqtt

BROKER = "z05c66ff.ala.eu-central-1.emqxsl.com"
PORT = 8084
TOPIC = "myapp/feedback"
USERNAME = "fb"
PASSWORD = "junhj14"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
        client.subscribe(TOPIC)
    else:
        print("Connect failed with code", rc)

def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client(transport="websockets")  # 웹소켓 연결 설정
client.username_pw_set(USERNAME, PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

# TLS 옵션 필요 시 주석 해제하고 조정 가능
# client.tls_set() 

client.connect(BROKER, PORT)
client.loop_forever()
