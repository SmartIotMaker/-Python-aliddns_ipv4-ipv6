#! /bin/bash
cd /home/pi/Python-aliddns
while true
do
	/usr/bin/python3 /home/pi/Python-aliddns/ddns.py
	sleep 3600
done
