import nmap

def puertos_abiertos():
    print(" _   _                 _  ___             ")
    print("| | | |___  ___  _ __ | |/ (_)_ __   __ _ ")
    print("| | | / __|/ _ \| '_ \| ' /| | '_ \ / _` |")
    print("| |_| \__ \ (_) | |_) | . \| | | | | (_| |")
    print(" \___/|___/\___/| .__/|_|\_\_|_| |_|\__, |")
    print("                |_|                 |___/ ")

    scanner = nmap.PortScanner()
    scanner.scan("192.168.1.12", "1-800", arguments="-sV -O -sC -sS -T4 -Pn")

    if not scanner.all_hosts():
        print("No se encontraron hosts activos.")
        return

    for ip in scanner.all_hosts():
        print(f" Estado:     {scanner[ip].state()}")
        estado = scanner[ip].state()

        if estado == 'up':
            print(f" IP: {ip} ({scanner[ip].hostname()})")
            for proto in scanner[ip].all_protocols():
                print(f" Protocolo:  {proto}")
                lport = scanner[ip][proto].keys()
                
                for port in sorted(lport):
                    print(f"  Puerto:    {port}   Estado:   {scanner[ip][proto][port]['state']}")                       
                    producto = scanner[ip][proto][port].get('product', 'Desconocido')
                    version = scanner[ip][proto][port].get('versions', 'Desconocido')
                    name = scanner[ip][proto][port].get('name', 'Desconocido')

                    print(f"  Producto:   {producto}")
                    print(f"  Version:    {version}")
                    print(f"  Nombre:     {name}")
        else:
            print(" La máquina está apagada")
            exit()

puertos_abiertos()