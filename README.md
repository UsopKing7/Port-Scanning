# Escáner de Puertos Abiertos

Este script en Python utiliza la librería `nmap` para realizar un escaneo de puertos abiertos en una IP específica. El script se enfoca en mostrar solo los puertos que están abiertos y su estado, con una salida visual mejorada utilizando colores para facilitar la lectura.

## Características

- Escaneo de puertos abiertos en una IP dada.
- Muestra información sobre los puertos y su estado (`open`).
- Salida de consola coloreada para facilitar la lectura.
- Utiliza la librería `nmap` para realizar el escaneo de red.

## Requisitos

- Python 3.6 o superior.
- Paquetes adicionales:
  - `nmap`
  - `colorama`
  - `pip`

## Instalación
clonamos el repositorio

```bash
git clone https://github.com/UsopKing7/Port-Scanning.git
```

entramos al archivo clonado

```bash
cd Port-Scanning
```

le damos permisos de ejecucion

```bash
chmod +x openports.py
```

## Instalacion de los requisitos
instalacion de nmap
```bash
# para debian
sudo apt install nmap
```
```bash
# para arch
yay -S nmap
```

instalacion de pip
```bash
# para debian
sudo apt install python3-pip
pip --version
```
```bash
# para arch
sudo pacman -S python-pip
pip --version
```
instalacion de python-nmap con pip
```bash
pip install python-nmap
```
instalacion de colorama con pip
```bash
pip install colorama
```
## Uso
```bash
python3 openports.py
#salida en consla
Por favor ingresa la IP que deseas escanear: <IP>
```

## Salida
```bash
 _   _                 _  ___             
| | | |___  ___  _ __ | |/ (_)_ __   __ _ 
| | | / __|/ _ \| '_ \| ' /| | '_ \ / _` |
| |_| \__ \ (_) | |_) | . \| | | | | (_| |
 \___/|___/\___/| .__/|_|\_\_|_| |_|\__, |
                |_|                 |___/ 
 Estado:     up
 IP: 8.8.8.8 ()
 Protocolo:  tcp
  Puerto:    53   Estado:   open
  Puerto:    443   Estado:   open
```
## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, puedes seguir estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu cambio 
3. Realiza tus cambios y haz commit de ellos 
4. Sube tus cambios a tu fork 
5. Abre un pull request desde tu fork hacia el repositorio original.

## Soporte

Si tienes problemas al utilizar este script o tienes preguntas, no dudes en abrir un **issue** en el repositorio. Nos esforzamos por responder lo antes posible y ayudar a resolver cualquier inconveniente.

## Agradecimientos

Gracias por utilizar este proyecto. Si lo encuentras útil, ¡no dudes en dejar una estrella ⭐ en GitHub!
