Para instalar Open vSwitch, ejecutamos:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y openvswitch-switch
```
Para comprobar la versión, usamos:
```bash
ovs-vswitchd --version
ovs-vsctl --version
```
En nuestro caso, la versión instada es `ovs-vswitchd (Open vSwitch) 2.13.8`.
