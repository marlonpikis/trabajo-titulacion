Aquí se detallará el procedimiento a seguir para obtener estadísticas del tráfico de red que se da al momento de consumir transmisiones reales de video.

Pasos:
1. Podemos capturar, con Wireshark, el tráfico de red mientras consumimos un servicio de streaming. Debemos identificar la IP del servidor que nos envía dicha transmisión de video. 
2. Con el archivo .pcapng, ejecutamos el siguiente comando para obtener los datos de tasa de bits:
```bash
./01_tasa-bitsTraficoReal.sh
```
3. Se generarán archivos `.txt` con la información requerida.
4. Para obtener la tendencia, ejecutamos:
```bash
./02_tendenciasTraficoReal.py <archivo_1>.txt <archivo_2>.txt ...
```
5. Para graficar al intervalo de confianza, ejecutamos:
```bash
./03_estadisticasTraficoReal.py <archivo_1>.txt <archivo_2>.txt ...
```
