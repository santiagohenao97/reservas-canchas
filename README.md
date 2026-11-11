# reservas-canchas

API pequeña para reservar canchas barriales (3 canchas, horas en punto de 08:00 a 21:00).
Es el servicio de práctica del **Encuentro 1 · Estud-IA, Arquitectura en la nube (nivel intermedio)**. Los datos son sintéticos y no hay secretos.

## Cómo ejecutarlo

Requiere Docker con Compose. Hay tres caminos que hacen lo mismo, de menos a más automatizado.

> `main` contiene el código de `v1.5.0`, que está roto a propósito (Ejercicio 2). Para ver el servicio funcionando, parte de `v1.4.0`.

**A mano** (entiendes cada paso):

```bash
git checkout v1.4.0
cp .env.example .env
docker compose up -d --build
./comprobar.sh
git checkout main        # al terminar
```

**Con el script `dev`** (dos comandos, sin cambiar de rama):

```bash
./dev levantar v1.4.0     # construye, levanta y comprueba con una reserva real (v1.4.0 es el valor por defecto)
./dev levantar v1.5.0     # la versión rota: termina en FALLÓ
./dev diagnosticar        # reúne la evidencia y le pide la causa a una IA (necesita `claude`)
```

**Con Claude Code** (un comando; la IA decide qué mirar):

```
/verificar v1.5.0
```

La salida esperada de `comprobar.sh` termina en `ok`. Si no, el script dice qué falló.

## Cómo está hecho `dev`

| Parte | Quién la hace | Por qué |
|---|---|---|
| Levantar, comprobar, reunir evidencia | Script (`dev`) | Es repetible: siempre los mismos pasos |
| Interpretar la evidencia | IA (`herramientas/diagnostico.md`) | Requiere juicio: relacionar logs, diff y pruebas |
| Decidir y aplicar la corrección | Una persona | La IA solo propone; no tiene permiso de escritura |

`dev` no incluye `.env` en la evidencia que envía a la IA.

## Qué expone

| Método | Ruta | Qué hace |
|---|---|---|
| GET | `/salud` | Estado y versión |
| GET | `/reservas` | Lista las reservas |
| POST | `/reservas` | Crea una: `{"cancha": 2, "hora": "18:00", "nombre": "Camila"}` |
| DELETE | `/reservas/{id}` | Elimina una |

Códigos: `201` creada, `400` datos inválidos, `409` cancha ocupada a esa hora.

## Configuración

Por variables de entorno (ver `.env.example`): `PORT` y `DB_PATH`.

## Versiones

- `v1.4.0`: funciona.
- `v1.5.0`: la integración sale en verde, pero el servicio no puede reservar. Es el Ejercicio 2.

```bash
git checkout v1.5.0
```

## Pruebas

```bash
python -m unittest discover -s tests -v
```

## Ejercicios

Ver [EJERCICIOS.md](EJERCICIOS.md). La plantilla para tu propio proyecto está en [kit/README.plantilla.md](kit/README.plantilla.md).
