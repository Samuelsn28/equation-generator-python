import typing

from .valoravel_m import Integer
from .valoravel_m import Monomio
from .valoravel_m import Valoravel

class Polinomio:
    def __init__(self, list_valoravel: list[Valoravel]):
        if not list_valoravel or list_valoravel is None:
            raise ValueError('"list_valoravel" can\'t be empty.')
        self.valoravel = list_valoravel

    def get_valoravel(self) -> list[Valoravel]:
        return self.valoravel

    def multiple(self, other_polinomio: 'Polinomio') -> 'Polinomio':
        if other_polinomio is None:
            return None

        new_valoravel: list[Valoravel] = []
        for v1 in self.valoravel:
            for v2 in other_polinomio.get_valoravel():
                result_valoravel = v1.multiple(v2)

                if result_valoravel is not None:
                    new_valoravel.append(result_valoravel)
        return Polinomio(new_valoravel)

    def __str__(self):
        return_str: str = ''
        for i, v in enumerate(self.get_valoravel()):
            if (i == 0) or (isinstance(v, Integer)):
                return_str += str(v)
                continue
            m = typing.cast(Monomio, v)
            if m.coefficient == 1:
                return_str += '+'
            return_str += str(v)
        return return_str


