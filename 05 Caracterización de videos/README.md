Aquí de detallará el procedimiento para codificar videos según las tasas de codificación que se ha escogido. Seguido a eso, se transmitirá localmente el video codificado y se analizará su perfil de tráfico.

Pasos:
1. Haber descargado los videos en formato `.yuv`.
2. Para codificar los videos usamos:
```bash
./01_codificarVideos.sh
```
3. Para transmitir localmente el video, realizando una captura del tráfico de red, usamos:
```bash
./02_transmitir.sh
```
4. Para obtener las tendencias de los archivos `.txt` generados, usamos:
```bash
./03_tendenciasTXlocalmente.py <archivo_1>.txt <archivo_2>.txt ...
```
5. Para graficar el intervalo de confianza de las muestras obtenidas, se ejecuta:
```bash
./04_estadisticasTXlocalmente.py <archivo_1>.txt <archivo_2>.txt ...
```
