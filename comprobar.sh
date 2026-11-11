#!/usr/bin/env bash
# Comprueba que el servicio responde y que una reserva real se crea y se lista.
# Uso: ./comprobar.sh [URL]   (por defecto http://localhost:8000)
set -u
URL="${1:-http://localhost:8000}"
for i in $(seq 1 20); do curl -fs "$URL/salud" >/dev/null 2>&1 && break; sleep 1; done
SALUD=$(curl -s "$URL/salud") || { echo "FALLA: no responde $URL/salud"; exit 1; }
VERSION=$(echo "$SALUD" | sed -n 's/.*"version": *"\([^"]*\)".*/\1/p')
ENTRADA='{"cancha": 2, "hora": "18:00", "nombre": "Prueba"}'
RESP=$(curl -s -o /tmp/comprobar.out -w '%{http_code}' -X POST "$URL/reservas" -H 'Content-Type: application/json' -d "$ENTRADA")
echo "versión   ${VERSION:-?}"
echo "entrada   POST /reservas  cancha=2 hora=18:00"
echo "esperado  201"
echo "obtenido  $RESP"
if [ "$RESP" != "201" ]; then echo "FALLA: $(cat /tmp/comprobar.out)"; exit 1; fi
ID=$(sed -n 's/.*"id": *\([0-9]*\).*/\1/p' /tmp/comprobar.out)
curl -s "$URL/reservas" | grep -q '"hora": "18:00"' || { echo "FALLA: la reserva no aparece en GET /reservas"; exit 1; }
curl -s -X DELETE "$URL/reservas/$ID" >/dev/null
echo "ok"
