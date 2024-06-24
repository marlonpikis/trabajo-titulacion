#!/usr/bin/bash

<< COMMENT
Universidad de Cuenca
Facultad de Ingeniería
Carrera de Telecomunicaciones

Trabajo de titulación

Autores:
        Marlon Xavier Gomezcoello Rodríguez
        Justin Mateo Picón Barros

Inicializar el servicio de OVS en R1
COMMENT

sudo systemctl stop zebra

sudo systemctl start ovs-vswitchd.service

PUERTOS="eth0 eth1 eth2"
IP_RYU=192.168.1.254
PUENTE=br0

sudo ovs-vsctl add-br ${PUENTE}
sudo ovs-vsctl set Bridge ${PUENTE} other-config:datapath-id=0000000000000001

for i in ${PUERTOS}
do
	sudo ifconfig ${i} 0
	sudo ovs-vsctl add-port ${PUENTE} ${i}
done

sudo ovs-vsctl set-controller ${PUENTE} tcp:${IP_RYU}:6633
sudo ovs-vsctl set-fail-mode ${PUENTE} secure
sudo ovs-vsctl show