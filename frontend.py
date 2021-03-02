from tkinter import *
import backend as bk

window = Tk()

Grid.rowconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 0, weight=1)
Grid.rowconfigure(window, 1, weight=1)

l1 = Label(window, text="Title")
l1.grid(row=0, column=0, sticky="NSEW")

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=3)

e3_value = StringVar()
e3 = Entry(window, textvariable=e3_value)
e3.grid(row=1, column=1)

e4_value = StringVar()
e4 = Entry(window, textvariable=e4_value)
e4.grid(row=1, column=3)

b1 = Button(window, text="View All", width=12)
b1.grid(row=2, column=3, sticky="EW")
b2 = Button(window, text="Search Entry", width=12)
b2.grid(row=3, column=3, sticky="EW")
b3 = Button(window, text="Add Entry", width=12)
b3.grid(row=4, column=3, sticky="EW")
b4 = Button(window, text="Update", width=12)
b4.grid(row=5, column=3, sticky="EW")
b5 = Button(window, text="Delete", width=12)
b5.grid(row=6, column=3, sticky="EW")
b6 = Button(window, text="Close", command=window.quit, width=12)
b6.grid(row=7, column=3, sticky="EW")
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2, sticky="NSEW")

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6, sticky="NS")
window.mainloop()
