# reservas-canchas

API pequeña para reservar canchas barriales (3 canchas, horas en punto de 08:00 a 21:00).
Es el servicio de práctica del **Encuentro 1 · Estud-IA, Arquitectura en la nube (nivel intermedio)**. Los datos son sintéticos y no hay secretos.

## Cómo ejecutarlo

Requiere Docker con Compose.

```bash
cp .env.example .env
docker compose up -d --build
./comprobar.sh
```

La salida esperada de `comprobar.sh` termina en `ok`. Si no, el script dice qué falló.

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
