#!/bin/sh
cd /home/gcloud04/proj/kafka;
printf "starting zookeeper\n";
(nohup bin/zookeeper-server-start.sh config/zookeeper.properties &) &
sleep 2;
printf "starting kafka\n";
(nohup bin/kafka-server-start.sh config/server.properties  &) &
cd /home/gcloud04/gcloud04/ &
