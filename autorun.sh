#! /bin/bash
cd /home/pi/Python-aliddns_ipv4-ipv6
while true
do
	/usr/bin/python3 /home/pi/Python-aliddns_ipv4-ipv6/ddns.py
	sleep 3600
done
