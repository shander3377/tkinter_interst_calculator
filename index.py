from tkinter import *

def calculate():
    p =float(principal.get())
    r =float(rate.get())
    t =float(time.get())
    si = (p*r*t)/100
    interest=round(si, 2)
    text="Your simple interst would be "+str(si)
    show =Label(result_Frame, text=text, bg="cyan", font=("sans-serif", 12))
    show.place(x=20, y=20)
    show.pack()

window = Tk()
window.title("Simple Interest Calculator")
window.geometry("400x600")
window.configure(bg="cyan")

heading = Label(window, text="Calculate Simple Interest!", fg="red", bg="cyan", font=("sans-serif", 20))
heading.place(x=40, y=20)

principalLabel = Label(window, text="Principal: ", fg="red", bg="cyan", font=("sans-serif", 12))
principalLabel.place(x= 20, y=70)
principal = Entry(window, text="", bd=2, width=22)
principal.place(x=100, y=70)

rateLabel = Label(window, text="Rate: ", fg="red", bg="cyan", font=("sans-serif", 12))
rateLabel.place(x= 20, y=90)
rate = Entry(window, text="", bd=2, width=22)
rate.place(x=100, y=90)

timeLabel = Label(window, text="Time: ", fg="red", bg="cyan", font=("sans-serif", 12))
timeLabel.place(x= 20, y=110)
time = Entry(window, text="", bd=2, width=22)
time.place(x=100, y=110)

calculateButton = Button(window, text="Calculate!", fg="cyan", bg="red", bd=4, command=calculate)
calculateButton.place(x=100, y=130)

result_Frame = LabelFrame(window, text="Result", bg="grey", font=("sans-serif", 12))
result_Frame.pack(padx=20, pady= 20)
result_Frame.place(x=100, y=150)

window.mainloop()
