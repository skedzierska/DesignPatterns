from abc import ABC, abstractmethod

class Interface(ABC):

    @abstractmethod
    def register(self, which):
        pass
    @abstractmethod
    def unregister(self, which):
        pass
    @abstractmethod
    def dispatch(self, message):
        pass
    
class Observer(ABC):
    
    @abstractmethod
    def update(self, subject):
        pass

class Klawisz(Observer):
    def __init__(self, key):
        self.key = key

    def update(self, message):
        print(' {} {}'.format(message, self.key))
        
class Klawiatura(Interface):
    # ref instancji 
    __instance__ = None

    def __init__(self):
        self.key_pressed = 'Alice'
        self.klawisze = set()

        # spraw czy jest instancja
        if Klawiatura.__instance__ is None:
            # tworz i zap instancji
            Klawiatura.__instance__ = self
        else:
            raise Exception("Nie mozna stworzyc instancji")
            
    # pobranie intancji
    @staticmethod
    def getInstance():
        if not Klawiatura.__instance__:
            Klawiatura()
        return Klawiatura.__instance__

    def register(self, which):
        self.klawisze.add(which)

    def unregister(self, which):
        self.klawisze.discard(which)
        #pub.dispatch('istniejace klawisze')

    def dispatch(self, message):
        for klawisz in self.klawisze:
            klawisz.update(message)

pub = Klawiatura()

k1 = Klawisz('Bob')
k2 = Klawisz('Alice')
k3 = Klawisz('John')
k4 = Klawisz('Rob')
k5 = Klawisz('Gina')

# zapisywanie w set()
pub.register(k1)
pub.register(k2)
pub.register(k3)
pub.register(k4)
pub.register(k5)

if pub.key_pressed == k2.key:
    print("Wcisnięto klawisz", k2.key)
    pub.unregister(k2)
