# Guia de uso del sistema de control de video adaptativo

Primeramente es necesario que el cliente esté listo para reproducir video para lo cual usamos el siguiente comando:
```bash
ffplay <url del servidor>
```
Luego ejecutamos el codigo de Python con el siguiente comando:
```bash
sudo python3 adaptivo_final.py
```
Realizado esto, se mostrará la siguiente interfaz de usuario

![interfaz(1)](https://github.com/marlonpikis/trabajo-titulacion/assets/173454467/6d85a32a-a5a0-4366-8129-ea3853c2886d)

La interfaz es bastante intuitiva, para transmitir se siguen los siguientes pasos:
1. ingresar la dirección IP del cliente
2. Seleccionar la categoría del video a transmitir
3. Iniciar transmisión

Luego de iniciar la transmision, se mostrara solamente la tasa de codificacion de 70 Kbps, luego de medir el ancho de banda de la red se mostrará dicho valor y la nueva tasa de codificacion.

Si se pulsa el botón `demo` no se medirá el ancho de banda, simplemente se transmitira en tres tasas de codificacion con las cuales será mas evidente el cambio de calidad.
