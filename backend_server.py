import pika

# connect to Omar's broker
creds = pika.PlainCredentials("Aayush", "urmom123")
conn = pika.BlockingConnection(
    pika.ConnectionParameters("100.70.116.108", credentials=creds)
)
ch = conn.channel()

# make sure omars queue is there
ch.queue_declare(
    queue="rpc_queue",
    durable=True,
    arguments={"x-queue-type": "quorum"}
)


# runs every time a request comes in
def on_request(ch, method, props, body):
    message = body.decode()
    print("Got a request:", message)

    reply = "backend got your message"

    ch.basic_publish(
        exchange="",
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=reply
    )

    ch.basic_ack(delivery_tag=method.delivery_tag)


# start listening
ch.basic_consume(queue="rpc_queue", on_message_callback=on_request)

print("Waiting for requests")
ch.start_consuming()
