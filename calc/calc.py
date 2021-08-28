from tkinter import *
import time
import win32gui, win32con

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)


calc=Tk()
calc.geometry("450x470")
calc.maxsize(450,470)
calc.minsize(350,350)
calc.title("Calculator")
#var declaration
start=" "
text=StringVar()



#frame
f=Frame(calc,height=800,width=800,bd=8,bg="lightgreen")
f.pack(side=TOP)
f2=Frame(calc,height=800,width=800,bd=8,bg="lightblue")
f2.pack(side=TOP)

#time
localtime=time.asctime(time.localtime(time.time()))
name=Label(f,font=("algerian",15),fg="red",text="calculator")
name.grid(row=0,column=0)
time=Label(f,font=("algerian",10),fg="purple",text=localtime)
time.grid(row=1,column=0)


#function declaration
def btnclick(num):
    global start
    if (start[-1]=='+'  or start[-1]=='-' or start[-1]=='*' or start[-1]=='/') and (num=='+' or num=='-' or num=='*' or num=='/'):
        start=start[:-1]
    start=start+str(num)
    text.set(start)
def btnclr():
    global start
    start=" "
    text.set(start)

def btneq():
    global start
    val=str(eval(start))
    text.set(val)
    start=val


#i use slicing method in this function
def backspace():
        global start
        start=start[:-1]
        text.set(start)
#button press by keyboard

def press(event):
    global start
    if (start[-1]=='+'  or start[-1]=='-' or start[-1]=='*' or start[-1]=='/') and (event.char=='+' or event.char=='-' or event.char=='*' or event.char=='/'):
        start=start[:-1]
    start=start+(event.char)
    text.set(start)

#that function i delclared for button
def equal(event):
    if(True):
        global start
        val=str(eval(start))
        text.set(val)
        start=val

#that function i delclared for keyboard

def eq(event):
        global start
        val=str(eval(start+event.char))
        text.set(val)
        start=val

def backspacing(event):
    global start
    start=start[:-1]
    text.set(start)

#entry
textbox=Entry(f2,font=("arial",15),fg="white",bd=20,textvariable=text,insertwidth=0.5,bg="steelblue",justify="left")
textbox.grid(columnspan=4)


#row work
#row1
btn1=Button(f2,font=("arial",12),fg="lightgreen",command=lambda: btnclick(1),bg="steelblue",padx=15,pady=10,bd=8,text=1)
btn1.grid(row=1,column=0)
btn2=Button(f2,font=("arial",12),fg="white",command=lambda: btnclick(2),bg="steelblue",padx=15,pady=10,bd=8,text=2)
btn2.grid(row=1,column=1)
btn3=Button(f2,font=("arial",12),fg="darkred",command=lambda: btnclick(3),bg="steelblue",padx=15,pady=10,bd=8,text=3)
btn3.grid(row=1,column=2)
bck=Button(f2,font=("arial",12),fg="black",command=lambda: backspace(),bg="steelblue",padx=12,pady=8,bd=6,text='<<')
bck.grid(row=1,column=3)
#row2
btn4=Button(f2,font=("arial",12),fg="lightgreen",command=lambda: btnclick(4),bg="steelblue",padx=15,pady=10,bd=8,text=4)
btn4.grid(row=2,column=0)
btn5=Button(f2,font=("arial",12),fg="white",command=lambda: btnclick(5),bg="steelblue",padx=15,pady=10,bd=8,text=5)
btn5.grid(row=2,column=1)
btn6=Button(f2,font=("arial",12),fg="darkred",command=lambda: btnclick(6),bg="steelblue",padx=15,pady=10,bd=8,text=6)
btn6.grid(row=2,column=2)

plus=Button(f2,font=("arial",12),fg="red",command=lambda:  btnclick('+'),bg="steelblue",padx=15,pady=10,bd=8,text="+")
plus.grid(row=2,column=3)
#row3
btn7=Button(f2,font=("arial",12),fg="lightgreen",command=lambda: btnclick(7),bg="steelblue",padx=15,pady=10,bd=8,text=7)
btn7.grid(row=3,column=0)
btn8=Button(f2,font=("arial",12),fg="white",command=lambda: btnclick(8),bg="steelblue",padx=15,pady=10,bd=8,text=8)
btn8.grid(row=3,column=1)
btn9=Button(f2,font=("arial",12),fg="darkred",command=lambda: btnclick(9),bg="steelblue",padx=15,pady=10,bd=8,text=9)
btn9.grid(row=3,column=2)
minus=Button(f2,font=("arial",12),fg="red",command=lambda: btnclick('-'),bg="steelblue",padx=15,pady=10,bd=8,text="-")
minus.grid(row=3,column=3)
#row4
btnc=Button(f2,font=("arial",12),fg="lightgreen",command=lambda: btnclr(),bg="steelblue",padx=15,pady=10,bd=8,text="C")
btnc.grid(row=4,column=0)
btn0=Button(f2,font=("arial",12),fg="white",command=lambda: btnclick(0),bg="steelblue",padx=15,pady=10,bd=8,text=0)
btn0.grid(row=4,column=1)
divide=Button(f2,font=("arial",12),fg="orange",command=lambda: btnclick('/'),bg="steelblue",padx=15,pady=10,bd=8,text="/")
divide.grid(row=4,column=2)
multiply=Button(f2,font=("arial",12),fg="red",command=lambda: btnclick('*'),bg="steelblue",padx=15,pady=10,bd=8,text="*")
multiply.grid(row=4,column=3)
#extra button
dot=Button(f2,font=("arial",12),fg="lightgreen",command=lambda: btnclick('.'),bg="steelblue",padx=15,pady=10,bd=8,text=".")
dot.grid(row=5,column=0)
btnequal=Button(f2,font=("arial",12),fg="white",command=lambda: btneq(),bg="steelblue",padx=15,pady=10,bd=8,text="=")
btnequal.grid(row=5,column=1)
ob=Button(f2,font=("arial",12),fg="purple",command=lambda: btnclick('('),bg="steelblue",padx=15,pady=10,bd=8,text="(")
ob.grid(row=5,column=2)
cb=Button(f2,font=("arial",12),fg="red",command=lambda: btnclick(')'),bg="steelblue",padx=15,pady=10,bd=8,text=")")
cb.grid(row=5,column=3)



calc.bind("1",press)
calc.bind("2",press)
calc.bind("3",press)
calc.bind("4",press)
calc.bind("5",press)
calc.bind("6",press)
calc.bind("7",press)
calc.bind("8",press)
calc.bind("9",press)
calc.bind("0",press)
calc.bind("+",press)
calc.bind("-",press)
calc.bind("*",press)
calc.bind("/",press)
calc.bind(".",press)
calc.bind("<BackSpace>",backspacing)
calc.bind("<Return>",equal)
calc.bind("<Return>",eq)



calc.mainloop()


