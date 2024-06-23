#!/usr/bin/python3

'''
Universidad de Cuenca
Facultad de Ingeniería
Carrera de Telecomunicaciones

Trabajo de titulación

Autores:
	Marlon Xavier Gomezcoello Rodríguez
	Justin Mateo Picón Barros

Graficar intervalo de confianza de tráfico real
'''

import matplotlib.pyplot as plt
import numpy as np
import sys
from math import sqrt

UNIDAD=1e6
etiqueta='Mbps'
colores = ['tab:blue',
           'tab:orange',
           'tab:green',
           'tab:red',
           'tab:purple',
           'tab:brown',
           'tab:pink',
           'tab:gray',
           'tab:olive',
           'tab:cyan']

def graficar_intervalo_confianza(x, valores, z=1.96, color='#2187bb', ancho=0.25):
    promedio = np.mean(valores)
    desviacion_estandar = np.std(valores)
    intervalo_confianza = z * desviacion_estandar / sqrt(len(valores))
    print(f'Intervalo de confianza: +-{intervalo_confianza} {etiqueta}')
    superior = promedio + intervalo_confianza
    inferior = promedio - intervalo_confianza
    plt.plot([x, x], [superior, inferior], color=color)
    plt.plot(x, superior, 'o')
    plt.plot(x, inferior, 'o')
    pass

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
    
    graficar_intervalo_confianza(indice, y, color='#ff0000')
    plt.bar(indice, media, 0.2, color=colores[indice])

plt.ylabel('Tasa de bits [Mbps]')
plt.xticks(list(range(0, len(archivos))), [archivo[:-4].upper() for archivo in archivos])

plt.savefig('traficoReal.png', dpi=300)
plt.show()