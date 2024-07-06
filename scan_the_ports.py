#scanneo de puertos abiertos

import nmap

scanner = nmap.PortScanner()
scanner.scan('8.8.8.8', '1-1024', '-sV -sS -A -sC -O')

for host in scanner.all_hosts():
    print("host", host)
    for proto in scanner[host].all_protocols():
        lport = scanner[host][proto].keys()
        for port in lport:
            print("     port: ", port)
            print("     name: ", scanner[host][proto][port]['name'])
            print("     State: ", scanner[host][proto][port]['state'])
            print("     versions: ", scanner[host][proto][port]['version'])
            if 'product' in scanner[host][proto][port]:
                print("     product:", scanner[host][proto][port]['product'])
            if 'extraInfo' in scanner[host][proto][port]:
                print("     extraInfo: "[host][proto][port]['extraInfo'])