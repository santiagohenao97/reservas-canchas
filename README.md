# Empieza aquí · Encuentro 3

Este ejemplo es un servicio pequeño (`reservas-canchas`) para practicar imagen, contenedor, configuración y persistencia. Usa solo datos ficticios.

## Cómo obtenerlo
- Si ya tienes el repositorio: `git fetch origin` y `git checkout ejercicio-3-contenedor`.
- Si no: `git clone -b ejercicio-3-contenedor https://github.com/santiagohenao97/reservas-canchas.git`
- Sin git: descarga el ZIP de la rama desde GitHub (Code → Download ZIP), descomprímelo y entra a la carpeta.

**Antes de empezar:** si dejaste algo corriendo de ejercicios anteriores, entra a esa carpeta y ejecuta `docker compose down`. Este ejemplo también usa el puerto 8000.

## Qué necesitas
- Docker instalado y abierto. Verifica: `docker --version` y `docker run hello-world`.
- La carpeta del ejemplo en tu equipo (clonada o descomprimida).
- Una terminal abierta dentro de esa carpeta: Terminal en Mac o Linux, **PowerShell** en Windows.

## Lo mínimo para verlo funcionando
Corre los comandos uno a uno y mira qué responde cada uno. Funcionan igual en Mac, Linux y Windows, salvo el paso 5, que tiene una versión para cada uno.

**1. Crea tu configuración** a partir del ejemplo:
```
cp .env.example .env
```

**2. Construye la imagen y levanta el servicio:**
```
docker compose up -d --build
```

**3. Revisa que el contenedor esté arriba:**
```
docker compose ps
```
En la columna de estado debe aparecer `Up`. A los pocos segundos debe decir `(healthy)`.

**4. Pregúntale al servicio si está sano.** Abre en el navegador http://localhost:8000/salud. Debe responder `"estado": "ok"` y la versión.

**5. Crea una reserva** (una acción real, no solo "responde"):

Mac, Linux o Git Bash:
```
curl -X POST http://localhost:8000/reservas -H 'Content-Type: application/json' -d '{"cancha": 2, "hora": "18:00", "nombre": "Prueba"}'
```
Windows (PowerShell):
```
Invoke-RestMethod -Method Post -Uri http://localhost:8000/reservas -ContentType 'application/json' -Body '{"cancha": 2, "hora": "18:00", "nombre": "Prueba"}'
```
Debe devolver la reserva con su `id`.

**6. Comprueba que quedó guardada.** Abre http://localhost:8000/reservas en el navegador. Debe aparecer la cancha 2 a las 18:00.

**7. Apágalo:**
```
docker compose down
```
La reserva no se borra: queda guardada en un volumen de Docker. Si lo vuelves a levantar, sigue ahí. Para borrar también los datos: `docker compose down -v`.

> **Si repites el paso 5** recibes el error `esa cancha ya está reservada a esa hora` (código 409). No se dañó nada: los datos persisten y el servicio no deja reservar dos veces la misma cancha a la misma hora. Cambia la hora (por ejemplo `"19:00"`) o borra los datos con `docker compose down -v`.

### Atajo opcional: los pasos 4 a 6 en uno
`comprobar.sh` hace los pasos 4 a 6, borra la reserva de prueba y termina en `ok` o `FALLA`. Es un script de bash: córrelo en Mac, en Linux o, en Windows, desde **Git Bash** o WSL (no funciona en PowerShell).
```
bash comprobar.sh
```

## Los archivos
- `app/` · el servicio.
- `Dockerfile` · cómo se construye la imagen.
- `.dockerignore` · qué no entra a la imagen.
- `compose.yaml` · cómo se ejecuta (puerto, configuración, datos).
- `.env.example` · configuración de ejemplo, sin secretos. Tu `.env` real no se sube.
- `comprobar.sh` · opcional: los pasos 4 a 6 en un solo comando (bash).
- `docs/etapas/E03.md` · guía de la etapa, con un ejercicio para romper cosas y comprobar.
- `dev` y `herramientas/` · opcional (bash): los mismos pasos como script y una ayuda de diagnóstico. En clase usamos `docker compose` directamente.

## Si el puerto 8000 está ocupado
Abre `.env` y cambia `PORT=8000` por otro número (por ejemplo `PORT=8002`). Luego repite `docker compose up -d --build` y usa ese número en todas las direcciones: http://localhost:8002/salud, `http://localhost:8002/reservas` en el paso 5, y `bash comprobar.sh http://localhost:8002` si usas el atajo.

## Si no puedes ejecutar Docker
Sigue la clase con las salidas compartidas por el docente y declara en tu README que no ejecutaste.
