import os
import re
import base64
import argparse

from scapy.all import sniff, Raw, get_if_list
from colorama import Fore, Style, init

init(autoreset=True)


class SNISniper:
    def __init__(self, interface=None):
        self.interface = interface or self._auto_detect_interface()

        # Safe watermark decoding
        try:
            self._sig = base64.b64decode(
                b'aHR0cDovL3QubWUvY2lwaGVyLWF0dGFja3M='
            ).decode()
        except Exception:
            self._sig = "unknown"

        self._check_environment()
        self._print_banner()

    # 🔍 Auto-detect working interface
    def _auto_detect_interface(self):
        interfaces = get_if_list()

        for iface in interfaces:
            if "wlan" in iface:
                return iface

        return interfaces[0] if interfaces else None

    # ⚠️ Environment checks
    def _check_environment(self):
        if not self.interface:
            print(Fore.RED + "No network interface found.")
            exit(1)

        if os.geteuid() != 0:
            print(Fore.YELLOW + "[!] Warning: Not running as root.")
            print(Fore.YELLOW + "    Sniffing may fail or be limited.\n")

    def _print_banner(self):
        print(Fore.CYAN + "=" * 50)
        print(Fore.CYAN + "   SNI & Payload Sniper (Termux Stable)")
        print(Fore.CYAN + "=" * 50)
        print(Fore.YELLOW + f"Interface: {self.interface}")
        print(Fore.BLUE + f"Channel: {self._sig}")
        print(Fore.GREEN + "Sniffing started...\n")

    # 🔥 Safe packet processing
    def _process_packet(self, packet):
        try:
            if not packet.haslayer(Raw):
                return

            payload = packet[Raw].load

            if not payload or len(payload) < 5:
                return

            # ---- HTTP detection ----
            text = payload.decode(errors="ignore")

            if any(x in text for x in ["HTTP/", "CONNECT", "Host:"]):
                if not any(bad in text for bad in ["google", "gstatic", "android"]):
                    print(Fore.GREEN + "[HTTP DETECTED]")
                    print(text[:300])
                    print("-" * 50)
                    return

            # ---- TLS SNI detection ----
            if payload[0] == 0x16:  # TLS handshake
                domains = re.findall(rb'[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', payload)

                for d in set(domains):
                    try:
                        domain = d.decode()
                        if not any(x in domain for x in ["google", "gstatic", "android"]):
                            print(Fore.MAGENTA + "[SNI DETECTED]")
                            print(Fore.YELLOW + domain)
                            print("-" * 50)
                    except:
                        continue

        except Exception:
            # Prevent crash from bad packets
            pass

    # 🚀 Start sniffing safely
    def start(self):
        try:
            sniff(
                iface=self.interface,
                prn=self._process_packet,
                store=False,
                filter="tcp",
            )
        except PermissionError:
            print(Fore.RED + "Permission denied (حتاج root).")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", help="Network interface")
    args = parser.parse_args()

    sniper = SNISniper(interface=args.interface)
    sniper.start()
