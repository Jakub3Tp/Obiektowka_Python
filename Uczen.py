from Czlowiek import Czlowiek
class Uczen:

    Liczba_uczniow = 0

    def __init__(self, imie, nazwisko):
        self.__imie = imie
        self.__nazwisko = nazwisko
        Uczen.Liczba_uczniow += 1


    def __str__(self):
        return f'{self.__imie} {self.__nazwisko}'

    def ucz_sie(self):
        print(f'{self.__imie} {self.__nazwisko} uczy się!')