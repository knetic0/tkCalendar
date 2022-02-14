import calendar
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import datetime

root = Tk()
root.geometry('500x500')
root.title('Calendar')


def Cal():
	global choices
	global result
	global inpYear

	choice = calChoices.get()
	inChoices = choices.index(choice)
	inpYear = year.get()

	result = Calendar(root,selectmode='day',year = inpYear,month=inChoices,font=('Arial',13))
	result.grid(column=2,row=4,columnspan=2)

def reset():
	global choices
	global result
	global entYear

	calChoices.set('')
	year.set(0)

	result.destroy()

	choice = calChoices.get()
	inChoices = choices.index(choice)
	inpYear = year.get()

	r = calendar.month(inpYear,inChoices)

	result = Label(root,text='{}'.format(r),font=('Arial',10)).grid(column=2,row=4)

def yearCalendar():
	gui = Tk()
	#gui.geometry('650x700')
	gui.title(2022)

	year = 2022
	
	Calendar(gui,selectmode='day',year=year,month=1,font=('Arial',13)).grid(column=1,row=2,columnspan=2)
	Calendar(gui,selectmode='day',year=year,month=2,font=('Arial',13)).grid(column=3,row=2,columnspan=2)
	Calendar(gui,selectmode='day',year=year,month=3,font=('Arial',13)).grid(column=5,row=2,columnspan=2)
	Calendar(gui,selectmode='day',year=year,month=4,font=('Arial',13)).grid(column=1,row=3,columnspan=2)
	Calendar(gui,selectmode='day',year=year,month=5,font=('Arial',13)).grid(column=3,row=3,columnspan=2)
	Calendar(gui,selectmode='day',year=year,month=6,font=('Arial',13)).grid(column=5,row=3,columnspan=2)
	Calendar(gui,selectmode='day',year=year,month=7,font=('Arial',13)).grid(column=1,row=4,columnspan=2)
	Calendar(gui,selectmode='day',year=year,month=8,font=('Arial',13)).grid(column=3,row=4,columnspan=2)
	Calendar(gui,selectmode='day',year=year,month=9,font=('Arial',13)).grid(column=5,row=4,columnspan=2)
	Calendar(gui,selectmode='day',year=year,month=10,font=('Arial',13)).grid(column=1,row=5,columnspan=2)
	Calendar(gui,selectmode='day',year=year,month=11,font=('Arial',13)).grid(column=3,row=5,columnspan=2)
	Calendar(gui,selectmode='day',year=year,month=12,font=('Arial',13)).grid(column=5,row=5,columnspan=2)

	gui.mainloop()

noww = datetime.datetime.now()
Label(root,text='Now => {}'.format(noww),font=('Arial',12)).grid(row=5,column=1,columnspan=2)

Label(root,text='Enter the Year:',font=('Arial',13)).grid(column=1,row=1,columnspan=1)
year = IntVar()
entYear = Entry(root,textvariable=year,width=5)
entYear.grid(column=2,row=1,columnspan=1)

Label(root,text='Enter the Month:' + ' ',font=('Arial',13)).grid(column=1,row=2,columnspan=1)
choices = ['-----------','Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
calChoices = ttk.Combobox(root,values=choices,width=5)
calChoices.grid(column=2,row=2,columnspan=1)

Button(root,text='Submit',command=lambda:Cal(),width=10).grid(column=2,row=3,columnspan=1)

my_menu = Menu(root)
root.config(menu=my_menu)

resetMenu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='Reset',menu=resetMenu)
resetMenu.add_command(label='Reset Calendar',command=reset)

fullCalendar = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label='Calendar',menu=fullCalendar)
fullCalendar.add_command(label='2022 Calendar',command=yearCalendar)

root.mainloop()