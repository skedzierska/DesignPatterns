import random
from abc import ABC,abstractmethod


class Rozwiazanie(ABC):
     @abstractmethod
     def algorytm(self):
         pass

class Rozwiazanie_1(Rozwiazanie):
     def algorytm(self):
       m = 3
       n = 6
       l = random.sample(range(1,n), m)
       l.sort()
       return l

       
class Rozwiazanie_2(Rozwiazanie):
     def algorytm(self):
       m = 5
       n = 10
       l = [x for x in range(0,n)]
       podciag = l[:m]
       random.shuffle(podciag)
       return podciag
         
       
class Rozwiazanie_3(Rozwiazanie):
     def algorytm(self):
       m = 30
       n = 60
       podciag =[]
       l= [ random.randrange(1, n, 1) for i in range(m)]
       for i in l:
         if i not in podciag:
           podciag.append(i)
       return podciag       

class Fabryka(ABC):
     @abstractmethod
     def create(self):
         pass

class Fabryka1(Fabryka):
     def create(self):
         return Rozwiazanie_1()

class Fabryka2(Fabryka):
     def create(self):
         return Rozwiazanie_2()


class Fabryka3(Fabryka):
     def create(self):
         return Rozwiazanie_3()

rodzaj = 'alg1'
if rodzaj =='alg1':
  factory = Fabryka1()
elif rodzaj ==' alg2':
  factory = Fabryka2()
elif rodzaj =='alg3':
  factory = Fabryka3()
else:
     raise NotImplementedError(f"nie ma fabryki dla typu {rodzaj}")

algorytm = factory.create()
result = algorytm.algorytm()
print(result)



