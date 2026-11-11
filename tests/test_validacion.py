import unittest
from app.main import validar


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


if __name__ == "__main__":
    unittest.main()
