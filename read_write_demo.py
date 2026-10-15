import pika

creds = pika.PlainCredentials("Aayush", "urmom123")
conn = pika.BlockingConnection(
    pika.ConnectionParameters("100.70.116.108", credentials=creds)
)
ch = conn.channel()

# read the message from the queue
method_frame, header_frame, body = ch.basic_get(queue="cheese")
print("READ from cheese:", body.decode())
ch.basic_ack(method_frame.delivery_tag)

# write a reply back
ch.basic_publish(exchange="", routing_key="cheese", body="backend read it and wrote back")
print("wrote back to cheese")

conn.close()
