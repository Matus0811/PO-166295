import datetime

class Court:
    __width: float
    __length: float
    __address: str
    __year_built: int

    def __init__(self, width: float=68, length: float=150, address: str=None, year_built: int=None ) -> None:
        if width > 45 or width < 90 or length <90 or length >120:
            width = 68
            length = 150

        self.__width = width
        self.__length = length
        self.__address = address
        self.__year_built = year_built

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, value: float) -> None:
        if value < 45 or value > 90:
            raise ValueError("Podano nieodpowiednią wartość dla parametru width")
        else:
            self.__width = value

    @property
    def length(self) -> float:
        return self.__width

    @length.setter
    def length(self, value: float) -> None:
        if value < 90 or value > 120:
            raise ValueError("Podano nieodpowiednią wartość dla parametru length")
        else:
            self.__length = value

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str) -> None:
        if type(value) != str:
            raise ValueError("Nieodpowiedni typ danych")
        else:
            self.__address = value

    @property
    def year_built(self) -> int:
        return self.__year_built

    @year_built.setter
    def year_built(self, value: int) -> None:
        if type(value) != int:
            raise ValueError("Nieodpowiedni typ danych")
        else:
            self.__year_built = value


    def area(self):
        return self.__width * self.__year_built


    @staticmethod
    def validate(cls: 'Court') -> None:
        obecny = int(datetime.date.today().year)
        if cls.__year_built < 0 or cls.__year_built > obecny:
            cls.__year_built = obecny

    def __str__(self) -> str:
        return f'Boisko wybudowane w roku {self.year_built}, o długości {self.length} i szerokości {self.width} metrów\n' \
               f'Pole powierzchni: {self.area()} mkw\n' \
               f'Adres: {self.address}'

    def __eq__(self, other: 'Court') -> bool:
        if self.area() == other.area():
            return True
        else:
            return False

    def __ne__(self, other: 'Court') -> bool :
        if not self == other:
            return True
        else:
            return False