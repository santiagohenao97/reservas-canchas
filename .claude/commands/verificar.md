---
description: Levanta reservas-canchas en una versión, la comprueba con una reserva real y, si falla, diagnostica la causa (solo lectura).
argument-hint: [versión: v1.4.0 | v1.5.0 | HEAD]
allowed-tools: Bash(./dev levantar:*), Bash(docker compose -p reservas logs:*), Bash(git diff:*), Bash(git describe:*), Bash(git log:*), Read
---

Verifica el servicio de reservas en la versión **$ARGUMENTS** (si viene vacía, usa `HEAD`).

## 1. Levantar y comprobar
Corre `./dev levantar $ARGUMENTS`. Ese script construye, levanta y ejecuta una reserva real.
Si termina bien, resume en dos líneas qué quedó **ejecutado** y qué **solo diseñado**, y detente.

## 2. Si falló, diagnostica
A diferencia de `./dev diagnosticar`, aquí NO hay una lista fija de evidencia: decide tú qué mirar y en qué orden.
Fuentes permitidas: `.run/comprobar.txt`, los logs (`docker compose -p reservas logs --tail 30`), el código en `.run/`, y `git diff <versión anterior> <versión>`.

Reglas:
- **Solo lectura.** No edites archivos, no cambies de rama, no reinicies nada. Propón, no apliques.
- Cada afirmación cita la línea de evidencia que la sostiene. Si falta evidencia, dilo; no inventes.
- No leas ni muestres `.env`.
- Etiqueta cada conclusión: ejecutado, comprobado con una muestra o solo diseñado.

Responde con el formato de `herramientas/diagnostico.md`: Qué falló · Causa · Por qué nadie lo vio antes · Dos formas de corregirlo (con recomendación) · Qué sigue sin comprobarse.
