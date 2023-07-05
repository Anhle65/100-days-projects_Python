from tkinter import *
window1 = Tk()
# window1.minsize(width=100, height=150)
window1.title('Mile to Km Converter')
window1.config(padx=30, pady=30)
label = Label()
label.config(text='Miles')
label.grid(row=0, column=2)

def converted():
    miles = float(entry.get())
    km = miles * 1.689
    result.config(text=f'{km}')

entry = Entry(width=7)
entry.get()
entry.grid(row=0, column=1)

label1 = Label()
label1.config(text='is equal to')
label1.grid(row=1, column=0)

label2 = Label()
label2.config(text='Km')
label2.grid(row=1, column=2)

result = Label()
result.grid(row=1, column=1)

button = Button(text="Calculate", command=converted)
button.grid(row=2, column=1)












window1.mainloop()