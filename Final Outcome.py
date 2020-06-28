from tkinter import *

root = Tk()
root.geometry("500x500")


frame1 = Frame(root, background="lightsteelblue")
frame1.pack(fill="both", expand="True")

frame = Frame(frame1, height=900, width=160, padx=20, pady=10)
frame2 = Frame(frame1, height=900, width=160, padx=20, pady=10)
frame.pack(fill='y', anchor=NW)
frame2.pack(padx=10, pady=50, fill='y', anchor=CENTER)

# b2 = Button(frame2, text="Here")
# b2.pack()


listbox = Listbox(frame, height=100, width=20)
# listbox.append(object)
# print=("listbox")
listbox.place(relx=-0.1, rely=0)

listbox2 = Listbox(frame1)


def moveDown():
    move_text = listbox.selection_get()
    curindex = int(listbox.curselection()[0])
    listbox.delete(curindex)
    listbox2.insert(END, move_text)


moveBtn = Button(frame, text=">", command=moveDown)
moveBtn.place(relx=1, rely=0)

listbox2.place(relx=0.5, rely=0.5, anchor=NW)

for item in ["Chicken", "Beef", "Fish", "Pork", "Turkey", "Quil", "Duck", "Eggs", "Nuts", "Yogurt", ]:
    listbox.insert(END, item)


def moveDown():
    move_text = listbox2.selection_get()
    curindex = int(listbox2.curselection()[0])
    listbox2.delete(curindex)
    listbox.insert(END, move_text)


moveBtn2 = Button(frame, text="<", command=moveDown)
moveBtn2.place(relx=1, rely=0.1)

root.mainloop()
