#!/bin/bash
cd /home/gcloud04/proj/kafka;
printf "stopping kafka\n";
(nohup bin/kafka-server-stop.sh  &) &
sleep 2;
printf "stopping zookeeper\n";
(nohup bin/zookeeper-server-stop.sh &) &
cd /home/gcloud04/gcloud04/ &
