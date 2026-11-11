# Ejercicios

Para cada resultado, di cuál de estas tres cosas es: **ejecutado**, **comprobado con una muestra** o **solo diseñado**.

## Ejercicio 1 · Levántalo y compruébalo (en clase)

1. `git checkout v1.4.0`, `cp .env.example .env`, `docker compose up -d --build`.
2. Corre `./comprobar.sh`. Anota versión, entrada, esperado y obtenido.
3. Cambia `PORT` en `.env` y vuelve a levantarlo. ¿Qué tuviste que cambiar en `comprobar.sh`?
4. Escribe en tres líneas cómo lo ejecutaría otra persona sin preguntarte nada.

## Ejercicio 2 · Verde, pero nadie puede reservar

1. `git checkout v1.5.0`.
2. Corre las pruebas: pasan. Levanta con Compose y corre `./comprobar.sh`: falla.
3. Con `docker compose logs`, encuentra qué cambió entre `v1.4.0` y `v1.5.0` (`git diff v1.4.0 v1.5.0`).
4. Responde: ¿por qué las pruebas no lo detectaron? ¿Por qué `/salud` dice `ok`?
5. Corrígelo de dos formas: ajustando la configuración y ajustando el código. ¿Cuál preferirías operar y por qué?

## Ejercicio 3 · Llévalo a tu proyecto

1. Copia `kit/README.plantilla.md` a tu repositorio y complétalo con tu oportunidad.
2. Agrega a tu proyecto un `comprobar.sh` que pruebe una acción real, no solo que el servicio responda.
3. Marca en tu README qué está ejecutado, qué comprobado con muestra y qué solo diseñado.

## Para el Encuentro 4 (adelanto)

Agrega al flujo de `.github/workflows/ci.yml` un paso que levante el servicio y corra `./comprobar.sh`. Con eso, `v1.5.0` dejaría de salir en verde.
