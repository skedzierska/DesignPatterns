import abc

class Klawiatura:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Klawiatura, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.key_pressed = 3
        self.klawisze = []

    def register(self, which):
        self.klawisze.append(which)

    def unregister(self, which):
        self.klawisze.remove(which)
      
    def notify(self):
        pass
      
    def update(self):
      for klawisz in object.klawisze:
        print(klawisz.get_key())
        if klawisz.get_key()  == object.key_pressed:
          return "Wcisnieto " + str(klawisz.get_key())
          object.unregister(klawisz)
        else: 
          continue


class Klawisz_inter(metaclass=abc.ABCMeta):    
    
    @abc.abstractmethod
    def get_key(self):
        pass
    
class Klawisz(Klawisz_inter):

    def __init__(self, key):
        self.key = key

    def get_key(self):
       return self.key

        
class Dekorator1(Klawisz):
   def __init__(self, wrapped):
        self._wrapped = wrapped
     
   def update(self):
     return "{} ".format(self._wrapped.update()) + "!"


class Dekorator2(Klawisz):
   def __init__(self, wrapped):
        self._wrapped = wrapped
     
   def update(self):
     return "{} ".format(self._wrapped.update()) + "?"


object = Klawiatura()


k1 = Klawisz(1)
print(k1.get_key())
k2 = Klawisz(22)
k3 = Klawisz(3)
k4 = Klawisz(4)
k5 = Klawisz(5)

object.register(k1)
object.register(k2)
object.register(k3)
object.register(k4)
object.register(k5)

print(object.update())
