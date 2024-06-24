'''
Universidad de Cuenca
Facultad de Ingeniería
Carrera de Telecomunicaciones

Trabajo de titulación

Autores:
	Marlon Xavier Gomezcoello Rodríguez
	Justin Mateo Picón Barros

Inicializar el servicio de OVS en todos los nodos
'''

import paramiko

comando='./initOVSconfigurations.sh'
port = 22
username = 'usuario'
password = '1234'

for i in range(100, 104):
    print(f"Conectando a 192.168.1.{i}")
    host = f'192.168.1.{i}'
    try:
        # Crea un cliente SSH
        client = paramiko.SSHClient()

        # Configura el cliente para que no solicite confirmación de clave pública
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Conecta al servidor
        client.connect(host, port, username, password)

        # Abre una sesión SSH
        session = client.get_transport().open_session()
        session.get_pty()  # Obtener pseudo-terminal

        # Ejecuta un comando con sudo
        session.exec_command(f'sudo -S -p "" {comando}\n')

        # Enviar la contraseña
        session.sendall(password + '\n')

        # Leer la salida del comando
        stdout = session.makefile('r', -1)
        stderr = session.makefile_stderr('r', -1)
        exit_status = session.recv_exit_status()

        # Imprimir la salida
        print("STDOUT:\n", stdout.read().decode())
        print("STDERR:\n", stderr.read().decode())

    except paramiko.SSHException as e:
        print(f"Error de SSH al conectar a 192.168.1.{i}: {str(e)}")
    except Exception as e:
        print(f"Ocurrió un error al conectar a 192.168.1.{i}: {str(e)}")
    finally:
        # Cierra la conexión
        client.close()