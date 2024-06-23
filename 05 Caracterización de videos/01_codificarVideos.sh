#!/usr/bin/bash

<< COMMENT 
Universidad de Cuenca
Facultad de Ingeniería
Carrera de Telecomunicaciones

Trabajo de titulación

Autores:
	Marlon Xavier Gomezcoello Rodríguez
	Justin Mateo Picón Barros

Codificación inicial de videos
COMMENT

for video in *.y4m
do
    ffmpeg \
	    -hide_banner \
	    -i ${video} \
	    ${video:0:-4}.yuv
done

for video in *.yuv
do
    echo Procesando ${video}
    if [ ${video} == noticias.yuv ]
    then
	    BITRATE="70k 1703K 2580k 3457k"
    elif [ ${video} == entretenimiento.yuv ]
    then
	    BITRATE="70k 1829k 2770k 3712k"
    elif [ ${video} == tiemporeal.yuv ]
    then
	    BITRATE="70k 2051k 3107k 4164k"
    fi
    echo ${BITRATE}
    for bitrate in ${BITRATE}
    do
        ffmpeg \
		-hide_banner \
		-s cif \
		-i ${video} \
		-c:v libx264 \
		-b:v ${bitrate} \
		${video:0:-4}_${bitrate}.mp4
    done
done

for video in *.yuv
do
	rm ${video}
done
