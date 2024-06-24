#!/usr/bin/bash

<< COMMENT
Universidad de Cuenca
Facultad de Ingeniería
Carrera de Telecomunicaciones

Trabajo de titulación

Autores:
	Marlon Xavier Gomezcoello Rodríguez
	Justin Mateo Picón Barros

Inicializar el servicio de OVS en R4
COMMENT

sudo systemctl stop zebra

sudo systemctl start ovs-vswitchd.service

PUERTOS="eth0 eth1 eth2 eth3"
IP_RYU=192.168.1.254
PUENTE=br0

sudo ovs-vsctl add-br $PUENTE
sudo ovs-vsctl set Bridge $PUENTE other-config:datapath-id=000000000000004

for i in $PUERTOS
do
	PUERTO=$i
	sudo ifconfig $PUERTO 0
	sudo ovs-vsctl add-port $PUENTE $PUERTO
done

sudo ovs-vsctl set-controller $PUENTE tcp:$IP_RYU:6633
sudo ovs-vsctl set-fail-mode $PUENTE secure
sudo ovs-vsctl show
