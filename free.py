import sys
import os
import re
import base64
import argparse

# Scapy Setup (Android/Termux compatibility)
sys.platform = "linux"
from scapy.all import *
if hasattr(sys, 'getandroidapilevel'):
    del sys.getandroidapilevel

from colorama import Fore, Style, init

init(autoreset=True)

class SNISniper:
    def __init__(self, interface="rmnet_data0"):
        self.interface = interface
        # Watermark signature (Obfuscated to prevent easy removal)
        self._sig = base64.b64decode(b'aHR0cDovL3QubWUvY2lwaGVyLWF0dGFja3M=').decode()
	
        if os.name == 'posix' and os.geteuid() != 0:
            print(Fore.RED + "ERROR: Root privileges required.")
            sys.exit(1)

        self._print_banner()

    def _print_banner(self):
        print(Fore.CYAN + Style.BRIGHT + "="*50)
        print(Fore.CYAN + Style.BRIGHT + "       SNI & Payload Bug Sniper (Radar)           ")
        print(Fore.CYAN + Style.BRIGHT + "="*50)
        print(Fore.YELLOW + f"  Interface: {self.interface}")
        print(Fore.BLUE + Style.BRIGHT + f"  Channel: {self._sig}")
        print(Fore.GREEN + "  Listening started! Please start the Injector...\n")

    def _process_packet(self, packet):
        # Anti-tamper check: silently drop packets if watermark is modified
        if len(self._sig) < 20: 
            return

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            
            # 1. Cleartext HTTP/CONNECT check
            text_payload = payload.decode('utf-8', errors='ignore')
            if "HTTP/" in text_payload or "CONNECT " in text_payload or "Host: " in text_payload:
                # Filter out standard telemetry noise
                if "gstatic.com" not in text_payload and "google.com" not in text_payload:
                    print(Fore.GREEN + Style.BRIGHT + "[+] Cleartext HTTP/CONNECT Payload Detected:")
                    print(Fore.WHITE + text_payload.strip()[:400])
                    print(Fore.CYAN + "="*50)
                    return

            # 2. SSL/TLS SNI check (0x16 indicates TLS handshake)
            if payload[0] == 0x16:
                # Extract potential domains
                domains = re.findall(rb'[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', payload)
                
                for d in set(domains):
                    domain_str = d.decode('utf-8', errors='ignore')
                    
                    # Ignore common background domains
                    if "gstatic" not in domain_str and "google" not in domain_str and "android" not in domain_str:
                        print(Fore.MAGENTA + Style.BRIGHT + f"[!] Obfuscated SNI/Host Detected (TLS):")
                        print(Fore.YELLOW + Style.BRIGHT + f" --->  {domain_str}  <---")
                        print(Fore.CYAN + "="*50)

    def start_sniffing(self):
        try:
            sniff(
                iface=self.interface,
                prn=self._process_packet,
                store=0
            )
        except Exception as e:
            print(Fore.RED + f"\n[!] Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-i", "--interface", default="rmnet_data0", help="Network interface to sniff on")
    args = parser.parse_args()

    sniffer = SNISniper(interface=args.interface)	
    try:
        sniffer.start_sniffing()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[!] Operation aborted by -user.")
-
