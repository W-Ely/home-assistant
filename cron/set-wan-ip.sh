#!/bin/sh
WANIP=$(ssh admin@192.168.1.1 nvram get wan_ipaddr)
sed -i -r 's/(WANIP=)([0-9]{1,3}\.){3}[0-9]{1,3}'/"WANIP=$WANIP"/g /home/ely/home-assistant/.env