import nmap

def mac_ip(ip_range):
    scanner = nmap.PortScanner()

    scanner.scan(hosts = ip_range, arguments = "-sn")

    for host in scanner.all_hosts():
        if 'mac' in host[host]['addresses']:
            ipv4 = scanner[host]["addresses"]["ipv4"]
            ipv6 = scanner[host]["addresses"]["ipv6"]
            mc = scanner[host]["addresses"]["mac"]

            print(f"IPV4: {ipv4} ")
            print(f"IPV6: {ipv6}")
            print(f"MAC: {mc} ")


mac_ip(ip_range = "192.168.1.0/24") 