Para instalar el controlador SDN ejecutamos:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y pyhton3-pip
git clone https://github.com/faucetsdn/ryu.git
cd ryu/
sudo python3 ./setup.py install
sudo pip3 install --upgrade ryu
```
Para comprobar su instalación, podemos ejecutar el ejemplo:
```bash
ryu-manager ryu/app/simple_switch_13.py
```
Para saber la versión instalada, ejecutamos:
```bash
ryu-manager --version
```
En nuestro caso, tenemos la `ryu-manager 4-34`.
