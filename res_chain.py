from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
import numpy as np
import time

class Handler(ABC):

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class AbstractHandler(Handler):
   
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class QuadraticHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        list1 = [31,-41,59,26,-53,58,97,-93,-23,84] 
        vector1 = np.array(list1)
        print("Vector: ", vector1)
        n = len(vector1)
        maxsofar = (0, 0, 0)
        for i in range(n):
            for j in range(i+1, n+1):
                total = 0
                for k in range(i,j):
                    total += vector1[k]
                if total > maxsofar[0]:
                    maxsofar = (total, i, j)
        return f"QuadraticHandler: Sum is equal to {maxsofar}"     

class LinearHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        list1 = [31,-41,59,26,-53,58,97,-93,-23,84] 
        vector1 = np.array(list1)
        print("Vector: ", vector1)
        n = len(vector1)
        maxsofar = (0, 0, 0)
        maxhere = (0, 0)
        for i in range(1, n+1):
            if maxhere[0] + vector1[i-1] > 0:
                maxhere = (maxhere[0] + vector1[i-1], maxhere[1])
            else:
                maxhere = (0, i)
            if maxhere[0] > maxsofar[0]:
                maxsofar = (maxhere[0], maxhere[1], i)
        return f"LinearHandler: Sum is equal to {maxsofar}"
    
def client_code(handler: Handler) -> None:
    list1 = [31,-41,59,26,-53,58,97,-93,-23,84] 
    vector1 = np.array(list1)
    result = handler.handle(vector1)
    if result:
      print(f"  {result}", end="")
    else:
      print(f"  {vector1} was left untouched.", end="")

if __name__ == "__main__":
    quadratic = QuadraticHandler()
    linear = LinearHandler()

    start = time.time()
    client_code(quadratic)
    quadratic.set_next(linear)

    end = time.time()
    time = end-start
    if time < 0.0030: 
      print("\n Zmiana algorytmu ")
      client_code(linear)
