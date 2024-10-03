from src.valoravel_m import Integer
import unittest


class IntegerClassTests(unittest.TestCase):
    def test_create_a_integer_object(self):
        object = Integer(10)

        self.assertIsInstance(object, Integer)

    def test_getting_value_of_integer(self):
        value = 362
        integer: Integer = Integer(value)

        self.assertEqual(integer.get_value(), value)

    def test_adding_two_integers(self):
        value_1 = 10
        value_2 = 90
        expected_value = value_1 + value_2

        integer_1: Integer = Integer(value_1)
        integer_2: Integer = Integer(value_2)
        result_integer: Integer = integer_1.add(integer_2)

        self.assertEqual(result_integer.get_value(), expected_value)

    def test_multipling_two_integers(self):
        value_1 = 7
        value_2 = 9
        expected_value = value_1 * value_2

        integer_1: Integer = Integer(value_1)
        integer_2: Integer = Integer(value_2)
        result_integer = integer_1.multiple(integer_2)

        self.assertEqual(result_integer.get_value(), expected_value)


if __name__ == '__main__':
    unittest.main()
