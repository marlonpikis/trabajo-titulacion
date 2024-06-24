import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import threading
import time
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Diccionario para almacenar las rutas de los videos de cada categoría
videos = {
    "Noticias": "/home/marlon/tesis/Videosy4m/noticias_dup1.y4m",
    "Entretenimiento": "/home/marlon/tesis/Videosy4m/deportes_dup1.y4m",
    "Tiempo Real": "/home/marlon/tesis/Videosy4m/videovigilancia_dup1.y4m"
}
# Función para cargar el video correspondiente a la categoría seleccionada
def select_category(category):
    global selected_category
    selected_category = category
    file_path = videos.get(category)
    if file_path:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, file_path)
# Función para seleccionar el archivo de video
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.y4m")])
    if file_path:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, file_path)

# Función para medir el ancho de banda
def measure_bandwidth(ip):
    result = subprocess.run(['iperf3', '-c', ip, '-t', '5', '-f', 'm'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if "receiver" in result.stdout:
      #return float(result.stdout.split("sender")[1].split("MBytes")[1].split("Mbits/sec")[0].strip())
      return float(result.stdout.split("sender")[1].split("Bytes")[1].split("Mbits/sec")[0].strip())
    return None

# Función para ajustar el bitrate
def adjust_bitrate(bandwidth):
    if selected_category == "Noticias":
        if bandwidth > 5:
            return "3457k"
        elif bandwidth > 4:
            return "2580k"
        elif bandwidth > 3:
            return "1703k"
        else:
            return "500k"
    elif selected_category == "Entretenimiento":
        if bandwidth > 5.5:
            return "3712k"
        elif bandwidth > 4.5:
            return "2770k"
        elif bandwidth > 3:
            return "1829k"
        else:
            return "500k"
    elif selected_category == "Tiempo Real":
        if bandwidth > 5.5:
            return "4164k"
        elif bandwidth > 4:
            return "3107k"
        elif bandwidth > 3:
            return "2051k"
        else:
            return "500k"
    else:
        return "500k"
        

# Función para iniciar la transmisión de video
def start_stream():
    receiver_ip = entry_ip.get()
    input_file = entry_file.get()
    
    if not receiver_ip or not input_file:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    
    def stream():
        nonlocal receiver_ip, input_file
        process = None
        initial_bitrate = "70k"  # Bitrate inicial de 70 Kbps

        while True:
            if process:
                bandwidth = measure_bandwidth(receiver_ip)
                
                if bandwidth is None:
                    print("No se pudo medir el ancho de banda. Intentando de nuevo...")
                    time.sleep(5)
                    continue
                
                new_bitrate = adjust_bitrate(bandwidth)
                label_bandwidth.config(text=f"Ancho de banda: {bandwidth} Mbps")
                label_bitrate.config(text=f"Tasa de codificación: {new_bitrate}")
                print(f"Ancho de banda: {bandwidth} Mbps, ajustando bitrate a {new_bitrate}")

                process.terminate()
            else:
                new_bitrate = initial_bitrate
                label_bandwidth.config(text="Ancho de banda: N/A")
                label_bitrate.config(text=f"Tasa de codificación: {new_bitrate}")
                print(f"Iniciando transmisión con bitrate de {new_bitrate}")
            
            command = [
                'ffmpeg', '-re', '-i', input_file, '-c:v', 'libx264', '-b:v', new_bitrate, '-f', 'mpegts',
                f"udp://{receiver_ip}:1234?pkt_size=1316&fifo_size=5000000"
            ]
            process = subprocess.Popen(command)
            
            time.sleep(5)
    
    threading.Thread(target=stream, daemon=True).start()

# Función para iniciar la transmisión de video en modo Demo
def start_demo():
    global streaming_process
    receiver_ip = entry_ip.get()
    input_file = entry_file.get()
    
    if not receiver_ip or not input_file:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    
    def demo_stream():
        nonlocal receiver_ip, input_file
        bitrate_sequence = [("10k", 15), ("100k", 15), ("1000k", None)]
        
        for bitrate, duration in bitrate_sequence:
            label_bitrate.config(text=f"Tasa de codificación: {bitrate}")
            print(f"Codificando a {bitrate}")
            
            command = [
                'ffmpeg', '-re', '-i', input_file,'-c:v', 'libx264', '-b:v', bitrate, '-f', 'mpegts',
                f"udp://{receiver_ip}:1234?pkt_size=1316&fifo_size=5000000"
            ]
            streaming_process = subprocess.Popen(command)
            
            if duration:
                time.sleep(duration)
                streaming_process.terminate()
                streaming_process.wait()
            else:
                streaming_process.wait()
    
    demo_thread = threading.Thread(target=demo_stream, daemon=True)
    demo_thread.start()


# Configurar la interfaz gráfica
root = tk.Tk()
root.title("Sistema de control de Video Adaptativo")
root.configure(bg='#3F4A99') 

frame = tk.Frame(root, padx=10, pady=10, bg='#ADD8E6')
frame.pack(padx=10, pady=10)

# Cargar el logo
try:
    logo_image = Image.open("/home/marlon/tesis/Videosy4m/logou.png")
    logo_photo = ImageTk.PhotoImage(logo_image)

    # Mostrar el logo
    logo_label = tk.Label(frame, image=logo_photo, bg='#3F4A99')
    logo_label.grid(row=0, column=0, columnspan=3, sticky="w")
except Exception as e:
    print(f"Error al cargar el logo: {e}")

label_ip = tk.Label(frame, text="IP del Cliente:", bg='#ADD8E6')
label_ip.grid(row=1, column=0, sticky="e")

entry_ip = tk.Entry(frame, width=20)
entry_ip.grid(row=1, column=1)

label_file = tk.Label(frame, text="Archivo de Video:", bg='#ADD8E6')
label_file.grid(row=2, column=0, sticky="e")

entry_file = tk.Entry(frame, width=20)
entry_file.grid(row=2, column=1)

news_button = tk.Button(frame, text="Noticias", command=lambda: select_category("Noticias"))
news_button.grid(row=3, column=0, padx=5)

entertainment_button = tk.Button(frame, text="Entretenimiento", command=lambda: select_category("Entretenimiento"))
entertainment_button.grid(row=3, column=1, padx=5)

realtime_button = tk.Button(frame, text="Tiempo Real", command=lambda: select_category("Tiempo Real"))
realtime_button.grid(row=3, column=2, padx=5)

start_button = tk.Button(frame, text="Iniciar Transmisión", command=start_stream)
start_button.grid(row=4, columnspan=3, pady=10)

label_bandwidth = tk.Label(frame, text="Ancho de banda: N/A", bg='#ADD8E6')
label_bandwidth.grid(row=5, columnspan=3)

label_bitrate = tk.Label(frame, text="Tasa de codificación: N/A", bg='#ADD8E6')
label_bitrate.grid(row=6, columnspan=3)

demo_button = tk.Button(frame, text="Demo", command=start_demo)
demo_button.grid(row=7, columnspan=3, pady=10)

root.mainloop()
