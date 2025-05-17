import tkinter
from tkinter import *

window = Tk()

window.title("Miles to Kilometers Converter")
window.minsize(width = 400, height = 100)
window.config(padx =20, pady = 20)

#Entry
entry = Entry(width = 20)
entry.grid(column = 1, row = 0)



#label
miles_label = Label(text ="Miles", font = ("Arial" ,14,))
miles_label.grid(column = 2, row = 0)

other_label = Label(text = "is equal to", font  = ("Arial", 14))
other_label.grid(column = 0, row = 1)

result_label =Label(text = "")
result_label.grid(column = 1, row = 1)

km_label = Label(text = "Km", font = ("Arial", 14))
km_label.grid(column = 2, row =1)

#Button
def calculate():
    result = float(entry.get())
    result *= 1.609344
    result_label.config(text =f"{result}")
button = Button(text="Calculate", command = calculate)
button.grid(column =1, row = 2)

tkinter.mainloop()