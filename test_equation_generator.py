import unittest

from src.equation_generator import EquationGenerator
from src.equation_generator import RootRange
from src.equation_m import Equation


class TestEquationGenerator(unittest.TestCase):
    def test_creating_an_equation_gerator_object(self):
        object = EquationGenerator()

        self.assertIsInstance(object, EquationGenerator)

    def test_generate_a_equation_with_power_2(self):
        eg: EquationGenerator = EquationGenerator()

        result_equation: Equation = eg.generate_equation(symbol_incognita='x',
                                                         power=2,
                                                         root_range=RootRange(1, 3),
                                                         allow_repeted_roots=False)
        self.assertIsInstance(eg, EquationGenerator)

        print(result_equation)
        print(result_equation.roots)


if __name__ == '__main__':
    unittest.main()

