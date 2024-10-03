from src.incognita_m import Incognita
import unittest


class IncognitaClassTests(unittest.TestCase):
    def test_creating_an_incognita_object(self):
        object = Incognita('a', 1)

        self.assertIsInstance(object, Incognita)

    def test_multiplication_between_incognitas_of_the_same_symbol(self):
        incognita_1: Incognita = Incognita('x', 1)
        incognita_2: Incognita = Incognita('x', 2)
        result_incognita = incognita_1.multiple(incognita_2)

        self.assertEqual(result_incognita.get_power(), 3)
        self.assertEqual(result_incognita.get_simbol(), 'x')

    def test_multiplication_between_incognitas_of_different_symbols(self):
        incognita_x: Incognita = Incognita('x', 1)
        incognita_y: Incognita = Incognita('y', 1)
        result_incognita: Incognita = incognita_x.multiple(incognita_y)

        self.assertIs(result_incognita, None)


if __name__ == '__main__':
    unittest.main()

