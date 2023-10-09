import time
from tkinter import *
import os
# import pyglet


# pyglet.font.add_file('DJB_Get_Digital.ttf')
# action_man = pyglet.font.load('DJB Get Digital')

# Mastering
master = Tk()
master.config(background="cyan")
master.title("Calculator By Punyam Chauhan")
master.resizable(False,False)

operators = ["+","-","×","÷"]


# Creating Widgets
entry = Label(master,text="0" ,padx = 0, pady=0 ,font=("DJB Get Digital", 33),width=14, anchor=E, bg="#03befc", fg = "#151324" , borderwidth=2)

# Commands

def inno(no):
    if str( entry.cget("text")) == "INVALID INPUT" or str( entry.cget("text")) == "NOT DEFINED" :
        entry.config(text="")

    if str( entry.cget("text")) == "0":
        entry.config(text="")
        en = str( entry.cget("text") ) + str(no)
        entry.config(text=en)
    else:
        en = str( entry.cget("text") ) + str(no)
        entry.config(text=en)

def opt(oo):
    if str( entry.cget("text")) == "INVALID INPUT" or str( entry.cget("text")) == "NOT DEFINED":
        entry.config(text="0")
    if str( entry.cget("text") )[-1] == str(oo):
        pass
    else:
        on = str( entry.cget("text") ) + str(oo)
        entry.config(text=on)

def pnt(dd):
    if str( entry.cget("text")) == "INVALID INPUT" or str( entry.cget("text")) == "NOT DEFINED":
        entry.config(text="0")
    tteexxtt = str( entry.cget("text") )    
    if str( entry.cget("text") )[-1] == str(dd):
        pass

    elif any(i in tteexxtt for i in operators):
        for j,i in enumerate(reversed(str( tteexxtt ))):
            if i in operators:
                ab=j
                break
        bb = ((ab+1)*(-1))
        cc = (tteexxtt[bb:])
        if "." not in  cc:
            on = str( entry.cget("text") ) + str(dd)
            entry.config(text=on)
        else:
            pass

    elif "." in str( entry.cget("text") ):
        pass   

    else:
        on = str( entry.cget("text") ) + str(dd)
        entry.config(text=on)

def solve():
    tt = str (entry.cget("text"))
    if ")" in tt and "(" not in tt:
        tt = tt.replace(")","")
    elif "(" in tt and ")" not in tt:
        tt = tt.replace("(","")

    tt = tt.replace("²","**2")
    tt = tt.replace("×","*")
    tt = tt.replace("÷","/")
    try:
        result = eval(tt)
        result = round(result,3)
        if str(result)[-2:] ==".0": 
            result = int(str(result)[:-2])
        entry.config(text=result)
    except ZeroDivisionError:
        entry.config(text="NOT DEFINED")
    except:
        entry.config(text="INVALID INPUT")
    

def unroot_solve():
    if str( entry.cget("text")) == "INVALID INPUT" or str( entry.cget("text")) == "NOT DEFINED":
        entry.config(text="0")
    else:
        tt = str (entry.cget("text"))
        tt = tt.replace("²","**2")
        tt = tt.replace("×","*")
        tt = tt.replace("÷","/")
        try:
            result = eval(tt)
            result=result**(1/2)
            result = round(result,3)
            if str(result)[-2:] ==".0": 
                result = int(str(result)[:-2])
        except ZeroDivisionError:
            result= ("NOT DEFINED")
        except:
            tt = str (entry.cget("text"))
            result = ("INVALID INPUT")
        
        entry.config(text=result)    



def clearr():
    entry.config(text="0")

def backspace():
    a = str (entry.cget("text"))
    if a == "NOT DEFINED" or a == "INVALID INPUT":
        entry.config(text="0")
    else:
        if a[-2:] == "²":
            a= a[:-2]
        else:
            a= a[:-1]

        if len(a) !=0:
            entry.config(text=a)
        else:
            entry.config(text="0")

buffer = Label(master,text="  ", pady=5 , bg="cyan",font=("calibri", 3))



brac_o = Button(master, text="(", padx=17 , pady=0 ,font=("Calibri", 20 , "bold"), border=0 , background="#00d9ff", width= 2 , command=lambda: inno("("))
brac_c = Button(master, text=")", padx=17 , pady=0 ,font=("Calibri", 20 , "bold"), borderwidth=0 , background="#00d9ff",width= 2 , command=lambda: inno(")"))
unrt = Button(master, text="√", padx=17 , pady=0 ,font=("Swis721 Hv BT", 20), borderwidth=0 , background="#00d9ff",width= 2 , command=unroot_solve)


b1 = Button(master, text="1", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), border=0 , background="#00d9ff", width= 2 , command=lambda: inno(1))
b2 = Button(master, text="2", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), borderwidth=0 , background="#00d9ff",width= 2 , command=lambda: inno(2))
b3 = Button(master, text="3", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), borderwidth=0 , background="#00d9ff",width= 2 , command=lambda: inno(3))


b4 = Button(master, text="4", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), border=0 , background="#00d9ff",width= 2 , command=lambda: inno(4))
b5 = Button(master, text="5", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), borderwidth=0 , background="#00d9ff",width= 2 , command=lambda: inno(5))
b6 = Button(master, text="6", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), borderwidth=0 , background="#00d9ff",width= 2 , command=lambda: inno(6))

b7 = Button(master, text="7", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), border=0 , background="#00d9ff",width= 2 , command=lambda: inno(7))
b8 = Button(master, text="8", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), borderwidth=0 , background="#00d9ff",width= 2 , command=lambda: inno(8))
b9 = Button(master, text="9", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), borderwidth=0 , background="#00d9ff",width= 2 , command=lambda: inno(9))

b0 = Button(master, text="0", padx=17 , pady=0 ,font=("Calibri", 20,"bold"), borderwidth=0 , background="#00d9ff",width= 2 , command=lambda: inno(0))
b00 = Button(master, text="00", padx=17 , pady=0 ,font=("Calibri", 20,"bold"), borderwidth=0 , background="#00d9ff",width= 2 , command=lambda: inno("00"))
b_dot = Button(master, text=".", padx=17 , pady=0 ,font=("Calibri", 20,"bold"), borderwidth=0 , background="#00d9ff",width= 2 , command=lambda: pnt("."))


exp = Button(master, text="x²", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), borderwidth=0 , background="#04b0cf",width= 2 , command=lambda: opt('²'))
plu = Button(master, text="+", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), borderwidth=0 , background="#04b0cf",width= 2 , command=lambda: inno('+'))

div =  Button(master, text="÷", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), borderwidth=0 , background="#04b0cf",width= 2 , command=lambda: opt('÷'))
mul =  Button(master, text="×", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), borderwidth=0 , background="#04b0cf",width= 2 , command=lambda: opt('×'))
min_ =  Button(master, text="-", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), borderwidth=0 , background="#04b0cf",width= 2 , command=lambda: inno('-'))
equal =  Button(master, text="=", padx=10 , pady=21 ,font=("Berlin Sans FB", 30), borderwidth=0 , background="#2e88d1",width= 2, height=1 , command=solve)


bs = Button(master, text="🠔", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), border=0 , background="#04b0cf", width= 2 , command= backspace)
c = Button(master, text="C", padx=17 , pady=0 ,font=("Berlin Sans FB", 20), borderwidth=0 , background="#04b0cf",width= 2 , command=clearr)


# plaacing them
entry.grid(row=0,column=0, columnspan=4)
buffer.grid(row=1,column=0)

b1.grid(row=6,column=0,pady=3)
b2.grid(row=6,column=1,pady=3)
b3.grid(row=6,column=2,pady=3)

b4.grid(row=5,column=0,pady=3)
b5.grid(row=5,column=1,pady=3)
b6.grid(row=5,column=2,pady=3)

b7.grid(row=4,column=0,pady=3)
b8.grid(row=4,column=1,pady=3)
b9.grid(row=4,column=2,pady=3)

bs.grid(row=2,column=1,pady=3)
c.grid(row=2,column=0,pady=3)
exp.grid(row=2,column=2,pady=3)
plu.grid(row=2,column=3,pady=3)


brac_o.grid(row=3,column=0,pady=3)
brac_c.grid(row=3,column=1,pady=3)
unrt.grid(row=3,column=2,pady=3)


b0.grid(row=7,column=0,pady=3)
b00.grid(row=7,column=1,pady=3)
b_dot.grid(row=7,column=2,pady=3)


div.grid(row=3,column=3,pady=3)
mul.grid(row=4,column=3,pady=3)
min_.grid(row=5,column=3,pady=3)
equal.grid(row=6,column=3,pady=3 , rowspan=2)


master.bind('<Return>',lambda event:solve())
master.bind('1',lambda event:inno(1))
master.bind('2',lambda event:inno(2))
master.bind('3',lambda event:inno(3))
master.bind('4',lambda event:inno(4))
master.bind('5',lambda event:inno(5))
master.bind('6',lambda event:inno(6))
master.bind('7',lambda event:inno(7))
master.bind('8',lambda event:inno(8))
master.bind('9',lambda event:inno(9))
master.bind('0',lambda event:inno(0))
master.bind('(',lambda event:inno("("))
master.bind(')',lambda event:inno(")"))
master.bind('+',lambda event:inno("+"))
master.bind('-',lambda event:inno("-"))
master.bind('.',lambda event:pnt("."))
master.bind('/',lambda event:opt("÷"))
master.bind('*',lambda event:opt("×"))
master.bind('^',lambda event:opt("²"))
master.bind('<BackSpace>',lambda event:backspace())
master.bind('<Escape>',lambda event:clearr())


master.iconbitmap('ico.ico')

mainloop()

# 185 lines of code