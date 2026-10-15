import pika

creds = pika.PlainCredentials("Aayush", "urmom123")
conn = pika.BlockingConnection(
    pika.ConnectionParameters("100.70.116.108", credentials=creds)
)
ch = conn.channel()

ch.queue_declare(queue="backend_start")

ch.basic_publish(
    exchange="",
    routing_key="backend_start",
    body="start"
)

print("Sent start signal to backend")
conn.close()
