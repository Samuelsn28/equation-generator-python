

class Incognita:
    def __init__(self, incog_simbol: str, incog_power: int = 1):
        self.incog_simbol = incog_simbol
        self.incog_power = incog_power

    def get_simbol(self) -> str:
        return self.incog_simbol

    def get_power(self) -> int:
        return self.incog_power

    def multiple(self, another_incog: 'Incognita') -> 'Incognita':
        if another_incog.get_simbol() == self.incog_simbol:
            new_incog_power = another_incog.get_power() + self.incog_power
            return Incognita(self.incog_simbol, new_incog_power)
        pass

    def __eq__(self, other):
        if type(other) is Incognita:
            return self.incog_simbol == other.get_simbol() and self.incog_power == other.get_power()
        return False