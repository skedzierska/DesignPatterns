from database import *
from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def process(self,data):
        pass

class Add_data(Command):

    def process(self, data):
        id_ = data["id"]
        name = data["name"]
        phone = data["phone"]
        add_student(id_,name,phone)

class Update_data(Command):
    def process(self, data):
        id_ = data["id"]
        name = data["name"]
        phone = data["phone"]
        update_student(id_,name,phone)

class Delete_data(Command):
    def process(self, data):
        id_ = data["id"]
        delete_student(id_)



