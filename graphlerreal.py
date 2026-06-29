import tkinter
from math import *
from click import globals
from pygame import pixelarray

k = 20

tk = tkinter.Tk()
tk.title("Graphler")
tk.geometry("600x670")  # Slightly taller to fit buttons cleanly
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
        
    # 2. Draw Main Axes
    canvas.create_line(225, 0, 225, 450, fill='black', width=3)
    canvas.create_line(0, 225, 450, 225, fill='black', width=3)

    rovnica1 = okno.get()
    if rovnica1 and 'x' in rovnica1:
        points1 = []
        for pixel_x in range(450):
            x = (pixel_x - 450/2) / k  # Kept as 'x' so eval works
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

    # --- GRAPH 2 (Blue) ---
    rovnica2 = okno2.get()
    if rovnica2 and 'x' in rovnica2:
        points2 = []
        for pixel_x in range(450):
            x = (pixel_x - 450/2) / k  # Fixed: must use 'x' for eval to read it properly
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

def priesecnik():
    global k
    rovnica1 = okno.get()
    rovnica2 = okno2.get()
    
    najmensi_rozdiel = float('inf')
    priesecnik_x = None
    priesecnik_y = None

    for pixel_x in range(450):
        x = (pixel_x - 450/2) / k
        try:
            y1 = eval(rovnica1)
            y2 = eval(rovnica2)
            rozdiel = abs(y1-y2)
            if rozdiel < najmensi_rozdiel:
                najmensi_rozdiel = rozdiel
                priesecnik_x = pixel_x
                priesecnik_y = 225 - (y1 * k)

        except:
            continue

        if najmensi_rozdiel < 0.1 and priesecnik_y is not None:
            canvas.create_oval(priesecnik_x-5,priesecnik_y-5, priesecnik_x+5, priesecnik_y + 5, fill = 'yellow')

    skutocne_x = (priesecnik_x - 225)/ k, 2    
    skutocne_y = (priesecnik_y - 225)/ k, 2 
    canvas.create_text(priesecnik_x, priesecnik_y -20, text = f'[{skutocne_x};{skutocne_y}]', font=('Arial', 10, 'bold' ))   


def sin_command():
    okno.insert(0, 'sin(x)')
    okno2.insert(0, 'sin(x)')

def cos_command():
    okno.insert(0, 'cos(x)')
    okno2.insert(0, 'cos(x)')
    
btn_kresli = tkinter.Button(tk, text="Plot Graphs", font=('Arial', 12, 'bold'), bg='#A5D6A7', command=vykresli_vsetko)
btn_kresli.place(x=250, y=600)

btn_sin = tkinter.Button(tk, text='Sin()', font=('Arial', 10, 'bold'), bg='#F5F5F5', command=sin_command)
btn_sin.place(x=10, y=95)

btn_cos = tkinter.Button(tk, text='Cos()', font=('Arial', 10, 'bold'), bg='#F5F5F5', command=cos_command)
btn_cos.place(x=70, y=95)

btn_priesecnik = tkinter.Button(tk, text="Find Intercept", font=('Arial', 12, 'bold'), bg='#FFF59D', command= priesecnik)
btn_priesecnik.place(x=380, y=600)

vykresli_vsetko()

tk.mainloop()
