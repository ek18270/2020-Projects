import tkinter as tk
import tkinter.font as font

def main ():
    root = tk.Tk()
    root.title("Welcome Page Interface")
    root.minsize(width = 500, height = 500)
    root.maxsize(width = 500, height = 500)

    myfont = font.Font(family='Helvetica')

    button2 = tk.Label(root, font = myfont, text = "Welcome To Your Menu Planner", width = 150, height = 10, relief=tk.RAISED, bg='Steelblue', fg='White')
    button2.pack(padx = 1, pady = 50 )

    username_frame = tk.Frame(root)
    label = tk.Label(username_frame, text="Username")
    label.pack(side=tk.LEFT)
    button3 = tk.Entry(username_frame, width = 20)
    button3.pack(side=tk.LEFT)
    username_frame.pack(padx = 10, pady = 50 )

    button4 = tk.Entry(root, width = 30)
    button4.pack(padx = 10, pady = 20 )

    button5 = tk.Button(root, text = "Continue to the next page", width = 30, height = 1)
    button5.pack(padx = 10, pady= 20 )

    root.mainloop()

if __name__ == "__main__":
    main()