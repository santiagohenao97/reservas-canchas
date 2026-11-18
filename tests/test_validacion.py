import os, tempfile, unittest
from app.main import validar, db


class Validacion(unittest.TestCase):
    def test_reserva_valida(self):
        d, e = validar({"cancha": 2, "hora": "18:00", "nombre": "Camila"})
        self.assertIsNone(e)
        self.assertEqual(d["cancha"], 2)

    def test_cancha_inexistente(self):
        self.assertIsNotNone(validar({"cancha": 9, "hora": "18:00", "nombre": "Camila"})[1])

    def test_hora_fuera_de_rango(self):
        self.assertIsNotNone(validar({"cancha": 1, "hora": "23:00", "nombre": "Camila"})[1])

    def test_nombre_vacio(self):
        self.assertIsNotNone(validar({"cancha": 1, "hora": "10:00", "nombre": " "})[1])


class FallaControlada(unittest.TestCase):
    def test_falla_db_rompe_la_conexion(self):
        os.environ["FALLA"] = "db"
        try:
            with self.assertRaises(Exception):
                db()
        finally:
            del os.environ["FALLA"]

    def test_db_normal_funciona(self):
        with tempfile.TemporaryDirectory() as d:
            os.environ["DB_PATH"] = os.path.join(d, "t.db")
            try:
                db().execute("SELECT 1")
            finally:
                del os.environ["DB_PATH"]


if __name__ == "__main__":
    unittest.main()
