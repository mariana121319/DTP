# Informe de Seguridad (Enfoque Defensivo): Riesgo por Negociación DTP / Trunk no autorizado

**Fecha:** 2026-02-28 02:55:59  
**Autor:** mariana121319  
**Entorno:** Laboratorio (PNetLab / similar)  
**Dominio/LAN de referencia:** `mariana.local` (si aplica)

## 1) Objetivo (defensivo)
Documentar el riesgo de configuraciones inseguras de negociación de trunk (DTP), el diseño de VLANs/IP del laboratorio, y controles de mitigación, verificación y evidencias.

## 2) Topología (rellenar puertos)
- R1 (router-on-a-stick): subinterfaces en `f0/0`
- SW1 (L2): VLAN 10/20/30
- Trunk: R1 f0/0 ↔ SW1 ________
- Puertos access:
  - PC1: SW1 ________
  - PC2: SW1 ________
  - Server: SW1 ________
  - Admin PC: SW1 ________

## 3) VLANs y direccionamiento IP
### VLAN 10
- Red: 12.0.10.0/24
- Gateway: 12.0.10.1 (R1 f0/0.10)
- DHCP: 12.0.10.11–12.0.10.254
- Hosts: PC1 12.0.10.11, PC2 12.0.10.12

### VLAN 20
- Red: 12.0.20.0/24
- Gateway: 12.0.20.1 (R1 f0/0.20)
- DHCP: 12.0.20.11–12.0.20.254
- Host: Server 12.0.20.11

### VLAN 30
- Red: 12.0.30.0/24
- Gateway: 12.0.30.1 (R1 f0/0.30)
- DHCP: 12.0.30.11–12.0.30.254
- Host: Admin PC 12.0.30.11

## 4) Evidencias (capturas)
- Estado de trunks (antes/después): ____________
- VLANs y puertos: ____________
- Endurecimiento aplicado: ____________

## 5) Mitigación recomendada
- Puertos de usuario en modo access fijo y sin negociación.
- Trunk: permitir solo VLAN 10/20/30.
- VLAN nativa dedicada (no VLAN 1) y control de tráfico no etiquetado.
- Port-security / 802.1X (si aplica).
- DHCP Snooping / DAI / IP Source Guard (si aplica).
- ACLs inter-VLAN según necesidad (usuarios vs admin).

## 6) Verificación
- Solo el enlace SW1–R1 está en trunk.
- Los hosts reciben IP por DHCP en su VLAN correcta.
- Inter-VLAN routing funciona según política.

## 7) Espacio para adjuntar script (.py)
- Archivo: Dtp.py
- Ruta: Dtp.py
- Versión/hash: ____________