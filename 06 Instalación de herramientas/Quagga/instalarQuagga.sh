#!/usr/bin/bash

<< COMMENT
Universidad de Cuenca
Facultad de Ingeniería
Carrera de Telecomunicaciones

Trabajo de titulación

Autores:
    Marlon Xavier Gomezcoello Rodríguez
    Justin Mateo Picón Barros

Instalar la suite de Quagga
COMMENT

sudo apt update && sudo apt upgrade -y
sudo apt install -y quagga
sudo sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/g' /etc/sysctl.conf
sudo sysctl -p

sudo cp /usr/share/doc/quagga-core/examples/ospfd.conf.sample /etc/quagga/ospfd.conf
sudo cp /usr/share/doc/quagga-core/examples/ripd.conf.sample /etc/quagga/ripd.conf
sudo cp /usr/share/doc/quagga-core/examples/vtysh.conf.sample /etc/quagga/vtysh.conf
sudo cp /usr/share/doc/quagga-core/examples/zebra.conf.sample /etc/quagga/zebra.conf

sudo chown quagga:quagga /etc/quagga/*.conf
sudo chown quagga:quaggavty /etc/quagga/vtysh.conf
sudo chmod 640 /etc/quagga/*.conf
sudo mkdir /var/log/quagga/
sudo chown quagga:quagga /var/log/quagga/
sudo touch /var/log/zebra.log
sudo chown quagga:quagga /var/log/zebra.log

sudo systemctl start zebra.service
sudo systemctl start ripd.service
sudo systemctl start ospfd.service