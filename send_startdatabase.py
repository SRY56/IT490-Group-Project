import pika

creds = pika.PlainCredentials("Aayush", "urmom123")
conn = pika.BlockingConnection(
    pika.ConnectionParameters("100.70.116.108", credentials=creds)
)
ch = conn.channel()

ch.queue_declare(queue="database_start")

ch.basic_publish(
    exchange="",
    routing_key="database_start",
    body="start"
)

print("Sent start signal to database")
conn.close()
