import subprocess
import re
import time
import argparse
import sys
from datetime import datetime

def check_interface(interface=None):
    result = subprocess.run(["hciconfig"], capture_output=True, text=True)
    interfaces = re.findall(r'(hci\d+):', result.stdout)
    if interface:
        if interface not in interfaces:
            print(f"[!] Interface {interface} não encontrada.")
            sys.exit(1)
        return interface
    return interfaces[0] if interfaces else None

def enable_interface(interface):
    subprocess.run(["hciconfig", interface, "up"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def sniff_packets(interface, mac_filter=None, output_file="bluesniff_log.txt"):
    print(f"[+] Iniciando captura com interface {interface}")
    print(f"[+] Log: {output_file}")
    if mac_filter:
        print(f"[+] Filtro MAC ativo: {mac_filter}")
    else:
        print("[+] Filtro MAC desativado")
    print("[*] Capturando pacotes... pressione Ctrl+C para parar.\n")

    try:
        with open(output_file, "a") as log:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"\n[Início da captura: {timestamp}]\n")
            process = subprocess.Popen(["hcidump", "-i", interface, "-X"], stdout=subprocess.PIPE, text=True)

            for line in process.stdout:
                if mac_filter:
                    if mac_filter.lower() in line.lower():
                        log.write(line)
                        print(f"[{timestamp}] {line.strip()}")
                else:
                    log.write(line)
                    print(f"[{timestamp}] {line.strip()}")
    except KeyboardInterrupt:
        print("\n[!] Captura interrompida pelo usuário.")
    except Exception as e:
        print(f"[ERRO] {e}")
    finally:
        print("[+] Encerrando captura.")

def main():
    parser = argparse.ArgumentParser(
        description="PyBlueSniff - Sniffer Bluetooth estilo Nmap",
        epilog="Exemplo: sudo python3 pybluesniff.py --filter 00:11:22:33:44:55 --outfile log.txt"
    )
    parser.add_argument('--filter', help="Endereço MAC para filtrar (opcional)")
    parser.add_argument('--outfile', default="bluesniff_log.txt", help="Arquivo de saída (padrão: bluesniff_log.txt)")
    parser.add_argument('--interface', help="Interface Bluetooth (ex: hci0)")
    args = parser.parse_args()

    interface = check_interface(args.interface)
    if not interface:
        print("[ERRO] Nenhuma interface Bluetooth encontrada.")
        sys.exit(1)

    enable_interface(interface)
    sniff_packets(interface, mac_filter=args.filter, output_file=args.outfile)

if __name__ == "__main__":
    if not sys.platform.startswith("linux"):
        print("[!] Este script requer Linux com ferramentas hcitool/hcidump.")
        sys.exit(1)
    main()
