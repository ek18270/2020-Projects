from tkinter import *

app = Tk()
app.title("Weight Counter")
frame_name=Frame(app)

label_first=Label(frame_name,text="Name")
label_second=Label(frame_name,text="Date")
label_third=Label(frame_name,text="Weight")

entry_first=Entry(frame_name)
entry_second=Entry(frame_name)
entry_third=Entry(frame_name)

button_submit_name=Button(frame_name, text="   Submit   ")

label_first.grid(row=0, column=0)
label_second.grid(row=1, column=0)
label_third.grid(row=2, column=0)

entry_first.grid(row=0, column=1)
entry_second.grid(row=1, column=1)
entry_third.grid(row=2, column=1)

button_submit_name.grid(row=3, columnspan=2)

frame_name.grid(row=0, column=0)
app.mainloop()
