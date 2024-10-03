from abc import ABC, abstractmethod
import typing

from .incognita_m import Incognita

class Valoravel(ABC):

    @abstractmethod
    def multiple(self, other_valoravel: 'Valoravel') -> 'Valoravel':
        pass


class Monomio:
    pass


class Integer(Valoravel):
    def __init__(self, value: int = 0):
        self.value = value

    def get_value(self) -> int:
        return self.value

    def add(self, another_integer: 'Integer') -> 'Integer':
        new_value: int = self.value + another_integer.get_value()
        return Integer(new_value)

    def multiple(self, other_valoravel: Valoravel) -> Valoravel | None:
        if isinstance(other_valoravel, Monomio):
            return self.__multiple_monomio(typing.cast(Monomio, other_valoravel))
        if isinstance(other_valoravel, Integer):
            return self.__multiple_integer(typing.cast(Integer, other_valoravel))
        return None

    def __multiple_monomio(self, monomio: Monomio) -> Monomio | None:
        return monomio.multiple(Integer(self.value))

    def __multiple_integer(self, another_integer: 'Integer') -> 'Integer':
        new_value: int = self.value * another_integer.get_value()
        return Integer(new_value)

    def __str__(self):
        if self.value == abs(self.value):
            return '+' + str(self.value)
        return str(self.value)


class Monomio(Valoravel):
    def __init__(self, list_incog: list[Incognita], coefficient: int = 1):
        if not list_incog:
            raise ValueError('"list_incog" is empty')
        if coefficient == 0:
            raise ValueError('"coefficient" doesn\'t be equal 0')
        self.list_incog = list_incog
        self.coefficient = coefficient

    def get_coefficient(self) -> int:
        return self.coefficient

    def get_list_incog(self) -> list[Incognita]:
        return self.list_incog

    def add(self, other_monomio: 'Monomio') -> 'Monomio':
        if other_monomio is None:
            return None

        if other_monomio.get_list_incog() != self.list_incog:
            return None
        return Monomio(self.list_incog, (other_monomio.get_coefficient() + self.coefficient))

    def multiple(self, other_valoravel: Valoravel) -> Valoravel | None:
        if isinstance(other_valoravel, Monomio):
            return self.__multiple_monomio(typing.cast(Monomio, other_valoravel))
        if isinstance(other_valoravel, Integer):
            m = self.__multiple_integer(typing.cast(Integer, other_valoravel))
            return m
        return None

    def __multiple_monomio(self, other_monomio: 'Monomio') -> 'Monomio':
        final_incognitas = self.list_incog[:]
        for inc in other_monomio.get_list_incog():
            break_now = False
            for index, inc2 in enumerate(final_incognitas):
                if inc.get_simbol() != inc2.get_simbol():
                    continue
                final_incognitas[index] = inc2.multiple(inc)
                break_now = True
                break
            if break_now:
                break
            if inc not in final_incognitas:
                final_incognitas.append(inc)
                continue
        return Monomio(final_incognitas, (self.coefficient * other_monomio.get_coefficient()))

    def __multiple_integer(self, integer: Integer) -> 'Monomio':
        return Monomio(self.list_incog, (self.coefficient * integer.get_value()))

    def __str__(self):
        return_str = ''
        if self.coefficient > 1:
            return_str += '+' + str(self.coefficient)
        if self.coefficient < -1:
            return_str += str(self.coefficient)
        if self.coefficient == -1:
            return_str += '-'

        for i in self.list_incog:
            return_str += i.get_simbol()
            if i.get_power() != 1:
                return_str += '^(' + str(i.get_power()) + ')'
        return return_str


