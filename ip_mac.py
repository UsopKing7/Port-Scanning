import nmap # type: ignore

def mac_ip(ip_range):
    
    print(" _   _                 _  ___             ")
    print("| | | |___  ___  _ __ | |/ (_)_ __   __ _ ")
    print("| | | / __|/ _ \| '_ \| ' /| | '_ \ / _` |")
    print("| |_| \__ \ (_) | |_) | . \| | | | | (_| |")
    print(" \___/|___/\___/| .__/|_|\_\_|_| |_|\__, |")
    print("                |_|                 |___/  \n")
    
    scanner = nmap.PortScanner()

    scanner.scan(hosts = ip_range, arguments = "-sn")

    for host in scanner.all_hosts():
        if 'mac' in scanner[host]['addresses']:
            ipv4 = scanner[host]["addresses"].get('ipv4', 'N/A')
            mc = scanner[host]["addresses"]["mac"]
            vendor = scanner[host]["vendor"].get(mc, "N/A")

            print(f"IPV4: {ipv4} ")
            print(f"MAC: {mc} ")
            print(f"VENDOR: {vendor}")
            print("\n")

mac_ip(ip_range = "192.168.1.0/24") 
