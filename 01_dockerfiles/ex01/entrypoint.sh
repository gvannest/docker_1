#!/bin/bash
touch $TS3SERVER_ROUTE/.ts3server_license_accepted
$TS3SERVER_ROUTE/teamspeak3-server_linux_amd64/ts3server_startscript.sh start inifile=ts3server.ini

