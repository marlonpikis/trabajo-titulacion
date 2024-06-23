#!/usr/bin/bash

<< COMMENT
Universidad de Cuenca
Facultad de Ingeniería
Carrera de Telecomunicaciones

Trabajo de titulación

Autores:
	Marlon Xavier Gomezcoello Rodríguez
	Justin Mateo Picón Barros

Transmitir video localmente y obtener datos de tasa de bits
COMMENT

for VIDEO in *.mp4
do
	echo Procesando ${VIDEO}
	CAPTURA=$(mktemp -p .)

	gnome-terminal -- bash -c "sudo tcpdump -i lo udp port 1234 -w ${CAPTURA}; exe bash"
	sleep 5

	gnome-terminal -- bash -c "ffmpeg -re -i ${VIDEO} -c:v copy -f mpegts udp://127.0.0.1:1234; exit; exec bash"
	read -p "Presione Enter cuando haya terminado automáticamente ffmpeg y cerrado tcpdump manualmente"

	RESULTADOS=${VIDEO:0:-4}.txt

	tcpstat -r ${CAPTURA} -o "%b\n" 1 > ${RESULTADOS}

	rm -rf ${CAPTURA}
done
