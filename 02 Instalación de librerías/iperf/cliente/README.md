Para ejecutar la herramienta en modo cliente, se utiliza el siguiente comando:
```bash
iperf3 -c <IP_SERVIDOR>
```
Para guardar los resultados en un archivo de registros, usamos:
```bash
iperf3 -s <IP_SERVIDOR> -J --logfile <ARCHIVO_DE_SALIDA>.json
```
