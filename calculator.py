from tkinter import *

root = Tk()
root.title("Calculator")
root.iconbitmap('calculator.ico')

e = Entry(root, width=50, borderwidth=5, textvariable=1)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipady=3)


def button_click(number):
    e.insert(END, number)


def button_decimal():
    e.insert(END, ".")


def button_add():
    global f_num
    global math
    math = "addition"
    f_num = float(e.get())
    e.delete(0, END)


def button_subtract():
    global f_num
    global math
    math = "subtraction"
    f_num = float(e.get())
    e.delete(0, END)


def button_multiply():
    global f_num
    global math
    math = "multiplication"
    f_num = float(e.get())
    e.delete(0, END)


def button_divide():
    global f_num
    global math
    math = "division"
    f_num = float(e.get())
    e.delete(0, END)


def button_total():
    s_num = float(e.get())
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + s_num)
    elif math == "subtraction":
        e.insert(0, f_num - s_num)
    elif math == "multiplication":
        e.insert(0, f_num * s_num)
    elif math == "division":
        e.insert(0, f_num / s_num)


def button_invert():
    number = float(e.get())
    e.delete(0, END)
    e.insert(0, number * -1)


def button_clear():
    e.delete(0, END)


def button_backspace():
    text = e.get()[:-1]
    e.delete(0, END)
    e.insert(0, text)


# Create buttons
button_1 = Button(root, text=1, padx=40, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(root, text=2, padx=40, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(root, text=3, padx=40, pady=20,
                  command=lambda: button_click(3))
button_4 = Button(root, text=4, padx=40, pady=20,
                  command=lambda: button_click(4))
button_5 = Button(root, text=5, padx=40, pady=20,
                  command=lambda: button_click(5))
button_6 = Button(root, text=6, padx=40, pady=20,
                  command=lambda: button_click(6))
button_7 = Button(root, text=7, padx=40, pady=20,
                  command=lambda: button_click(7))
button_8 = Button(root, text=8, padx=40, pady=20,
                  command=lambda: button_click(8))
button_9 = Button(root, text=9, padx=40, pady=20,
                  command=lambda: button_click(9))
button_0 = Button(root, text=0, padx=40, pady=20,
                  command=lambda: button_click(0))
button_dec = Button(root, text=str("."), padx=41.5, pady=20,
                    command=lambda: button_decimal())

button_plus = Button(root, text=str("+"), padx=39, pady=20,
                     command=lambda: button_add())
button_subt = Button(root, text=str("-"), padx=39, pady=20,
                     command=lambda: button_subtract())
button_mult = Button(root, text=str("*"), padx=39, pady=20,
                     command=lambda: button_multiply())
button_div = Button(root, text=str("\\"), padx=37, pady=20,
                    command=lambda: button_divide())
button_tot = Button(root, text=str("="), padx=37, pady=20,
                    command=lambda: button_total())

button_inv = Button(root, text=str("+/-"), padx=34, pady=20,
                    command=lambda: button_invert())
button_clr = Button(root, text=str("Clear"), padx=77, pady=20,
                    command=lambda: button_clear())
button_bksp = Button(root, text=str("Bkspc"), padx=28, pady=20,
                     command=lambda: button_backspace())

# Place buttons
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_mult.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_subt.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_plus.grid(row=4, column=3)

button_inv.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_dec.grid(row=5, column=2)
button_tot.grid(row=5, column=3)

button_clr.grid(row=1, column=0, columnspan=2)
button_bksp.grid(row=1, column=2)
button_div.grid(row=1, column=3)


root.mainloop()
