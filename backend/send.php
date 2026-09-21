<?php

require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;
use PhpAmqpLib\Wire\AMQPTable;

$connection = new AMQPStreamConnection('localhost', 5672, 'it490user', 'it490pass','it490vhost');
$channel = $connection->channel();

$channel->queue_declare('hello', false, true, false, false, false, new AMQPTable(['x-queue-type' => 'quorum']));

$msg = new AMQPMessage('hi aayush');
$channel->basic_publish($msg, '', 'hello');

echo " [x] Sent 'sup aayush'\n";

$channel->close();
$connection->close();


