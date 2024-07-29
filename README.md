Escáner de Puertos y Detección de IPs y MACs
Este proyecto permite escanear puertos en una red y detectar direcciones IP y MAC de los dispositivos conectados.

Descripción
El escáner de puertos y detector de IPs y MACs es una herramienta que realiza un escaneo de red para identificar dispositivos activos y sus puertos abiertos. Utiliza Python y la librería Scapy para la manipulación de paquetes de red y el análisis del tráfico.

Requisitos
  -Python 3.x
  -Librerías de Python:
  -scapy
  -nmap
  -requests
  
Instalación
Clona este repositorio:
git clone https://github.com/UsopKing7/Port-Scanning.git

Crea un entorno virtual
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`

Instala las dependencias:
pip install scapy python-nmap requests

USO: 
Ejecuta el script principal:
python nombre_del_archivo.py

Contribuir
Si deseas contribuir a este proyecto, por favor sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
Realiza tus cambios y haz commits (git commit -am 'Agrega nueva característica').
Sube tus cambios a tu repositorio (git push origin feature/nueva-caracteristica).
Crea un Pull Request.
