from database import *
from command import *
#C CREATE R READ U UPADTE D DELETE
cd_adddata = Add_data()
cd_updatedata = Update_data()
cd_deletedata = Delete_data()


def add_data(id_,name,phone):
	add_student(id_,name,phone)

def update_data(id_,name,phone):
	update_student(id_,name,phone)

def delete_data(id_):
	delete_student(id_)

def get_data():
	return get_students()

def show_data():
	students = get_data()
	for student in students:
		print(student)

def select():
	sp.call('clear',shell=True)
	sel = input("1.Add data\n2.Show Data\n3.Update\n4.Delete\n5.Exit\n\n")
	
	if sel=='1':
		sp.call('clear',shell=True)
		data = {}
		data["id"] = int(input('id: '))
		data["name"] = input('Name: ')
		data["phone"] = input('phone: ')
		cd_adddata.process(data)
	
	elif sel=='2':
		sp.call('clear',shell=True)
		show_data()
		input("\n\npress enter to back:")
	
	elif sel=='3':
		sp.call('clear',shell=True)
		data = {}
		data["id"] = int(input('Enter Id: '))
		print()
		data["name"] = input('Name: ')
		data["phone"] = input('phone: ')
		cd_updatedata.process(data)
		input("\n\nYour data has been updated \npress enter to back:")

	elif sel=='4':
		sp.call('clear',shell=True)
		data = {}
		data["id"] = int(input('Enter Id: '))
		cd_deletedata.process(data)
		input("\n\nYour data has been deleted \npress enter to back:")
	else:
		return 0
	return 1

while(select()):
	pass 
