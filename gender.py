from tkinter import *


root = Tk()
root.geometry("300x300")
root.title("GENDER GUI")

gender = StringVar()

# method displaying gender
def selected_gender():
    if len(gender.get()) != 0:
        sg.config(text="You are: "+gender.get())
    else:
        sg.config(text="Gender not selected")
    
    
# gender label
gender_label = Label(text="Select your Gender")
gender_label.pack()

# radio buttons
male = Radiobutton(root, text="Male", variable=gender, value="Male")
male.pack()
female = Radiobutton(root, text="Female", variable=gender, value="Female")
female.pack()

# submit button
btn = Button(text="Submit", command=selected_gender)
btn.pack()

#label displaying gender after submission
sg = Label(root)
sg.pack()

root.mainloop()
