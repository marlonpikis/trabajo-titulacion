#!/usr/bin/bash

<< COMMENT
Universidad de Cuenca
Facultad de Ingeniería
Carrera de Telecomunicaciones

Trabajo de titulación

Autores:
	Marlon Xavier Gomezcoello Rodríguez
	Justin Mateo Picón Barros

Obtener tasa de bits de tráfico real
COMMENT

for ARCHIVO in ./*.pcapng
do
	echo Procesando: ${ARCHIVO}
	SALIDA=$(mktemp -p .)
	if [ ${ARCHIVO} == ./entretenimiento.pcapng ]
	then
		IP=18.64.174.26
	elif [ ${ARCHIVO} == ./noticias.pcapng ]
	then
		IP=152.199.52.215
	elif [ ${ARCHIVO} == ./tiempo-real.pcapng ]
	then
		IP=99.181.81.212
	fi

	sudo tcpdump -r ${ARCHIVO} src host ${IP} -w ${SALIDA}

	FILE=${ARCHIVO:0:-7}.txt
	tcpstat -r ${SALIDA} -o "%b\n" 1 > ${FILE}

	rm -rf ${SALIDA}
done
