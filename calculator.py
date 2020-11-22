from tkinter import *
import tkinter
from tkinter.ttk import *

def btnclick(numbers):
   global operator
   operator=operator+str(numbers)
   text_Input.set(operator)

def clear():
    text_Input.set('')
    
def btnequals():
    global operator
    sum=eval(operator)
    text_Input.set(sum)
    operator=""
window=tkinter.Tk()
window.title('Calculator')

operator=""
text_Input=StringVar()
text_Display=tkinter.Label(window,font=('arial',20,'bold'),textvariable=text_Input).grid(columnspan=4)

btn1=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='1',width=3,command=lambda:btnclick(1)).grid(row=1,column=0)
btn2=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='2',width=3,command=lambda:btnclick(2)).grid(row=1,column=1)
btn3=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='3',width=3,command=lambda:btnclick(3)).grid(row=1,column=2)
mul=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='*',width=3,command=lambda:btnclick('*')).grid(row=1,column=3)

#-------------------------------------------------------------------------------------------------

btn4=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='4',width=3,command=lambda:btnclick(4)).grid(row=2,column=0)
btn5=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='5',width=3,command=lambda:btnclick(5)).grid(row=2,column=1)
btn6=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='6',width=3,command=lambda:btnclick(6)).grid(row=2,column=2)
div=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='/',width=3,command=lambda:btnclick('/')).grid(row=2,column=3)

#-----------------------------------------------------------------------------------------------

btn7=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='7',width=3,command=lambda:btnclick(7)).grid(row=3,column=0)
btn8=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='8',width=3,command=lambda:btnclick(8)).grid(row=3,column=1)
btn9=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='9',width=3,command=lambda:btnclick(9)).grid(row=3,column=2)
addition=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='+',width=3,command=lambda:btnclick('+')).grid(row=3,column=3)

#-------------------------------------------------------------------------------------------------

btn10=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='0',width=3,command=lambda:btnclick(0)).grid(row=4,column=0)
btn11=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='C',width=3,command=lambda:clear()).grid(row=4,column=1)
btn12=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='=',width=3,command=lambda:btnequals()).grid(row=4,column=2)
sub=tkinter.Button(window,fg='black',font=('arial',20,'bold'),text='-',width=3,command=lambda:btnclick('-')).grid(row=4,column=3)

window.mainloop()