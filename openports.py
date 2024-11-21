import nmap
from colorama import Fore, init

init(autoreset=True)

def puertos_abiertos(ip):
    print(Fore.GREEN + r" _   _                 _  ___             ")
    print(Fore.GREEN + r"| | | |___  ___  _ __ | |/ (_)_ __   __ _ ")
    print(Fore.GREEN + r"| | | / __|/ _ \| '_ \| ' /| | '_ \ / _` |")
    print(Fore.GREEN + r"| |_| \__ \ (_) | |_) | . \| | | | | (_| |")
    print(Fore.GREEN + r" \___/|___/\___/| .__/|_|\_\_|_| |_|\__, |")
    print(Fore.GREEN + r"                |_|                 |___/ ")

    scanner = nmap.PortScanner()
    scanner.scan(ip, arguments="-Pn -n --open")

    if not scanner.all_hosts():
        print(Fore.RED + "No se encontraron hosts activos.")
        return

    for ip in scanner.all_hosts():
        print(Fore.YELLOW + f" Estado:     {scanner[ip].state()}")
        estado = scanner[ip].state()

        if estado == 'up':
            print(Fore.YELLOW + f" IP: {ip} ({scanner[ip].hostname()})")
            for proto in scanner[ip].all_protocols():
                print(Fore.CYAN + f" Protocolo:  {proto}")
                lport = scanner[ip][proto].keys()
                
                for port in sorted(lport):
                    if scanner[ip][proto][port]['state'] == 'open':
                        print(Fore.GREEN + f"  Puerto:    {port}   Estado:   {scanner[ip][proto][port]['state']}")
        else:
            print(Fore.RED + " La máquina está apagada")
            return

ip = input(Fore.YELLOW + "Por favor ingresa la IP que deseas escanear: ")
puertos_abiertos(ip)
