"""API mínima de reservas de canchas barriales. Solo biblioteca estándar. Datos sintéticos."""
import json, os, re, sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERSION = "1.4.0"
HORA = re.compile(r"^(0[8-9]|1[0-9]|2[0-1]):00$")  # horas en punto, 08:00 a 21:00


def validar(d):
    """Devuelve (datos_limpios, error)."""
    try:
        cancha = int(d.get("cancha"))
    except (TypeError, ValueError):
        return None, "cancha debe ser 1, 2 o 3"
    if cancha not in (1, 2, 3):
        return None, "cancha debe ser 1, 2 o 3"
    hora = str(d.get("hora", ""))
    if not HORA.match(hora):
        return None, "hora debe ser HH:00 entre 08:00 y 21:00"
    nombre = str(d.get("nombre", "")).strip()
    if not nombre or len(nombre) > 40:
        return None, "nombre es obligatorio (máximo 40 caracteres)"
    return {"cancha": cancha, "hora": hora, "nombre": nombre}, None


def db():
    path = os.environ.get("DB_PATH", "/data/reservas.db")
    con = sqlite3.connect(path)
    con.execute("CREATE TABLE IF NOT EXISTS reservas (id INTEGER PRIMARY KEY, cancha INT, hora TEXT, nombre TEXT, UNIQUE(cancha, hora))")
    return con


class H(BaseHTTPRequestHandler):
    def _send(self, code, body):
        raw = json.dumps(body, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def log_message(self, fmt, *a):
        print("%s %s" % (self.command, self.path), *a[1:2], flush=True)

    def do_GET(self):
        if self.path == "/salud":
            return self._send(200, {"estado": "ok", "version": VERSION})
        if self.path == "/reservas":
            try:
                con = db()
                rows = con.execute("SELECT id,cancha,hora,nombre FROM reservas ORDER BY cancha,hora").fetchall()
            except Exception as e:
                print("ERROR", repr(e), flush=True)
                return self._send(500, {"error": "error interno"})
            return self._send(200, [dict(zip(("id", "cancha", "hora", "nombre"), r)) for r in rows])
        self._send(404, {"error": "no existe"})

    def do_POST(self):
        if self.path != "/reservas":
            return self._send(404, {"error": "no existe"})
        try:
            n = int(self.headers.get("Content-Length", 0))
            datos = json.loads(self.rfile.read(n) or b"{}")
        except ValueError:
            return self._send(400, {"error": "JSON inválido"})
        d, err = validar(datos)
        if err:
            return self._send(400, {"error": err})
        try:
            con = db()
            cur = con.execute("INSERT INTO reservas (cancha,hora,nombre) VALUES (?,?,?)", (d["cancha"], d["hora"], d["nombre"]))
            con.commit()
        except sqlite3.IntegrityError:
            return self._send(409, {"error": "esa cancha ya está reservada a esa hora"})
        except Exception as e:
            print("ERROR", repr(e), flush=True)
            return self._send(500, {"error": "error interno"})
        self._send(201, dict(id=cur.lastrowid, **d, version=VERSION))

    def do_DELETE(self):
        m = re.match(r"^/reservas/(\d+)$", self.path)
        if not m:
            return self._send(404, {"error": "no existe"})
        con = db()
        con.execute("DELETE FROM reservas WHERE id=?", (int(m.group(1)),))
        con.commit()
        self._send(200, {"eliminada": int(m.group(1))})


if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", "8000"))
    print("reservas %s escuchando en :%d" % (VERSION, puerto), flush=True)
    ThreadingHTTPServer(("0.0.0.0", puerto), H).serve_forever()
