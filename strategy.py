from abc import ABCMeta, abstractmethod

class DostepneSrodki():
    
    #zmienne podawne z klawiatury
    koszt = 3
    czas = 30
    ryzyko = 'srednie'
    
    @classmethod
    def move(cls, movement_style):
        movement_style(cls.koszt, cls.czas, cls.ryzyko)

class IMove(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def __call__():
        "Implementors must select the default method"

class Bike(IMove):
    
    @staticmethod
    def bike(koszt,czas,ryzyko):
        koszt1 = 0
        czas1 = 60
        ryzyko1 = 'duze'
        if koszt == koszt1 and czas == czas1 and ryzyko == ryzyko1: 
            print(f"Do przewiezienia przedmiotu: rower")
        else:
            pass

    __call__ = bike

class PublicTransport(IMove):
    
    @staticmethod
    def public_transport(koszt,czas,ryzyko):
        koszt2 = 3
        czas2 = 30
        ryzyko2 = 'srednie'
        if koszt == koszt2 and czas == czas2 and ryzyko == ryzyko2: 
            print(f"Do przewiezienia przedmiotu: komunikacja publiczna")
        else:
            pass

    __call__ = public_transport

class Taxi(IMove):
   
    @staticmethod
    def taxi(koszt,czas,ryzyko):
        koszt3 = 20
        czas3 = 15
        ryzyko3 = 'male'
        if koszt == koszt3 and czas == czas3 and ryzyko == ryzyko3:
            print(f"Do przewiezienia przedmiotu: taksowka")
        else:
            pass

    __call__ = taxi

DOSTEPNE_SRODKI = DostepneSrodki()
DOSTEPNE_SRODKI.move(Bike())
DOSTEPNE_SRODKI.move(PublicTransport())
DOSTEPNE_SRODKI.move(Taxi())
