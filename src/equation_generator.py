import random
import typing

from .equation_m import Equation
from .incognita_m import Incognita
from .valoravel_m import Integer
from .valoravel_m import Monomio
from .polinomio_m import Polinomio
from .valoravel_m import Valoravel


class RootRange:
    def __init__(self, min_root: int, max_root: int):
        self.__verify_parameters(min_root=min_root, max_root=max_root)
        self.min_root = min_root
        self.max_root = max_root

    def get_min_root(self) -> int:
        return self.min_root

    def get_max_root(self) -> int:
        return self.max_root

    def get_variation(self) -> int:
        return (self.max_root + 1) - self.min_root

    def __verify_parameters(self, min_root: int, max_root: int) -> None:
        if min_root > max_root:
            raise ValueError('"min_root" parameter can\'t be bigger than "max_root".')


class EquationGenerator:
    def generate_equation(self, symbol_incognita: str,
                          power: int, root_range: RootRange,
                          allow_repeted_roots: bool = False) -> Equation:
        self.__verify_parameters(symbol_incognita, power, root_range, allow_repeted_roots)
        roots, all_roots = self.__generate_roots(power, root_range, allow_repeted_roots)
        return self.__create_equation(symbol_incognita, all_roots, roots)

    def __verify_parameters(self, symbol_incognita: str, power: int,
                            root_range: RootRange, allow_repeted_roots: bool) -> None:
        self.__verify_symbol_incognita_parameter(symbol_incognita=symbol_incognita)
        self.__verify_power_parameter(power=power)
        self.__verify_root_range_parameter(root_range=root_range, power=power,
                                           allow_repeted_roots=allow_repeted_roots)

        if (not allow_repeted_roots and
                (abs(root_range.get_min_root()) + abs(root_range.get_max_root())) < power):
            raise ValueError('"power" parameter is too big to roots avaliables. Reduce it '
                             'or increase the "root_range" parameter.')

    def __verify_symbol_incognita_parameter(self, symbol_incognita: str) -> None:
        if symbol_incognita is None:
            raise ValueError('"symbol_incognita" parameter can\' be None.')
        if len(symbol_incognita) > 1:
            raise ValueError('"symbol_incognita" str parameter can\'t be bigger than one.')
        if len(symbol_incognita) == 0:
            raise ValueError('"symbol_incognita" str parameter can\'t be empty.')

    def __verify_power_parameter(self, power: int) -> None:
        if power <= 0:
            raise ValueError('"power" int parameter can\'t be less than or equal to zero.')

    def __verify_root_range_parameter(self, root_range: RootRange, power: int,
                                      allow_repeted_roots: bool) -> None:
        if root_range is None:
            raise ValueError('"root_range" parameter can\'t be None.')
        if not allow_repeted_roots and (root_range.get_variation() < power):
            raise ValueError('"root_range" must have a variation (max_value - min_value)'
                             ' grether than "power" parameter')

    def __generate_roots(self, power: int, root_range: RootRange,
                         allow_repeted_roots: bool) -> tuple[list[int], list[int]]:
        roots: list[int] = []
        all_roots: list[int] = []

        i: int = 0
        while i < power:
            new_root: int = random.randint(root_range.get_min_root(),
                                           root_range.get_max_root())
            if (not allow_repeted_roots) and (new_root in roots):
                continue
            roots.append(new_root)
            all_roots.append(new_root)
            i += 1
        return roots, all_roots

    def __create_equation(self, symbol_incognita: str, all_roots: list[int],
                          roots: list[int]) -> Equation:
        polinomios: list[Polinomio] = self.__create_polinomios(symbol_incognita, all_roots)
        equation_polinomio: Polinomio = self.__multiple_polinomios(polinomios)
        equation_polinomio = self.__add_similar_parts(equation_polinomio)
        return Equation(equation_polinomio, roots)

    def __create_polinomios(self, symbol_incognita: str, all_roots: list[int]) -> list[Polinomio]:
        polinomios: list[Polinomio] = []
        for r in all_roots:
            monomio: Monomio = Monomio([Incognita(symbol_incognita)])
            integer: Integer = Integer(-r)
            list_valoravel: list[Valoravel] = [monomio, integer]
            polinomios.append(Polinomio(list_valoravel))
        return polinomios

    def __multiple_polinomios(self, polinomios: list[Polinomio]) -> Polinomio:
        equation_polinomio: Polinomio = polinomios[0]
        del polinomios[0]

        for p in polinomios:
            equation_polinomio = equation_polinomio.multiple(p)
        return equation_polinomio

    def __add_similar_parts(self, equation_polinomio: Polinomio) -> Polinomio:
        equation_polinomio_valoravel = equation_polinomio.get_valoravel()
        final_integer: Integer = self.__add_all_integers(equation_polinomio_valoravel)
        powers: set[int] = self.__search_powers(equation_polinomio_valoravel)
        monomios: list[Monomio] = self.__add_each_monomio_with_the_same_power(powers, equation_polinomio_valoravel)

        monomios: list[Monomio] = sorted(monomios, key=lambda m: m.get_list_incog()[0].get_power(), reverse=True)

        list_valoravel: list[Valoravel] = []
        list_valoravel = list_valoravel + monomios
        list_valoravel.append(final_integer)

        return Polinomio(list_valoravel)


    def __add_all_integers(self, list_valoravel: list[Valoravel]) -> Integer:
        def filter_integer(valoravel):
            if isinstance(valoravel, Integer):
                return True
            return False
        collected_values = list(filter(filter_integer, list_valoravel))
        final_integer: Integer = typing.cast(Integer, collected_values[0])
        del collected_values[0]

        for v in collected_values:
            integer: Integer = typing.cast(Integer, v)
            final_integer = final_integer.add(integer)
        return final_integer

    def __filter_monomio(self, valoravel):
        if isinstance(valoravel, Monomio):
            return True
        return False

    def __search_powers(self, list_valoravel: list[Valoravel]) -> set[int]:

        found_powers: set[int] = set()
        collected_values = filter(self.__filter_monomio, list_valoravel)

        for v in collected_values:
            monomio: Monomio = typing.cast(Monomio, v)
            found_powers.add(monomio.list_incog[0].get_power())
        return found_powers

    def __add_each_monomio_with_the_same_power(self, powers: set[int],
                                               list_valoravel: list[Valoravel]) -> list[Monomio]:
        def filter_monomios_with_the_same_power(value):
            monomio = typing.cast(Monomio, value)
            if monomio.get_list_incog()[0].get_power() == p:
                return True
            return False
        list_final_monomios: list[Monomio] = []
        list_monomios = list(filter(self.__filter_monomio, list_valoravel))
        for p in powers:
            list_monomios_filtered = list(filter(filter_monomios_with_the_same_power, list_monomios))
            new_monomio: Monomio = typing.cast(Monomio, list_monomios_filtered[0])
            del list_monomios_filtered[0]
            # Adding each monomio
            for m in list_monomios_filtered:
                new_monomio = new_monomio.add(m)
            list_final_monomios.append(new_monomio)
        return list_final_monomios












