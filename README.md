# Empieza aquí · Encuentro 3

Este ejemplo es un servicio pequeño (`reservas-canchas`) para practicar imagen, contenedor, configuración y persistencia. Usa solo datos ficticios.

## Cómo obtenerlo
- Si ya tienes el repositorio: `git fetch origin` y `git checkout ejercicio-3-contenedor`.
- Si no: `git clone -b ejercicio-3-contenedor https://github.com/santiagohenao97/reservas-canchas.git`
- Sin git: descarga el ZIP de la rama desde GitHub (Code → Download ZIP), descomprímelo y entra a la carpeta. Ahí `comprobar.sh` se corre con `bash comprobar.sh`.

**Antes de empezar:** si dejaste algo corriendo de ejercicios anteriores, entra a esa carpeta y ejecuta `docker compose down`. Comparte el puerto 8000.

## Qué necesitas
- Docker instalado y abierto. Verifica: `docker --version` y `docker run hello-world`.
- La carpeta del ejemplo en tu equipo (clonada o descomprimida) y una terminal dentro de ella.

## Lo mínimo para verlo funcionando
```
cp .env.example .env
docker compose up -d --build
bash comprobar.sh
```
La última línea debe decir `ok`. Para apagarlo: `docker compose down`.

## Los archivos
- `app/` · el servicio.
- `Dockerfile` · cómo se construye la imagen.
- `.dockerignore` · qué no entra a la imagen.
- `compose.yaml` · cómo se ejecuta (puerto, configuración, datos).
- `.env.example` · configuración de ejemplo, sin secretos. Tu `.env` real no se sube.
- `comprobar.sh` · la prueba A: crea una reserva y la busca en el listado.
- `docs/etapas/E03.md` · guía de la etapa, con un ejercicio para romper cosas y comprobar.
- `dev` y `herramientas/` · opcional: los mismos pasos como script y una ayuda de diagnóstico. En clase usamos `docker compose` directamente.

## Si el puerto 8000 está ocupado
Abre `.env` y cambia `PORT=8000` por otro número (por ejemplo `PORT=8002`). Luego repite `docker compose up -d --build`. En `comprobar.sh`, usa `bash comprobar.sh http://localhost:8002`.

## Si no puedes ejecutar Docker
Sigue la clase con las salidas compartidas por el docente y declara en tu README que no ejecutaste.
