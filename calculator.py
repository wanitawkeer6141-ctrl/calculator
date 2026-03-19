import tkinter as tk
from tkinter import *
from tkinter import ttk
window=tk.Tk()
window.title("app")

first_number = None

operator = None
 


display_var = tk.StringVar()
display_var.set("")



def click(num):
    c_text=display_var.get()
    display_var.set(c_text + str(num))


def clear():
    display_var.set("")

    



def operation(op):
    global first_number, operator
    try:
        first_number = float(display_var.get())
        operator = op
        display_var.set("")
    except:
        display_var.set("Error")
    

def equal():
    global first_number,operator
    

    second_number = float(display_var.get())

    if operator == '+':

            result = first_number +  second_number

    elif operator == '-':
            result = first_number - second_number
    elif operator == '/':
    
            result = first_number / second_number


    elif operator == '*':
            result = first_number * second_number
    else:
            result= second_number
    display_var.set(result)
    try:
        if operator == '/':
            result = first_number / second_number

    except:
        display_var.set("Error")


def addition():
    
    global fourth_number, number,operator,number1,number

    try:
        if operator == '+':
            result = number1 + number
             
    except:result = number1 + number
          



e=ttk.Entry(window,textvariable=display_var,width=35,font=("Bold",14),justify='right')
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10,sticky='nsew')


for i in range(4):
    window.grid_columnconfigure(i,weight=1)
for i in range(0,6):
    window.grid_rowconfigure(i,weight=1)


Button=[
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('-',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('*',3,3),
    ('0',4,0),('.',4,1),('+',4,2),
    ('C', 5, 0), ('=', 5, 1),
]
button_font=('arial',14)
for(button_text,r,c) in Button:
    if button_text =='C':
        button=tk.Button(window,text=button_text,font=button_font,padx=20,pady=20,command=clear)
        button.grid(row=r,column=c,padx=5,pady=5,sticky='nsew')


        
    
    elif button_text == '+':
        button=tk.Button(window,text=button_text, padx=20,pady=20,command=lambda op=button_text:operation(op))

        button.grid(row=r,column=c,columnspan=2,sticky='nsew')
        button.grid(row=r,column=c,columnspan=2,sticky='nsew')


    elif button_text == '/':
        button=tk.Button(window,text=button_text, padx=20,pady=20,command=lambda op=button_text: operation(op))

        button.grid(row=r,column=c,columnspan=2,sticky='nsew')



    elif button_text == '-':
        button=tk.Button(window,text=button_text, padx=20,pady=20,command=lambda op=button_text: operation(op))

        button.grid(row=r,column=c,columnspan=2,sticky='nsew')


    elif button_text == '*':
        button=tk.Button(window,text=button_text, padx=20,pady=20,command=lambda op=button_text: operation(op))

        button.grid(row=r,column=c,columnspan=2,sticky='nsew')





    elif button_text=='=':
         
        button=tk.Button(window,text=button_text, padx=20,pady=20,command=equal)
        button.grid(row=r,column=c,columnspan=3,padx=5,pady=5,sticky='nsew')
    

    else:
        button=tk.Button(window,text=button_text, padx=20,pady=20,command=lambda num=button_text:click(num))
        button.grid(row=r,column=c,sticky='nsew')

    
window.mainloop()

