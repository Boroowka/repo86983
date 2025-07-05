import unittest
from kalkulator import Kalkulator  # jeszcze nie istnieje

class TestKalkulator(unittest.TestCase):

    def setUp(self):
        self.k = Kalkulator()

    def test_dodawanie(self):
        self.assertEqual(self.k.dodaj(2, 3), 5)

    def test_odejmowanie(self):
        self.assertEqual(self.k.odejmij(5, 3), 2)

    def test_mnozenie(self):
        self.assertEqual(self.k.mnoz(2, 4), 8)

    def test_dzielenie(self):
        self.assertEqual(self.k.dziel(10, 2), 5)

    def test_dzielenie_przez_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.k.dziel(5, 0)
	def test_potegowanie(self):
		self.assertEqual(self.k.poteguj(2, 3), 8)



if __name__ == "__main__":
    unittest.main()
