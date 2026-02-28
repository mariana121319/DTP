# Informe (Defensivo): Riesgo por Negociación DTP / Trunk no autorizado

**Fecha:** 2026-02-28 04:17:35  
**Autor:** mariana121319  
**Entorno:** PNetLab (laboratorio)  
**Dominio/LAN (opcional):** `mariana.local`

---

## 1) Objetivo del laboratorio (enfoque defensivo)

- Documentar el **riesgo** de permitir **negociación dinámica de trunk** en puertos que deberían ser de acceso.
- Describir la **topología**, **VLANs** y **direccionamiento IP**.
- Incluir **evidencias** (capturas) y un checklist de **verificación**.
- Proponer **medidas de mitigación** y buenas prácticas de hardening.

> Este README es **defensivo**: describe prevención/detección/verificación, no una guía operativa de explotación.

---

## 2) Topología (completar con tus puertos)

### Dispositivos
- **R1**: Router-on-a-stick (subinterfaces en `f0/0`)
- **SW1**: Switch L2 (VLAN 10/20/30)
- **Hosts**
  - VLAN 10: PC1, PC2
  - VLAN 20: Server
  - VLAN 30: Admin PC

### Interfaces / Puertos (rellenar)
- **Trunk**: `R1 f0/0` ↔ `SW1 __________`
- **Access ports**
  - PC1 ↔ `SW1 __________`
  - PC2 ↔ `SW1 __________`
  - Server ↔ `SW1 __________`
  - Admin PC ↔ `SW1 __________`

**Captura/diagrama de topología:**  
(PEGA AQUÍ LA IMAGEN)

---

## 3) VLANs y direccionamiento IP (definido)

### 🌐 VLAN 10
- **Red:** `12.0.10.0/24`
- **Gateway (R1 f0/0.10):** `12.0.10.1`
- **Rango DHCP:** `12.0.10.11 – 12.0.10.254`
- **Ejemplos de hosts:**
  - PC1 → `12.0.10.11`
  - PC2 → `12.0.10.12`

### 🌐 VLAN 20
- **Red:** `12.0.20.0/24`
- **Gateway (R1 f0/0.20):** `12.0.20.1`
- **Rango DHCP:** `12.0.20.11 – 12.0.20.254`
- **Ejemplo:**
  - Server → `12.0.20.11`

### 🌐 VLAN 30
- **Red:** `12.0.30.0/24`
- **Gateway (R1 f0/0.30):** `12.0.30.1`
- **Rango DHCP:** `12.0.30.11 – 12.0.30.254`
- **Ejemplo:**
  - Admin PC → `12.0.30.11`

---

## 4) Evidencias (capturas)

- [ ] Estado de trunks (antes/después): ______________________
- [ ] VLANs y puertos asignados: _____________________________
- [ ] Config final de puertos de usuario (access): ___________
- [ ] (Opcional) Logs/Syslog: ________________________________

---

## 5) Riesgo (resumen)

Si un puerto de usuario permite negociación de trunk, se puede degradar la segmentación por VLAN y aumentar el riesgo de exposición de tráfico y movimiento lateral, dependiendo de la configuración del entorno.

---

## 6) Medidas de mitigación (recomendadas)

- Puertos de usuario en **access fijo**, con VLAN explícita y sin negociación.
- Enlace SW1–R1 como trunk **controlado** y con **VLANs permitidas mínimas** (solo 10/20/30).
- VLAN nativa dedicada y documentada (evitar VLAN 1 si es posible).
- Port-security / 802.1X (si aplica).
- DHCP Snooping + DAI + IP Source Guard (si aplica).
- ACLs inter-VLAN según rol (usuarios vs admin) si necesitas segmentación adicional.

---

## 7) Verificación (checklist)

- [ ] Solo el enlace SW1–R1 está en trunk.
- [ ] Los puertos de hosts están en access y en su VLAN correcta.
- [ ] El trunk permite únicamente VLAN 10/20/30.
- [ ] DHCP entrega IPs correctas:
  - VLAN10 → 12.0.10.0/24
  - VLAN20 → 12.0.20.0/24
  - VLAN30 → 12.0.30.0/24
- [ ] Inter-VLAN routing funciona según la política definida.

---

## 8) Parámetros del laboratorio (rellenar)

- Trunk SW1 (puerto): __________
- VLAN nativa: __________
- DHCP lo provee: (R1/Server) __________
- DNS (si aplica): __________
- Dominio (si aplica): mariana.local

---

## 9) Espacio para subir un .py

- **Archivo:** `Dtp.py`
- **Ruta:** `./Dtp.py`
- **Notas:** (descripción conceptual, sin instrucciones operativas) ____________________