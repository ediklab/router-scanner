# Router Security Scanner

Script educativo para verificar puertos expuestos en tu router desde internet.

## ¿Qué hace?

Escanea tu IP pública buscando puertos críticos que podrían estar expuestos:
- **22** (SSH) - Acceso remoto
- **23** (Telnet) - Protocolo inseguro
- **80** (HTTP) - Panel de administración
- **443** (HTTPS) - Panel seguro
- **7547** (TR-069) - Protocolo de gestión ISP
- **8080** (HTTP-alt) - Puerto alternativo

## Instalación

```bash
git clone https://github.com/ediklab/router-scanner.git
cd router-scanner/
chmod +x router_scanner.py
```

## Uso

1. Obtén tu IP pública:
```bash
curl ifconfig.me
```

2. Escanea esa IP:
```bash
python3 router_scanner.py TU_IP_AQUI
```

Ejemplo:
```bash
python3 router_scanner.py 203.0.113.42
```

## ¿Por qué es importante?

Muchos routers de operadoras (Movistar, Vodafone, Orange, etc.) tienen puertos expuestos a internet para gestión remota. Esto puede ser usado por atacantes para:

- **Cambiar configuración DNS** → Redirigir tu tráfico a sitios falsos
- **Crear botnets** → Usar tu router en ataques DDoS
- **Interceptar tráfico** → Espiar conexiones

## ¿Cómo protegerse?

Si el script encuentra puertos abiertos:

1. Accede a tu router (ej: `192.168.1.1`)
2. Ve a configuración de seguridad/firewall
3. **Desactiva "Gestión remota desde WAN"**
4. Guarda cambios y reinicia router

## Notas de seguridad

- Solo escanea TU propia IP pública
- No escanees IPs de otras personas sin permiso
- Este script es educativo, para concienciación sobre seguridad
- Los escaneos son detectables por firewalls/IDS

## Limitaciones

- Solo escanea 6 puertos (no es exhaustivo)
- Timeout de 1.5s por puerto (puede dar falsos negativos)
- Algunos firewalls pueden bloquear los intentos de conexión

## Contacto

Si tienes dudas o sugerencias:
- TikTok: [@3diklab](https://tiktok.com/@3diklab)
- GitHub Issues: [router-scanner/issues](https://github.com/ediklab/router-scanner/issues)

---

**⚠️ Disclaimer:** Este script es solo para fines educativos. Escanear redes o sistemas sin autorización es ilegal. El autor no se hace responsable del mal uso de esta herramienta.
