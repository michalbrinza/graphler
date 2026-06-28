import tkinter
from math import *

k = 20

tk = tkinter.Tk()
tk.title("Graphler ")
tk.geometry("600x600")
tk.configure(bg = "white")

lbl = tkinter.Label(text = 'Equation:', font=('Arial', 20, 'bold'), bg = 'red')
lbl.pack(pady=(15, 2))
lbl.place(relx = 0.15, rely=0.1, anchor='center')

okno = tkinter.Entry(font=('Arial', 20, 'bold'), bg = 'blue4', width = '18',)
okno.pack(pady = 42)

canvas = tkinter.Canvas(width = 450, height=450)
canvas.pack()

def graf():
    global k
    
    #grid
    for i in range(80):
        canvas.create_line(0,10*i, 450,10*i, fill='blue')
        canvas.create_line(10*i,0,10*i,450)
       #xy osa
    y_osa = canvas.create_line(225,0,225,450,fill ='black', width = 3)
    x_osa = canvas.create_line(0,225,450,225,fill='black', width=3)


    rovnica =  okno.get()
    if 'x' not in rovnica:
        canvas.create_text( 225,225,text = 'Not valid, use x', font='Arial 35 ')



graf()
tk.mainloop()