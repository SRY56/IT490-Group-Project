import pika

creds = pika.PlainCredentials("Aayush", "urmom123")
conn = pika.BlockingConnection(
    pika.ConnectionParameters("100.70.116.108", credentials=creds)
)
ch = conn.channel()

ch.queue_declare(queue="frontend_start")

ch.basic_publish(
    exchange="",
    routing_key="frontend_start",
    body="start"
)

print("Sent start signal from aayush")
conn.close()
