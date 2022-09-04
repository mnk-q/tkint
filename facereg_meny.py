from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import json

if __name__ == '__main__':
    k = 1
    root = Tk()
    root.geometry("800x800")
    #root.grid(columnspan=1,rowspan=3)
    root.configure(bg="#FBF6F0")
    frame1 = LabelFrame(root,height=50, background="#1F4690")
    frame1.pack(side="top", fill=BOTH)
    label11 = ttk.Label(frame1, text='Face Registration', font=("Helvetica", 14), background="#1F4690", foreground="white")
    label11.pack(side=LEFT, padx=10, pady=10)

    #frame for buttons
    frame2 = Frame(root, width=600, height=300, bg="#FBF6F0")
    frame2.pack(side="top", padx=100, pady=120)
    #button 1: back
    btn1 = Button(frame2, text="BACK", height=4, width=15, bg="#1F4690", fg="white")
    #btn1.grid(row=0,column=0)
    btn1.pack(side=LEFT, pady=10, padx=10)

    #button 2:Capture
    btn2 = Button(frame2, text='CAPTURE', height=4, width=15, bg="#1F4690", fg="white")
    #btn2.grid(row=0, column=1)
    btn2.pack(side=LEFT, pady=10, padx=10)

    # button 3:Update
    btn3 = Button(frame2, text='UPDATE', height=4, width=15, bg="#1F4690", fg="white")
    btn3.pack(side=LEFT, pady=10, padx=10)

    # button 4:Delete
    btn4 = Button(frame2, text='DELETE', height=4, width=15, bg="#1F4690", fg="white")
    btn4.pack(side=RIGHT, pady=10, padx=10)

    #Outer Image frame
    frame3 = Frame(root, width=600, height=100, bg="#FBF6F0")
    frame3.pack(side="top", fill=BOTH, padx=50, pady=100)

    with open("users.json", "r") as urs:
        users = json.load(urs)
        for u in users['users']:
            f1 = Frame(frame3, width=150, height=20, highlightbackground="#16213E", highlightthickness=2)
            f1.pack(side="left", fill=BOTH, padx=10, pady=10)
            image = Image.open(u['path'])
            width, height = image.size
            newsize = (140, 140)
            image = image.resize(newsize)

            photo = ImageTk.PhotoImage(image)
            label = Label(f1, image=photo)
            label.image = photo
            label.grid(row=1, column=k)
            label2 = Label(f1, text=u['name'])
            label2.grid(row=2, column=k)
            k += 1
    root.mainloop()

