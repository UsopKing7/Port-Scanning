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
