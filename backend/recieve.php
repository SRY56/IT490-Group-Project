<?php

require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;
use PhpAmqpLib\Wire\AMQPTable;


$connection = new AMQPStreamConnection('localhost', 5672, 'it490user', 'it490pass', 'it490vhost');
$channel = $connection->channel();

$channel->queue_declare('hello', false, true, false, false, false, new AMQPTable(['x-queue-type' => 'quorum']));

echo " [*] Waiting for messages. To exit press CTRL+C\n";

$callback = function (AMQPMessage $msg) {
  echo ' [x] Received ', $msg->getBody(), "\n";
};

$channel->basic_consume('hello', '', false, true, false, false, $callback);

try {
    $channel->consume();
} catch (\Throwable $exception) {
    echo $exception->getMessage();
}
