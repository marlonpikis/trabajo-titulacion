#!/usr/bin/bash

<< COMMENT
Universidad de Cuenca
Facultad de Ingeniería
Carrera de Telecomunicaciones

Trabajo de titulación

Autores:
	Marlon Xavier Gomezcoello Rodríguez
	Justin Mateo Picón Barros

Detener los servicios
COMMENT

sudo ovs-vsctl --if-exists del-br br0
sudo systemctl stop ovs-vswitchd.service
sudo systemctl stop zebra
