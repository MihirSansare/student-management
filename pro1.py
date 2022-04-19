from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *
import matplotlib.pyplot as plt
import requests
import bs4
from tkinter.scrolledtext import *


def f1():
	root.withdraw()
	add_st.deiconify()

def f2():
	add_st.withdraw()
	root.deiconify()

def f3():
	root.withdraw()
	view_st.deiconify()
	view_st_data.delete(1.0, END)
	con=None
	try:
		con=connect("mihir.db")
		sql="select * from student"
		cursor=con.cursor()
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data:
			info=info+"rno:"+str(d[0])+" name:"+str(d[1])+" marks:"+str(d[2])+"\n"
		view_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()

def f4():
	view_st.withdraw()
	root.deiconify()

def f5():
	con=None
	try:
		con=connect("mihir.db")
		sql="insert into student values('%d','%s','%d')"
		cursor=con.cursor()
		rno=add_st_entrno.get()
		if len(rno)!=0:
			try:
				rno=int(rno)	
				if rno>0:
					name=add_st_entname.get()
					if len(name)!=0:
						if name.isalpha()==True:
							if len(name)>1:	
								marks=add_st_entmarks.get()
								if len(marks)!=0:
									try:
										marks=int(marks)
										if marks>=0 and marks<=100:
											cursor.execute(sql %(rno,name,marks))
											con.commit()
											showinfo("Success","Record Added")
										else:
											showerror("Issue","marks should between 0-100")
									except ValueError:
										showerror("issue","marks must be in integer ")
								else:
									showerror("Issue","marks is empty")
							else:
								showerror("Issue","name should contain atleast two alphabates")
						else:
							showerror("Issue","name should contain only alphabates")
					else:
						showerror("Issue","name is empty")
				else:
					showerror("Issue","Rno should be +ve int")
			except ValueError:
				showerror("issue","roll no must be in integer ")
		else:
			showerror("Issue","rno is empty")
	except Exception as e:
		showerror("Failure",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

def f6():
	con=None

	try:
		con=connect("mihir.db")
		sql="update student set name='%s' , marks='%d' where rno='%d'"
		cursor=con.cursor()
		rno=update_st_entrno.get()
		if len(rno)!=0:
			try:
				rno=int(rno)	
				if rno>0:
					name=update_st_entname.get()
					if len(name)!=0:
						if name.isalpha()==True:
							if len(name)>1:	
								marks=update_st_entmarks.get()
								if len(marks)!=0:
									try:
										marks=int(marks)
										if marks>=0 and marks<=100:
											cursor.execute(sql%(name,marks,rno))
											if cursor.rowcount==1:
												con.commit()
												showinfo("success","record updated")
											else:
												showerror("issue","record does not exist")
										else:
											showerror("Issue","marks should between 0-100")
									except ValueError:
										showerror("issue","marks must be in integer ")
								else:
									showerror("Issue","marks is empty")
							else:
								showerror("Issue","name should contain atleast two alphabates")
						else:
							showerror("Issue","name should contain only alphabates")
					else:
						showerror("Issue","name is empty")
				else:
					showerror("Issue","Rno should be +ve int")
			except ValueError:
				showerror("issue","rno should be integer")
		else:
			showerror("Issue","rno is empty")
	except Exception as e:
		showerror("issue",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

def f7():
	update_st.withdraw()
	root.deiconify()

def f8():
	root.withdraw()
	update_st.deiconify()

def f9():
	try:
		con=connect("mihir.db")
		sql="delete from student where rno='%d'"
		cursor=con.cursor()
		rno=delete_st_entrno.get()
		if len(rno)!=0:
			try:
				rno=int(rno)
				cursor.execute(sql%(rno))
				if cursor.rowcount==1:
					con.commit()
					showinfo("success","record deleted")
				else:
					showerror("issue","record does not exist")
			except ValueError:
				showerror("issue","rno should be integer only")
		else:
			showerror("issue","rno is empty")
	except Exception as e:
		showerror("issue",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

def f10():
	delete_st.withdraw()
	root.deiconify()

def f11():
	root.withdraw()
	delete_st.deiconify()

def f12():
	con=None
	try:
		con=connect("mihir.db")
		sql="select * from student"
		cursor=con.cursor()
		cursor.execute(sql)
		data=cursor.fetchone()
		name=[]
		marks=[]
		
		while data:
			name.append(data[1])
			marks.append(data[2])
			data=cursor.fetchone()

	except Exception as e:
		showerror("issue",e)

	
	my_colors=['red','green','blue']
	plt.bar(name,marks,color=my_colors)
	
	
	
	plt.title("Batch Information")
	plt.xlabel("name")
	plt.ylabel("Marks")
	
	plt.show()
		
			

#quotes

try:
	web_add="https://www.brainyquote.com/quote_of_the_day"
	res=requests.get(web_add)
	data=bs4.BeautifulSoup(res.text,"html.parser")
	info=data.find('img',{"class":"p-qotd"})
	quote=info['alt']
except Exception as e:
	print("issue",e)

#loc
try:
	web_address="https://ipinfo.io/"
	res=requests.get(web_address)
	data=res.json()	
	city=data['city']
except Exception as e:
	print("issue",e)

#temp

try:
	a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q="+ city
	a3="&appid=c6e315d09197cec231495138183954bd"
	web_address=a1+a2+a3
	res=requests.get(web_address)
	data=res.json()
	t=data['main']['temp']
except Exception as e:
	print("issue",e)





root=Tk()
root.title("S.M.S.")
root.geometry("700x500+600+300")
root.configure(bg='light blue')

btnAdd=Button(root,text="Add",font=('arial',17,'bold'),width=10,bg='light grey',command=f1)
btnView=Button(root,text="View",font=('arial',17,'bold'),width=10,bg='light grey',command=f3)
btnUpdate=Button(root,text="Update",font=('arial',17,'bold'),width=10,bg='light grey',command=f8)
btnDel=Button(root,text="Delete",font=('arial',17,'bold'),width=10,bg='light grey',command=f11)
btnChart=Button(root,text="Charts",font=('arial',17,'bold'),width=10,bg='light grey',command=f12)

btnAdd.pack(pady=5)
btnView.pack(pady=5)
btnUpdate.pack(pady=5)
btnDel.pack(pady=5)
btnChart.pack(pady=5)

lblLoc=Label(root,text="Location:",font=('arial',17,'bold'),bg='light blue')
lblTemp=Label(root,text="Temp:",font=('arial',17,'bold'),bg='light blue')
lblQOTD=Label(root,text="QOTD:",font=('arial',17,'bold'),bg='light blue')
lblq=Label(root,text=quote,wraplength=500,font=('arial',17,'bold','italic'),bg='light blue')
lblCity=Label(root,text=city,font=('Times new Roman',17,'bold'),bg='light blue')
lblt=Label(root,text=t,font=('Times new Roman',17,'bold'),bg='light blue')

lblLoc.place(x=0,y=320)
lblCity.place(x=140,y=320)
lblTemp.place(x=500,y=320)
lblt.place(x=600,y=320)
lblQOTD.place(x=0,y=400)
lblq.place(x=100,y=400)


add_st=Toplevel(root)
add_st.title("Add stu")
add_st.geometry("600x600+600+300")
add_st.configure(bg='dark cyan')

add_st_lblrno=Label(add_st,text='enter rno',font=('arial',20,'bold'),bg='dark cyan')
add_st_entrno=Entry(add_st,font=('arial',20,'bold'))
add_st_lblname=Label(add_st,text='enter name',font=('arial',20,'bold'),bg='dark cyan')
add_st_entname=Entry(add_st,font=('arial',20,'bold'))
add_st_lblmarks=Label(add_st,text='enter marks',font=('arial',20,'bold'),bg='dark cyan')
add_st_entmarks=Entry(add_st,font=('arial',20,'bold'))
add_st_btnsave=Button(add_st,text='Save',font=('arial',20,'bold'),width=10,bg='light grey',command=f5)
add_st_btnback=Button(add_st,text='Back',font=('arial',20,'bold'),width=10,bg='light grey',command=f2)

add_st_lblrno.pack(pady=10)
add_st_entrno.pack(pady=10)
add_st_lblname.pack(pady=10)
add_st_entname.pack(pady=10)
add_st_lblmarks.pack(pady=10)
add_st_entmarks.pack(pady=10)
add_st_btnsave.pack(pady=10)
add_st_btnback.pack(pady=10)

add_st.withdraw()


view_st=Toplevel(root)
view_st.title("View stu")
view_st.geometry("600x600+600+300")
view_st.configure(bg='#fff9d0')

view_st_data=ScrolledText(view_st,width=28,height=10,font=('arial',20,'bold'),bg='#fff9d0')
view_st_btnback=Button(view_st,text="Back",font=('arial',20,'bold'),width=10,bg='light grey',command=f4)

view_st_data.pack(pady=10)
view_st_btnback.pack(pady=10)
view_st.withdraw()


update_st=Toplevel(root)
update_st.title("Update stu")
update_st.geometry("600x600+600+300")
update_st.configure(bg='light pink')

update_st_lblrno=Label(update_st,text='enter rno',font=('arial',20,'bold'),bg='light pink')
update_st_entrno=Entry(update_st,font=('arial',20,'bold'))
update_st_lblname=Label(update_st,text='enter name',font=('arial',20,'bold'),bg='light pink')
update_st_entname=Entry(update_st,font=('arial',20,'bold'))
update_st_lblmarks=Label(update_st,text='enter marks',font=('arial',20,'bold'),bg='light pink')
update_st_entmarks=Entry(update_st,font=('arial',20,'bold'))
update_st_btnsave=Button(update_st,text='Save',font=('arial',20,'bold'),width=10,bg='light grey',command=f6)
update_st_btnback=Button(update_st,text='Back',font=('arial',20,'bold'),width=10,bg='light grey',command=f7)

update_st_lblrno.pack(pady=10)
update_st_entrno.pack(pady=10)
update_st_lblname.pack(pady=10)
update_st_entname.pack(pady=10)
update_st_lblmarks.pack(pady=10)
update_st_entmarks.pack(pady=10)
update_st_btnsave.pack(pady=10)
update_st_btnback.pack(pady=10)

update_st.withdraw()

delete_st=Toplevel(root)
delete_st.title("delete stu")
delete_st.geometry("600x600+600+300")
delete_st.configure(bg='light green')

delete_st_lblrno=Label(delete_st,text='enter rno',font=('arial',20,'bold'),bg='light green')
delete_st_entrno=Entry(delete_st,font=('arial',20,'bold'))

delete_st_btndelete=Button(delete_st,text='Delete',font=('arial',20,'bold'),width=10,bg='light grey',command=f9)
delete_st_btnback=Button(delete_st,text='Back',font=('arial',20,'bold'),width=10,bg='light grey',command=f10)

delete_st_lblrno.pack(pady=10)
delete_st_entrno.pack(pady=10)


delete_st_btndelete.pack(pady=10)
delete_st_btnback.pack(pady=10)

delete_st.withdraw()













root.mainloop()
