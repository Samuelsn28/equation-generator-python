from typing import Any
import unittest

from src.valoravel_m import Monomio
from src.incognita_m import Incognita


class MonomioClassTests(unittest.TestCase):
    def setUp(self):
        self.incognita = Incognita('x', 2)

    def test_creating_a_monomio_object(self):
        object = Monomio([self.incognita])

        self.assertIsInstance(object, Monomio)

    def test_creating_a_monomio_object_incorrectly(self):
        def create_monomio_without_incognitas() -> Any:
            monomio = Monomio([])
            return monomio

        def create_monomio_with_coefficient_equals_zero() -> Any:
            monomio = Monomio([self.incognita], 0)
            return monomio

        with self.assertRaises(ValueError):
            create_monomio_without_incognitas()

        with self.assertRaises(ValueError):
            create_monomio_with_coefficient_equals_zero()

    def test_adding_two_monomios(self):
        coefficient_1 = 2
        coefficient_2 = 5
        expected_coefficient = coefficient_1 + coefficient_2

        monomio_1 = Monomio([self.incognita], coefficient_1)
        monomio_2 = Monomio([self.incognita], coefficient_2)
        result_monomio: Monomio = monomio_1.add(monomio_2)

        self.assertEqual(expected_coefficient, result_monomio.get_coefficient())
        self.assertEqual([self.incognita], result_monomio.get_list_incog())

    def test_adding_two_different_monomios(self):
        monomio_1 = Monomio([Incognita('y', 4)])
        monomio_2 = Monomio([self.incognita])
        result = monomio_1.add(monomio_2)

        self.assertEqual(None, result)

    # def test_multiplying_two_monomios(self):


if __name__ == '__main__':
    unittest.main()

