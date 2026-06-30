import tkinter
from math import *
from click import globals
from pygame import pixelarray
from pickle import GLOBAL
from asyncio.mixins import _global_lock

k = 20

tk = tkinter.Tk()
tk.title("Graphler")
tk.geometry("600x670") 
tk.configure(bg="white")

lbl = tkinter.Label(text='Equation 1:', font=('Arial', 20, 'bold'), bg='white', fg='black')
lbl.place(x=10, y=10)

lbl2 = tkinter.Label(text='Equation 2:', font=('Arial', 20, 'bold'), bg='white', fg='black')
lbl2.place(x=10, y=50)

okno = tkinter.Entry(font=('Arial', 20, 'bold'), bg="#9c9cc4", fg='white', width=18)
okno.place(x=175, y=10)

okno2 = tkinter.Entry(font=('Arial', 20, 'bold'), bg="#b4db94", fg='white', width=18)
okno2.place(x=175, y=50)

canvas = tkinter.Canvas(width=450, height=450, bg='white', bd=2, relief="groove")
canvas.place(x=75, y=130)

def vykresli_vsetko():
    global k
    canvas.delete("all")  
    
    for i in range(46):
        canvas.create_line(0, 10*i, 450, 10*i, fill='#E0F7FA')
        canvas.create_line(10*i, 0, 10*i, 450, fill='#E0F7FA')
        
    canvas.create_line(225, 0, 225, 450, fill='black', width=3)
    canvas.create_line(0, 225, 450, 225, fill='black', width=3)

    rovnica1 = okno.get()
    if rovnica1 and 'x' in rovnica1:
        points1 = []
        for pixel_x in range(450):
            x = (pixel_x - 450/2) / k  
            try:
                y = eval(rovnica1)
                pixel_y = 225 - (y * k)
                if -1000 <= pixel_y <= 1500:
                    points1.append((pixel_x, pixel_y))
            except:
                continue
        
        flattened_points1 = [coord for pt in points1 for coord in pt]
        if len(flattened_points1) >= 4:
            canvas.create_line(flattened_points1, fill='red', width=3, smooth=True)

    rovnica2 = okno2.get()
    if rovnica2 and 'x' in rovnica2:
        points2 = []
        for pixel_x in range(450):
            x = (pixel_x - 450/2) / k  
            try:
                y = eval(rovnica2)
                pixel_y = 225 - (y * k)
                if -1000 <= pixel_y <= 1500:
                    points2.append((pixel_x, pixel_y))
            except:
                continue
                
        flattened_points2 = [coord for pt in points2 for coord in pt]
        if len(flattened_points2) >= 4:
            canvas.create_line(flattened_points2, fill='blue', width=3, smooth=True)

def maximum1():
    global k
    max_y = -99999
    max_x = 0
    naslo_sa = False  
    rovnica1 = okno.get()
    
    if not rovnica1:
        return

    for pixel_x in range(449): 
        try:
            x = (pixel_x - 225) / k
            aktualne_y = eval(rovnica1)
            
            x_vpravo = (pixel_x + 1 - 225) / k 
            x = x_vpravo
            y_vpravo = eval(rovnica1)
        except:
            continue
        
        if (y_vpravo < aktualne_y) and (aktualne_y > max_y):
            max_y = aktualne_y
            max_x = pixel_x 
            naslo_sa = True

    if naslo_sa and max_y != -99999:
        vykresli_x = max_x 
        vykresli_y = 225 - (max_y * k)
        canvas.create_line(vykresli_x -10000, vykresli_y, vykresli_x +100000, vykresli_y, dash = True)

def maximum2():
    global k
    max_y = -99999
    max_x = 0
    naslo_sa = False  
    rovnica2 = okno2.get()
    
    if not rovnica2:
        return

    for pixel_x in range(449): 
        try:
            x = (pixel_x - 225) / k
            aktualne_y = eval(rovnica2)
            
            x_vpravo = (pixel_x + 1 - 225) / k 
            x = x_vpravo
            y_vpravo = eval(rovnica2)
        except:
            continue
        
        if (y_vpravo < aktualne_y) and (aktualne_y > max_y):
            max_y = aktualne_y
            max_x = pixel_x 
            naslo_sa = True

    if naslo_sa and max_y != -99999:
        vykresli_x = max_x 
        vykresli_y = 225 - (max_y * k)
        canvas.create_line(vykresli_x -10000, vykresli_y, vykresli_x +100000, vykresli_y, dash = True)

def minimum1():
    global k
    min_y = 99999
    max_x = 0
    naslo_sa = False  
    rovnica1 = okno.get()
    
    if not rovnica1:
        return

    for pixel_x in range(449): 
        try:
            x = (pixel_x - 225) / k
            aktualne_y = eval(rovnica1)
            
            x_vpravo = (pixel_x + 1 - 225) / k 
            x = x_vpravo
            y_vpravo = eval(rovnica1)
        except:
            continue
        
        if (y_vpravo > aktualne_y) and (aktualne_y < min_y):
            min_y = aktualne_y
            max_x = pixel_x 
            naslo_sa = True

    if naslo_sa and min_y != -99999:
        vykresli_x = max_x 
        vykresli_y = 225 - (min_y * k)
        canvas.create_line(vykresli_x -10000, vykresli_y, vykresli_x +100000, vykresli_y, dash = True)


def minimum2():
    global k
    min_y = 99999
    max_x = 0
    naslo_sa = False  
    rovnica2 = okno2.get()
    
    if not rovnica2:
        return

    for pixel_x in range(449): 
        try:
            x = (pixel_x - 225) / k
            aktualne_y = eval(rovnica2)
            
            x_vpravo = (pixel_x + 1 - 225) / k 
            x = x_vpravo
            y_vpravo = eval(rovnica2)
        except:
            continue
        
        if (y_vpravo > aktualne_y) and (aktualne_y < min_y):
            min_y = aktualne_y
            max_x = pixel_x 
            naslo_sa = True

    if naslo_sa and min_y != -99999:
        vykresli_x = max_x 
        vykresli_y = 225 - (min_y * k)
        canvas.create_line(vykresli_x -10000, vykresli_y, vykresli_x +100000, vykresli_y, dash = True)


def priesecnik():
    global k
    rovnica1 = okno.get() 
    rovnica2 = okno2.get()
    
    if not rovnica1 or not rovnica2:
        return
    
    najmensi_rozdiel = float('inf')
    priesecnik_x = None
    priesecnik_y = None

    for pixel_x in range(450):
        x = (pixel_x - 450/2) / k
        try:
            y1 = eval(rovnica1)
            y2 = eval(rovnica2)
            rozdiel = abs(y1 - y2)
            if rozdiel < najmensi_rozdiel:
                najmensi_rozdiel = rozdiel
                priesecnik_x = pixel_x
                priesecnik_y = 225 - (y1 * k)
        except:
            continue

    if najmensi_rozdiel < 0.2 and priesecnik_x is not None and priesecnik_y is not None:
        canvas.create_oval(priesecnik_x - 5, priesecnik_y - 5, priesecnik_x + 5, priesecnik_y + 5, fill='yellow', outline="black")
        
        skutocne_x = round((priesecnik_x - 225) / k, 2)    
        skutocne_y = round((225 - priesecnik_y) / k, 2) 
        canvas.create_text(priesecnik_x, priesecnik_y - 20, text=f'[{skutocne_x};{skutocne_y}]', font=('Arial', 10, 'bold'))

def animate1(pixel_x = 0):
    global k
    if pixel_x < 450:
        x = (pixel_x - 225)/k
        try:
            rovnica2 = okno.get()
            y = eval(rovnica2)
            pixel_y = 225 - (y*k)
            canvas.create_oval(pixel_x-2,pixel_y-2, pixel_x+2, pixel_y+2, fill = 'red', outline='red')
        except:
            pass
    tk.after(5,lambda: animate2(pixel_x+1))

    

def animate2(pixel_x = 0):
    global k
    if pixel_x < 450:
        x = (pixel_x - 225)/k
        try:
            rovnica = okno2.get()
            y = eval(rovnica)
            pixel_y = 225 - (y*k)
            canvas.create_oval(pixel_x -2,pixel_y - 2, pixel_x+2, pixel_y+2, fill = 'blue', outline='blue')
        except:
            pass
    tk.after(5,lambda: animate1(pixel_x+1))


def sin_command():
    okno.insert(0, 'sin(x)')
    okno2.insert(0, 'sin(x)')

def cos_command():
    okno.insert(0, 'cos(x)')
    okno2.insert(0, 'cos(x)')

def clear():
    canvas.delete('all')
    for i in range(46):
        canvas.create_line(0, 10*i, 450, 10*i, fill='#E0F7FA')
        canvas.create_line(10*i, 0, 10*i, 450, fill='#E0F7FA')
        
    canvas.create_line(225, 0, 225, 450, fill='black', width=3)
    canvas.create_line(0, 225, 450, 225, fill='black', width=3)

btn_kresli = tkinter.Button(tk, text="Plot Graphs", font=('Arial', 12, 'bold'), bg='#A5D6A7', command=vykresli_vsetko)
btn_kresli.place(x=250, y=600)

btn_sin = tkinter.Button(tk, text='Sin()', font=('Arial', 10, 'bold'), bg='#F5F5F5', command=sin_command)
btn_sin.place(x=10, y=95)

btn_cos = tkinter.Button(tk, text='Cos()', font=('Arial', 10, 'bold'), bg='#F5F5F5', command=cos_command)
btn_cos.place(x=70, y=95)

btn_priesecnik = tkinter.Button(tk, text="Find Intercept", font=('Arial', 12, 'bold'), bg='#FFF59D', command=priesecnik)
btn_priesecnik.place(x=380, y=600)

btn_max1 = tkinter.Button(tk, text="Max1", font=('Arial', 12, 'bold'), bg='#FFF59D', command=maximum1)
btn_max1.place(x=13, y=150)

btn_max2 = tkinter.Button(tk, text="Max2", font=('Arial', 12, 'bold'), bg='#FFF59D', command=maximum2)
btn_max2.place(x=13, y=200)

btn_min1 = tkinter.Button(tk, text="Min1", font=('Arial', 12, 'bold'), bg='#FFF59D', command=minimum1)
btn_min1.place(x=13, y=250)

btn_min2 = tkinter.Button(tk, text="Min2", font=('Arial', 12, 'bold'), bg='#FFF59D', command=minimum2)
btn_min2.place(x=13, y=300)

btn_ani1 = tkinter.Button(tk, text="Ani1", font=('Arial', 12, 'bold'), bg='#FFF59D', command=animate1)
btn_ani1.place(x = 13, y= 550)

btn_ani2 = tkinter.Button(tk, text="Ani2", font=('Arial', 12, 'bold'), bg='#FFF59D', command=animate2)
btn_ani2.place(x = 13, y= 600)

btn_clear = tkinter.Button(tk, text='Clear', bg = "#E61D1D", font=('Arial', 12, 'bold'), command=clear)
btn_clear.place(x = 120, y = 600)
vykresli_vsetko()
tk.mainloop()
