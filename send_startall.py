import pika

creds = pika.PlainCredentials("Aayush", "urmom123")
conn = pika.BlockingConnection(
    pika.ConnectionParameters("100.70.116.108", credentials=creds)
)
ch = conn.channel()

for q in ["backend_start", "database_start", "frontend_start"]:
    ch.queue_declare(queue=q)
    ch.basic_publish(exchange="", routing_key=q, body="start")
    print("Sent start to", q)

conn.close()

