# Ejercicios

Para cada resultado, di cuál de estas tres cosas es: **ejecutado**, **comprobado con una muestra** o **solo diseñado**.

## Ejercicio 1 · Levántalo y compruébalo (en clase)

1. A mano: `git checkout v1.4.0`, `cp .env.example .env`, `docker compose up -d --build`. Luego vuelve a `main`.
2. Corre `./comprobar.sh`. Anota versión, entrada, esperado y obtenido. Después repítelo con `./dev levantar v1.4.0` y compara: ¿qué hizo el script por ti?
3. Cambia `PORT` en `.env` y vuelve a levantarlo. ¿Qué tuviste que cambiar en `comprobar.sh`?
4. Escribe en tres líneas cómo lo ejecutaría otra persona sin preguntarte nada.

## Ejercicio 2 · Verde, pero nadie puede reservar

1. `git checkout v1.5.0`.
2. Corre las pruebas: pasan. Levanta con Compose y corre `./comprobar.sh`: falla.
3. Con `docker compose logs`, encuentra qué cambió entre `v1.4.0` y `v1.5.0` (`git diff v1.4.0 v1.5.0`). Puedes levantar la versión rota con `./dev levantar v1.5.0`.
4. Responde: ¿por qué las pruebas no lo detectaron? ¿Por qué `/salud` dice `ok`?
5. Corrígelo de dos formas: ajustando la configuración y ajustando el código. ¿Cuál preferirías operar y por qué?

## Ejercicio 2b · Compara tu diagnóstico con el de una IA

1. Corre `./dev diagnosticar` (o `/verificar v1.5.0` en Claude Code).
2. Compara con tu diagnóstico del Ejercicio 2. ¿Qué vio ella que tú no? ¿Qué vio él que ella no?
3. Abre `.run/evidencia.md`: es lo único que la IA recibió. ¿Qué evidencia le faltó? ¿Qué no debería recibir nunca?
4. Lee `herramientas/diagnostico.md`. Cambia una regla (por ejemplo, quita "no inventes") y vuelve a correrlo. ¿Qué cambió en la respuesta?
5. Marca cada afirmación de la IA como ejecutada, comprobada con una muestra o solo diseñada.
6. Responde: ¿qué parte automatizarías siempre y qué parte dejarías a una persona?

## Ejercicio 3 · Llévalo a tu proyecto

1. Copia `kit/README.plantilla.md` a tu repositorio y complétalo con tu oportunidad.
2. Agrega a tu proyecto un `comprobar.sh` que pruebe una acción real, no solo que el servicio responda.
3. Marca en tu README qué está ejecutado, qué comprobado con muestra y qué solo diseñado.
4. Opcional: copia `dev` y `herramientas/diagnostico.md` a tu proyecto y adáptalos (puerto, nombre del proyecto, qué evidencia reunir).

## Para el Encuentro 4 (adelanto)

Agrega al flujo de `.github/workflows/ci.yml` un paso que levante el servicio y corra `./comprobar.sh`. Con eso, `v1.5.0` dejaría de salir en verde.
