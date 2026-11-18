#!/usr/bin/env bash
# Comprueba con una acción real: el servicio responde, una reserva se crea y aparece en el listado.
# Uso: ./comprobar.sh [URL] [VERSIÓN_ESPERADA]     (por defecto http://localhost:8000)
set -u
URL="${1:-http://localhost:8000}"
ESPERADA="${2:-}"
OUT=$(mktemp); trap 'rm -f "$OUT"' EXIT
for _ in $(seq 1 20); do curl -fs "$URL/salud" >/dev/null 2>&1 && break; sleep 1; done
SALUD=$(curl -s "$URL/salud") || { echo "FALLA: no responde $URL/salud"; exit 1; }
VERSION=$(echo "$SALUD" | sed -n 's/.*"version": *"\([^"]*\)".*/\1/p')
echo "versión   ${VERSION:-?}"
if [ -n "$ESPERADA" ] && [ "$VERSION" != "$ESPERADA" ]; then
  echo "FALLA: se esperaba la versión $ESPERADA y responde ${VERSION:-?}"; exit 1
fi
CODIGO=$(curl -s -o "$OUT" -w '%{http_code}' -X POST "$URL/reservas" -H 'Content-Type: application/json' \
  -d '{"cancha": 2, "hora": "18:00", "nombre": "Prueba"}')
echo "entrada   POST /reservas  cancha=2 hora=18:00"
echo "esperado  201"
echo "obtenido  $CODIGO"
[ "$CODIGO" = "201" ] || { echo "FALLA: $(cat "$OUT")"; exit 1; }
ID=$(sed -n 's/.*"id": *\([0-9]*\).*/\1/p' "$OUT")
curl -s "$URL/reservas" | grep -q '"hora": "18:00"' || { echo "FALLA: la reserva no aparece en GET /reservas"; exit 1; }
curl -s -X DELETE "$URL/reservas/$ID" >/dev/null
echo "ok"
