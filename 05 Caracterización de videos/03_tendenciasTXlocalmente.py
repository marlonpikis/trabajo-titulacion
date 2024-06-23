#!/usr/bin/python3

'''
Universidad de Cuenca
Facultad de Ingeniería
Carrera de Telecomunicaciones

Trabajo de titulación

Autores:
	Marlon Xavier Gomezcoello Rodríguez
	Justin Mateo Picón Barros

Graficar tendencias de videos transmitidos localmente
'''

import matplotlib.pyplot as plt
import numpy as np
import sys

UNIDAD=1e6
etiqueta='Mbps'

archivos = sys.argv[1:]
for indice, archivo in enumerate(archivos):
    print('*'*100)
    print(f'Procesando {archivo}')
    y = np.loadtxt(archivo)/UNIDAD
    
    bitrate_data = np.array([y])
    media = np.mean(bitrate_data)
    desviacion_estandar = np.std(bitrate_data)
    varianza = np.var(bitrate_data)
    maximo = np.max(bitrate_data)
    minimo = np.min(bitrate_data)
    
    print(f'''\
Media:\t{media} {etiqueta}
Desviación estándar:\t{desviacion_estandar} {etiqueta}
Varianza:\t{varianza} {etiqueta}
Máximo:\t{maximo} {etiqueta}
Mínimo:\t{minimo} {etiqueta}''')

    x = np.arange(0, len(y), 1)
    
    plt.stem(x, y)
    plt.xlabel('Tiempo [s]')
    plt.ylabel(f'Tasa de bits [{etiqueta}]')
    plt.savefig(f'{archivo[:-4]}_tendencias.png', dpi=300)
    plt.show()
