import sqlite3
import subprocess as sp 

def create_table():
	conn = sqlite3.connect('testdb2.sqlite')

	cursor = conn.cursor()

	query = '''
	    CREATE TABLE IF NOT EXISTS student(
	    	id INTEGER PRIMARY KEY, 
	    	roll INTEGER, 
	    	name TEXT,
	        phone TEXT
	    )
	'''

	cursor.execute(query)

	conn.commit()
	conn.close()

def add_student(roll,name,phone):
	conn = sqlite3.connect('testdb2.sqlite')

	cursor = conn.cursor()

	query = '''
	    INSERT INTO student( roll, name, phone )
	    	        VALUES ( ?,?,? )
	'''

	cursor.execute(query,(roll,name,phone))

	conn.commit()
	conn.close()


def get_students():
	conn = sqlite3.connect('testdb2.sqlite')

	cursor = conn.cursor()

	query = '''
	    SELECT roll, name, phone
	    FROM student
	'''

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows

def update_student(roll,name,phone):
	conn = sqlite3.connect('testdb2.sqlite')

	cursor = conn.cursor()

	query = '''
	    UPDATE student
	    SET name = ?, phone = ?
	    WHERE roll = ?
	'''

	cursor.execute(query,(name,phone,roll))

	conn.commit()
	conn.close()


def delete_student(roll):
	conn = sqlite3.connect('testdb2.sqlite')

	cursor = conn.cursor()

	query = '''
	    DELETE
	    FROM student
	    WHERE roll = {}
	''' .format(roll)

	cursor.execute(query)
	all_rows = cursor.fetchall()

	conn.commit()
	conn.close()

	return all_rows



create_table()
