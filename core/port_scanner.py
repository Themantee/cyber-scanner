# import socket
# from core.banner import grab_banner
# from colorama import Fore, Style

# def scan_ports(target_ip, ports):
#     open_ports = []

#     for port in ports:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.settimeout(1)

#         result = sock.connect_ex((target_ip, port))

#         if result == 0:
#             print(f"{Fore.GREEN}[OPEN]{Style.RESET_ALL} Port {port}")
#             banner = grab_banner(target_ip, port)
#             if banner:
#                 print(f"       Banner: {banner}")
#             open_ports.append(port)
#         else:
#             print(f"{Fore.RED}[CLOSED]{Style.RESET_ALL} Port {port}")

#         sock.close()

#     return open_ports






import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from core.banner import grab_banner
from colorama import Fore, Style

def scan_single_port(target_ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target_ip, port))

    if result == 0:
        banner = grab_banner(target_ip, port)
        return (port, True, banner)

    sock.close()
    return (port, False, None)

def scan_ports(target_ip, ports, threads=50):
    open_ports = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {
            executor.submit(scan_single_port, target_ip, port): port
            for port in ports
        }

        for future in as_completed(futures):
            port, is_open, banner = future.result()

            if is_open:
                print(f"{Fore.GREEN}[OPEN]{Style.RESET_ALL} Port {port}")
                if banner:
                    print(f"       Banner: {banner}")
                open_ports.append(port)
            else:
                print(f"{Fore.RED}[CLOSED]{Style.RESET_ALL} Port {port}")

    return sorted(open_ports)
