import nmap  # type: ignore
import argparse
import concurrent.futures

# Colores ANSI
RED = "\033[91m"
RESET = "\033[0m"

def banner():
    print(f"{RED}  _    _     _    __  __          ")
    print(" | |  | |   | |  |  \/  |         ")
    print(" | |__| |_ _| | _| \  / | ___ _ __ ")
    print(" |  __  / _` | |/ / |\/| |/ _ \ '__|")
    print(" | |  | | (_| |   <| |  | |  __/ |   ")
    print(" |_|  |_|\__,_|_|\_\_|  |_|\\___|_|   ")
    print("                                   {RESET}\n")

def scan_host(scanner, host):
    scanner.scan(hosts=host, arguments="-sn")
    result = []
    if 'mac' in scanner[host]['addresses']:
        ipv4 = scanner[host]["addresses"].get('ipv4', 'N/A')
        mac = scanner[host]["addresses"]["mac"]
        vendor = scanner[host]["vendor"].get(mac, "N/A")
        result = [ipv4, mac, vendor]
    return result

def mac_ip(ip_range, threads, output_file):
    scanner = nmap.PortScanner()
    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        future_to_host = {executor.submit(scan_host, scanner, host): host for host in ip_range.split(',')}
        for future in concurrent.futures.as_completed(future_to_host):
            result = future.result()
            if result:
                results.append(result)
                print(f"IPV4: {result[0]}")
                print(f"MAC: {result[1]}")
                print(f"VENDOR: {result[2]}")
                print("\n")

    if output_file:
        with open(output_file, 'w') as file:
            for result in results:
                file.write(f"IPV4: {result[0]}\n")
                file.write(f"MAC: {result[1]}\n")
                file.write(f"VENDOR: {result[2]}\n")
                file.write("\n")

def main():
    parser = argparse.ArgumentParser(description="IP and MAC Address Scanner")
    parser.add_argument("-r", "--range", type=str, help="IP range to scan (e.g., 192.168.1.0/24)", required=True)
    parser.add_argument("-t", "--threads", type=int, help="Number of threads to use for scanning", default=4)
    parser.add_argument("-o", "--output", type=str, help="Output file to save results", default=None)
    
    args = parser.parse_args()
    
    banner()
    mac_ip(args.range, args.threads, args.output)

if __name__ == "__main__":
    main()
