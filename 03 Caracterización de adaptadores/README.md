Aquí se detallará el procedimiento para caracterizar los adaptadores USB a Ethernet que hemos utilizado. 

Las pruebas a realizar son:
- Ethernet con adaptador
- Adaptador con adaptador

Pasos:
1. Debemos configurar iperf en modo [servidor](../02%20Instalación%20de%20librerías/iperf/servidor/README.md) en uno de los nodos
2. Ejecutar iperf en modo [cliente](../02%20Instalación%20de%20librerías/iperf/cliente/README.md) colocando la IP del servidor del punto 1
3. Obteniendo los dos archivos `.json`, obtenemos el gráfico de tendencias así:
```bash
./01_tendenciasAnchoDeBanda.py <archivo_1>.json <archivo_2>.json
```
4. Para comparar estadísticas mediante el intervalo de confianza, usamos
```bash
./02_estadisticasAnchosDeBanda.py <archivo_1>.txt <archivo_2>.txt
```
