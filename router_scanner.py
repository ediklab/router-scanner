#!/usr/bin/env python3
"""
Router External Scanner - DEMO EDUCATIVA
Escanea TU IP pública buscando puertos expuestos

Uso: python3 router_exposure_scanner.py <IP>
     python3 router_exposure_scanner.py --demo
"""

import socket
import sys
import time

# Colores ANSI
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
GRAY = '\033[90m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Puertos críticos en routers
CRITICAL_PORTS = {
    22: "SSH",
    23: "Telnet",
    80: "HTTP",
    443: "HTTPS",
    7547: "TR-069",
    8080: "HTTP-alt"
}

def print_banner():
    """Banner minimalista"""
    print(f"{CYAN}Router Exposure Scanner{RESET}")
    print(f"{GRAY}Checking critical ports...{RESET}\n")

def scan_port(ip, port, timeout=1.5):
    """Escanea un puerto TCP"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        time.sleep(0.1)  # Delay realista
        return result == 0
    except:
        return False

def scan_demo_mode(port):
    """Demo: simula puertos típicamente abiertos en routers"""
    # SSH, HTTP, TR-069 (típico en Movistar/Vodafone/Orange)
    typically_open = [22, 80, 7547]
    # Delay realista por puerto (2-3 segundos cada uno)
    time.sleep(2.5)
    return port in typically_open

def scan_target(ip, demo=False):
    """Escanea puertos críticos"""
    print(f"Target: {BOLD}{ip}{RESET}")
    print(f"Ports: {', '.join(map(str, CRITICAL_PORTS.keys()))}\n")

    vulnerable = []

    for port, service in CRITICAL_PORTS.items():
        # Escanear
        if demo:
            is_open = scan_demo_mode(port)
        else:
            is_open = scan_port(ip, port)

        # Output compacto
        if is_open:
            print(f"{RED}[OPEN]{RESET}  {port:5}/tcp  {service}")
            vulnerable.append((port, service))
        else:
            print(f"{GRAY}[----]{RESET}  {port:5}/tcp  {service}")

    return vulnerable

def show_summary(vulnerable):
    """Resumen final compacto"""
    print(f"\n{CYAN}─────────────────────────────────────────{RESET}")

    if not vulnerable:
        print(f"{GREEN}✓ No critical ports exposed{RESET}")
        print(f"{GRAY}Router appears secure{RESET}")
    else:
        print(f"{RED}✗ {len(vulnerable)} port(s) exposed:{RESET}")
        for port, service in vulnerable:
            print(f"  {RED}•{RESET} {port}/tcp ({service})")

        print(f"\n{YELLOW}Risks:{RESET}")
        if 22 in [p for p, _ in vulnerable]:
            print(f"  {RED}•{RESET} SSH: Config changes, DNS hijacking")
        if 80 in [p for p, _ in vulnerable]:
            print(f"  {RED}•{RESET} HTTP: Admin panel exposed")
        if 7547 in [p for p, _ in vulnerable]:
            print(f"  {RED}•{RESET} TR-069: ISP protocol (botnet target)")

        print(f"\n{CYAN}Fix:{RESET} Router settings → Disable WAN access")

    print(f"{CYAN}─────────────────────────────────────────{RESET}\n")

def main():
    """Main function"""
    # Verificar argumentos
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <IP> | --demo")
        print(f"\nExample:")
        print(f"  {sys.argv[0]} 203.0.113.42")
        print(f"  {sys.argv[0]} --demo")
        sys.exit(1)

    # Modo demo o IP real
    demo_mode = False
    if sys.argv[1] == "--demo":
        target_ip = "203.0.113.42"  # TEST-NET-3
        demo_mode = True
        print(f"{YELLOW}[!] DEMO MODE{RESET}\n")
    else:
        target_ip = sys.argv[1]

    # Banner
    print_banner()

    # Escanear
    vulnerable = scan_target(target_ip, demo=demo_mode)

    # Resumen
    show_summary(vulnerable)

    # Footer
    print(f"{GRAY}github.com/3diklab{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[✗] Interrupted{RESET}\n")
        sys.exit(0)
