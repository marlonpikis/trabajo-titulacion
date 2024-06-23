#!/usr/bin/python3

'''
Universidad de Cuenca
Facultad de Ingeniería
Carrera de Telecomunicaciones

Trabajo de titulación

Autores:
	Marlon Xavier Gomezcoello Rodríguez
	Justin Mateo Picón Barros

Graficar tendencias de ancho de banda
'''

import matplotlib.pyplot as plt
import numpy as np
import sys
import json

UNIDAD=1e6
etiqueta='Mbps'

def leer_datos(nombre_archivo):
    valores = []
    with open(archivo) as f:
        data = json.load(f)
        for i in data['intervals']:
            BITS_PER_SECOND=i['sum']['bits_per_second']/1e6
            valores.append(BITS_PER_SECOND)
    with open(archivo[:-5]+'.txt', 'w') as f:
        for valor in valores:
            f.write(f'{valor}\n')

archivos = sys.argv[1:]
for indice, archivo in enumerate(archivos):
    print('*'*100)
    print(f'Procesando {archivo}')
    datos = leer_datos(archivo)
    y = np.loadtxt(f'{archivo[:-5]}.txt')
    
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
    plt.ylabel(f'Ancho de banda [{etiqueta}]')
    plt.savefig(f'{archivo[:-5]}_tendencias.png', dpi=300)
    plt.show()