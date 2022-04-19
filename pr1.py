from sqlite3 import *

con=None

try:
	con=connect("mihir.db")
	print("connected")
	sql="create table student(rno int primary key,name text,marks int)"
	cursor=con.cursor()
	cursor.execute(sql)
	print("table created")
except Exception as e:
	print("issue",e)
finally:
	if con is not None:
		con.close()
		print("disconnected")