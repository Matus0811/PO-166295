from court import *

class Stadium(Court):
    __name: str
    __common_name: str
    __capacity: int

    def __init__(self, width: float = 68, length: float = 150,
                 address: str = None, year_built: int = None,
                 name: str = None, capacity: int = 0, common_name: str = 'opcjonalny') -> None:
        super().__init__(width, length, address, year_built)
        self.__name = name
        self.__common_name = common_name
        if capacity < 0:
            capacity = 0
        self.__capacity = capacity

    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, value: str) -> None:
        if type(value) != str:
            raise ValueError("Nieodpowiedni typ danych")
        else:
            self.__name = value

    @property
    def common_name(self) -> str:
        return self.__common_name
    @common_name.setter
    def common_name(self, value: str) -> None:
        if type(value) != str:
            raise ValueError("Nieodpowiedni typ danych")
        else:
            self.__common_name = value

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        if type(value) != int:
            raise ValueError("Nieodpowiedni typ danych")
        else:
            self.__capacity = value

    def __eq__(self, other: 'Stadium') -> bool:
        if self.capacity == other.capacity and self.area() == other.area():
            return True
        else:
            return False

    def __ne__(self, other: 'Stadium') -> bool:
        if not self == other:
            return True
        else:
            return False

    def __str__(self) -> str:
        if self.__common_name != 'opcjonalny':
            return f'Boisko wybudowane w roku {self.year_built}, o długości {self.length} i szerokości {self.width} metrów\n' \
                   f'Pole powierzchni: {self.area()} mkw\n' \
                   f'Adres: {self.address}\n' \
                   f'Nazwa: {self.name}\n' \
                   f'Nazwa zwyczajowa: {self.common_name}\n' \
                   f'Pojemność stadionu: {self.capacity} osób'
        else:
            return f'Boisko wybudowane w roku {self.year_built}, o długości {self.length} i szerokości {self.width} metrów\n' \
                   f'Pole powierzchni: {self.area()} mkw\n' \
                   f'Adres: {self.address}\n' \
                   f'Nazwa: {self.name}\n' \
                   f'Pojemność stadionu: {self.capacity} osób'
