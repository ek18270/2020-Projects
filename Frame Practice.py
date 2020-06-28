from tkinter import *

root = Tk()
root.geometry('600x500')
root.title('Menu Planner')
#root.iconbitmap()

def createNewWindow():
    newWindow = Toplevel(root)
    labelExample = Label(newWindow, text = "New Window")
    buttonExample = Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()


frame1 = Frame(root, width=600, height=500, background="bisque")

frame1.pack(fill=None, expand=False)


listbox = Listbox(root)
#listbox.append(object)
#print=("listbox")
listbox.place(relx = 0.3, rely = 0.1, anchor = NE)


listbox2 = Listbox(root)

def moveDown():

    move_text = listbox.selection_get()
    curindex = int(listbox.curselection()[0])
    listbox.delete(curindex)
    listbox2.insert(END, move_text)

moveBtn = Button(root, text=">", command=moveDown)
moveBtn.place(relx = 0.3, rely = 0.1, anchor = CENTER)


listbox2.place(relx = 0.5, rely = 0.5, anchor = NW)

for item in ["Chicken", "Beef", "Fish", "Pork"]:
    listbox.insert(END, item)

root.mainloop()