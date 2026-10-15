import pika
import subprocess

# connect to Omar's broker
creds = pika.PlainCredentials("Aayush", "urmom123")
conn = pika.BlockingConnection(
    pika.ConnectionParameters("100.70.116.108", credentials=creds)
)
ch = conn.channel()

# watch the start queue
ch.queue_declare(queue="backend_start")


# runs when a start signal comes in
def on_start(ch, method, props, body):
    message = body.decode()

    if message == "start":
        print("Got start signal launching backend")
        subprocess.Popen(["python3", "backend_server.py"])

    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Message received:", body.decode())

# listen for the signal
ch.basic_consume(queue="backend_start", on_message_callback=on_start)

print("Waiting for start signal")
ch.start_consuming()
