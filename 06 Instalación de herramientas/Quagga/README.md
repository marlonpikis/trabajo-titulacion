Para instalar la suite de Quagga, debemos ejecutar:
```bash
./instalarQuagga.sh
```
Después del reinicio, comprobar que existe un `1` al momento de ejecutar:
```bash
cat /proc/sys/net/ipv4/ip_forward
```
Para comprobar la vesión que tenemos instalada, ejecutamos:
```bash
zebra --version
```
En nuestro caso, la versión instalada es la `zebra version 1.2.4`.
