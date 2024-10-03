from .polinomio_m import Polinomio


class Equation:
    def __init__(self, polinomio: Polinomio, roots: list[int]):
        self.polinomio = polinomio
        self.roots = roots

    def __str__(self):
        return str(self.polinomio) + ' = 0'
