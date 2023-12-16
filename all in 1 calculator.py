import math
import cmath
from decimal import *
from tkinter import *
import tkinter.messagebox
from tkinter.constants import SUNKEN
from tkinter import IntVar
root = Tk()
root.geometry("400x500")
root.title("All In One Calculator")

options = ["Factorial", "Prime-Composite",  "Odd-Even", "Area-Perimeter", "Calculator", 
          "Quadratic-Cubic","Root Finder", "Power Finder", "Matrices-Determinant"]


def calculate():
    if clicked.get() == "Factorial":
        label = Label(root, text="Number", font="Arial")
        label.place(x=5, y=100)
        number = IntVar()
        textbox = Entry(root, textvariable=number)
        textbox.place(x=70, y=100)

        def calculate1():
            a = number.get()
            f = 1
            for i in range(1,a + 1):
                f = f*i
            label1 = Label(text="Factorial is: " + str("%.3f" % f), fg="Green", font="Arial")
            label1.place(x=5, y=165)

            def next1():
                for widget in root.winfo_children():
                    if isinstance(widget, Label):
                        widget.destroy()
                    if isinstance(widget, Entry):
                        widget.destroy()
                    if isinstance(widget, Button):
                        widget.destroy()
                button7 = Button(root, text="Calculate", command=calculate)
                button7.place(x=165, y=40)

            button_5 = Button(root, text="Next", command=next1)
            button_5.place(x=90, y=193)

            def refresh():
                label1.destroy()
                button_1.destroy()
                button_5.destroy()

            button_1 = Button(root, text="Refresh", command=refresh)
            button_1.place(x=20, y=193)

        button1 = Button(root, text="Calculate", command=calculate1)
        button1.place(x=70, y=130)


    elif clicked.get() == "Prime-Composite":
        label = Label(root, text="Number", font="Arial")
        label.place(x=5, y=100)
        number = IntVar()
        textbox = Entry(root, textvariable=number)
        textbox.place(x=70, y=100)

        def calculate1():
            c=0
            i=1
            while (i<=number.get()):
                if(number.get()%i==0):
                    c+=1
                i+=1
            if(c==2):
                label3 = Label(text="Number is Prime " , fg="Green", font="Arial")
                label3.place(x=5, y=165)
                def next1():
                    for widget in root.winfo_children():
                        if isinstance(widget, Label):
                            widget.destroy()
                        if isinstance(widget, Entry):
                            widget.destroy()
                        if isinstance(widget, Button):
                            widget.destroy()
                    button7 = Button(root, text="Calculate", command=calculate)
                    button7.place(x=165, y=40)

                button_5 = Button(root, text="Next", command=next1)
                button_5.place(x=90, y=190)

                def refresh():
                    label3.destroy()
                    button_1.destroy()
                    button_5.destroy()

                button_1 = Button(root, text="Refresh", command=refresh)
                button_1.place(x=20, y=190)

            elif(number.get()==0):
                label4 = Label(text="Number is Niether Prime Nor Composite " , fg="Green", font="Arial")
                label4.place(x=5, y=165)
                def next1():
                    for widget in root.winfo_children():
                        if isinstance(widget, Label):
                            widget.destroy()
                        if isinstance(widget, Entry):
                            widget.destroy()
                        if isinstance(widget, Button):
                            widget.destroy()
                    button7 = Button(root, text="Calculate", command=calculate)
                    button7.place(x=165, y=40)

                button_5 = Button(root, text="Next", command=next1)
                button_5.place(x=90, y=190)

                def refresh():
                    label4.destroy()
                    button_1.destroy()
                    button_5.destroy()

                button_1 = Button(root, text="Refresh", command=refresh)
                button_1.place(x=20, y=190)
            
            elif(number.get()==1):
                label4 = Label(text="Number is Niether Prime Nor Composite " , fg="Green", font="Arial")
                label4.place(x=5, y=165)
                def next1():
                    for widget in root.winfo_children():
                        if isinstance(widget, Label):
                            widget.destroy()
                        if isinstance(widget, Entry):
                            widget.destroy()
                        if isinstance(widget, Button):
                            widget.destroy()
                    button7 = Button(root, text="Calculate", command=calculate)
                    button7.place(x=165, y=40)

                button_5 = Button(root, text="Next", command=next1)
                button_5.place(x=90, y=190)

                def refresh():
                    label4.destroy()
                    button_1.destroy()
                    button_5.destroy()

                button_1 = Button(root, text="Refresh", command=refresh)
                button_1.place(x=20, y=190)
            
            else:
                label5 = Label(text="Number is Composite" , fg="Green", font="Arial")
                label5.place(x=5, y=165)
                def next1():
                    for widget in root.winfo_children():
                        if isinstance(widget, Label):
                            widget.destroy()
                        if isinstance(widget, Entry):
                            widget.destroy()
                        if isinstance(widget, Button):
                            widget.destroy()
                    button7 = Button(root, text="Calculate", command=calculate)
                    button7.place(x=165, y=40)

                button_5 = Button(root, text="Next", command=next1)
                button_5.place(x=90, y=190)

                def refresh():
                    label5.destroy()
                    button_1.destroy()
                    button_5.destroy()

                button_1 = Button(root, text="Refresh", command=refresh)
                button_1.place(x=20, y=190)


        button1 = Button(root, text="Calculate", command=calculate1)
        button1.place(x=70, y=130)


    elif clicked.get()=="Area-Perimeter":
        label100 = Label(root, text="Select Shape", font=("Arial",12))
        label100.place(x=5, y=87)
        options55 = ["Circle", "Triangle", "Rectangle", "Square", "Parallelogram", "Trapazium"]
        clicked22 = StringVar()
        clicked22.set("Circle")
        drop333 = OptionMenu(root, clicked22, *options55)
        drop333.place(x=110, y=84)
        
                
        def calculate333():
            if clicked22.get() == "Circle":
                label = Label(root, text="Radius", font="Arial")
                label.place(x=5, y=153)
                radius = DoubleVar()
                textbox = Entry(root, textvariable=radius)
                textbox.place(x=70, y=153)

                def calculate1():
                    area = float(math.pi * radius.get() * radius.get())
                    circumference = float(2 * math.pi * radius.get())
                    label1 = Label(text="Area is: " + str("%.3f" % area), fg="Green", font="Arial")
                    label1.place(x=5, y=217)
                    label2 = Label(text="Circumference is: " + str("%.3f" % circumference), fg="Blue", font="Arial")
                    label2.place(x=5, y=240)

                    def next1():
                        for widget in root.winfo_children():
                            if isinstance(widget, Label):
                                widget.destroy()
                            if isinstance(widget, Entry):
                                widget.destroy()
                            if isinstance(widget, Button):
                                widget.destroy()
                            drop333.destroy()
                        button7 = Button(root, text="Calculate", command=calculate)
                        button7.place(x=165, y=40)

                    button_5 = Button(root, text="Next", command=next1)
                    button_5.place(x=90, y=275)

                    def refresh():
                        label1.destroy()
                        label2.destroy()
                        button_1.destroy()
                        button_5.destroy()

                    button_1 = Button(root, text="Refresh", command=refresh)
                    button_1.place(x=20, y=275)

                button1 = Button(root, text="Calculate", command=calculate1)
                button1.place(x=100, y=185)

            elif clicked22.get() == "Rectangle":
                label3 = Label(root, text="Length", font="Arial")
                label3.place(x=5, y=170)
                length = DoubleVar()
                textbox1 = Entry(root, textvariable=length)
                textbox1.place(x=67, y=170)
                label4 = Label(root, text="Breadth", font="Arial")
                label4.place(x=5, y=195)
                breadth = DoubleVar()
                textbox2 = Entry(root, textvariable=breadth)
                textbox2.place(x=67, y=195)

                def calculate2():
                    area1 = float(length.get() * breadth.get())
                    perimeter1 = float(2 * (length.get() + breadth.get()))
                    label5 = Label(text="Area is: " + str("%.3f" % area1), fg="Green", font="Arial")
                    label5.place(x=5, y=250)
                    label6 = Label(text="Perimeter is: " + str("%.3f" % perimeter1), fg="Blue", font="Arial")
                    label6.place(x=5, y=270)

                    def next1():
                        for widget in root.winfo_children():
                            if isinstance(widget, Label):
                                widget.destroy()
                            if isinstance(widget, Entry):
                                widget.destroy()
                            if isinstance(widget, Button):
                                widget.destroy()
                            drop333.destroy()
                        button7 = Button(root, text="Calculate", command=calculate)
                        button7.place(x=165, y=40)

                    button_5 = Button(root, text="Next", command=next1)
                    button_5.place(x=90, y=300)

                    def refresh():
                        label5.destroy()
                        label6.destroy()
                        button__2.destroy()
                        button_5.destroy()

                    button__2 = Button(root, text="Refresh", command=refresh)
                    button__2.place(x=20, y=300)

                button2 = Button(root, text="Calculate", command=calculate2)
                button2.place(x=70, y=220)

            elif clicked22.get() == "Square":
                label7 = Label(root, text="Length", font="Arial")
                label7.place(x=5, y=170)
                length = DoubleVar()
                textbox3 = Entry(root, textvariable=length)
                textbox3.place(x=60, y=170)

                def calculate2():
                    area2 = float(length.get() * length.get())
                    perimeter2 = float(4 * length.get())
                    label8 = Label(text="Area is: " + str("%.3f" % area2), fg="Green", font="Arial")
                    label8.place(x=5, y=230)
                    label9 = Label(text="Perimeter is: " + str("%.3f" % perimeter2), fg="Blue", font="Arial")
                    label9.place(x=5, y=250)

                    def next1():
                        for widget in root.winfo_children():
                            if isinstance(widget, Label):
                                widget.destroy()
                            if isinstance(widget, Entry):
                                widget.destroy()
                            if isinstance(widget, Button):
                                widget.destroy()
                            drop333.destroy()
                        button7 = Button(root, text="Calculate", command=calculate)
                        button7.place(x=165, y=40)

                    button_5 = Button(root, text="Next", command=next1)
                    button_5.place(x=90, y=280)

                    def refresh():
                        label8.destroy()
                        label9.destroy()
                        button_3.destroy()
                        button_5.destroy()

                    button_3 = Button(root, text="Refresh", command=refresh)
                    button_3.place(x=20, y=280)

                button3 = Button(root, text="Calculate", command=calculate2)
                button3.place(x=70, y=195)

            elif clicked22.get() == "Parallelogram":
                label23 = Label(root, text="Hieght", font="Arial")
                label23.place(x=5, y=160)
                hieght = DoubleVar()
                textbox9 = Entry(root, textvariable=hieght)
                textbox9.place(x=67, y=160)
                label24 = Label(root, text="Base", font="Arial")
                label24.place(x=5, y=185)
                Side1 = DoubleVar()
                textbox10 = Entry(root, textvariable=Side1)
                textbox10.place(x=67, y=185)
                label25 = Label(root, text="Side", font="Arial")
                label25.place(x=5, y=210)
                Side2 = DoubleVar()
                textbox11 = Entry(root, textvariable=Side2)
                textbox11.place(x=67, y=210)

                def calculate2():
                    area1 = float(hieght.get() * Side1.get())
                    perimeter1 = float(2 * (Side1.get() + Side2.get()))
                    label5 = Label(text="Area is: " + str("%.3f" % area1), fg="Green", font="Arial")
                    label5.place(x=5, y=270)
                    label6 = Label(text="Perimeter is: " + str("%.3f" % perimeter1), fg="Blue", font="Arial")
                    label6.place(x=5, y=290)

                    def next1():
                        for widget in root.winfo_children():
                            if isinstance(widget, Label):
                                widget.destroy()
                            if isinstance(widget, Entry):
                                widget.destroy()
                            if isinstance(widget, Button):
                                widget.destroy()
                            drop333.destroy()
                        button7 = Button(root, text="Calculate", command=calculate)
                        button7.place(x=165, y=40)

                    button_5 = Button(root, text="Next", command=next1)
                    button_5.place(x=90, y=320)

                    def refresh():
                        label5.destroy()
                        label6.destroy()
                        button__2.destroy()
                        button_5.destroy()

                    button__2 = Button(root, text="Refresh", command=refresh)
                    button__2.place(x=20, y=320)

                button2 = Button(root, text="Calculate", command=calculate2)
                button2.place(x=70, y=240)   

            elif clicked22.get() == "Trapazium":
                label23 = Label(root, text="Hieght", font="Arial")
                label23.place(x=5, y=210)
                hieght = DoubleVar()
                textbox9 = Entry(root, textvariable=hieght)
                textbox9.place(x=67, y=210)
                label24 = Label(root, text="Parallel Side 1", font=("Arial", 11))
                label24.place(x=5, y=153)
                Side1 = DoubleVar()
                textbox10 = Entry(root, textvariable=Side1)
                textbox10.place(x=110, y=153)
                label25 = Label(root, text="Parallel Side 2", font=("Arial", 11))
                label25.place(x=5, y=180)
                Side2 = DoubleVar()
                textbox11 = Entry(root, textvariable=Side2)
                textbox11.place(x=110, y=180)
                label24 = Label(root, text="Side 3", font="Arial")
                label24.place(x=5, y=237)
                Side3 = DoubleVar()
                textbox10 = Entry(root, textvariable=Side3)
                textbox10.place(x=67, y=237)
                label25 = Label(root, text="Side 4", font="Arial")
                label25.place(x=5, y=268)
                Side4 = DoubleVar()
                textbox11 = Entry(root, textvariable=Side4)
                textbox11.place(x=67, y=268)
            
                def calculate2():
                    area1 = float(1/2*(hieght.get()*(Side1.get()+Side2.get())))
                    perimeter1 = float(Side1.get() + Side2.get()+Side3.get() + Side4.get())
                    label5 = Label(text="Area is: " + str("%.3f" % area1), fg="Green", font="Arial")
                    label5.place(x=5, y=330)
                    label6 = Label(text="Perimeter is: " + str("%.3f" % perimeter1), fg="Blue", font="Arial")
                    label6.place(x=5, y=357)

                    def next1():
                        for widget in root.winfo_children():
                            if isinstance(widget, Label):
                                widget.destroy()
                            if isinstance(widget, Entry):
                                widget.destroy()
                            if isinstance(widget, Button):
                                widget.destroy()
                            drop333.destroy()
                        button7 = Button(root, text="Calculate", command=calculate)
                        button7.place(x=165, y=40)

                    button_5 = Button(root, text="Next", command=next1)
                    button_5.place(x=90, y=383)

                    def refresh():
                        label5.destroy()
                        label6.destroy()
                        button__2.destroy()
                        button_5.destroy()

                    button__2 = Button(root, text="Refresh", command=refresh)
                    button__2.place(x=20, y=383)

                button2 = Button(root, text="Calculate", command=calculate2)
                button2.place(x=70, y=300)


            elif clicked22.get() == "Triangle":
                label10 = Label(root, text="Calculate By :", font=("Arial",11))
                label10.place(x=5, y=157)
                options2 = ["Three Sides", "Height And Base"]
                clicked2 = StringVar()
                clicked2.set("Three Sides")
                drop1 = OptionMenu(root, clicked2, *options2)
                drop1.place(x=95, y=155)
                def calculate3():
                    if clicked2.get() == "Three Sides":
                        label11 = Label(root, text="Side1", font="Arial")
                        label11.place(x=5, y=220)
                        label12 = Label(root, text="Side2", font="Arial")
                        label12.place(x=5, y=260)
                        label13 = Label(root, text="Side3", font="Arial")
                        label13.place(x=5, y=300)
                        side1 = DoubleVar()
                        side2 = DoubleVar()
                        side3 = DoubleVar()
                        textbox4 = Entry(root, textvariable=side1)
                        textbox4.place(x=55, y=222)
                        textbox5 = Entry(root, textvariable=side2)
                        textbox5.place(x=55, y=262)
                        textbox6 = Entry(root, textvariable=side3)
                        textbox6.place(x=55, y=302)

                        def calculate4():

                            check1 = side1.get() + side2.get()
                            check2 = side2.get() + side3.get()
                            check3 = side3.get() + side1.get()

                            perimeter = side1.get() + side2.get() + side2.get()

                            if check1 < side3.get():
                                label14 = Label(root, text="Triangle Is Not Possible", fg="Green", font="Arial")
                                label14.place(x=25, y=360)

                                def next1():
                                    for widget in root.winfo_children():
                                        if isinstance(widget, Label):
                                            widget.destroy()
                                        if isinstance(widget, Entry):
                                            widget.destroy()
                                        if isinstance(widget, Button):
                                            widget.destroy()
                                    drop1.destroy()
                                    drop333.destroy()
                                    button7 = Button(root, text="Calculate", command=calculate)
                                    button7.place(x=165, y=40)

                                button_5 = Button(root, text="Next", command=next1)
                                button_5.place(x=100, y=385)

                                def refresh():
                                    label14.destroy()
                                    button_4.destroy()
                                    button_5.destroy()

                                button_4 = Button(root, text="Refresh", command=refresh)
                                button_4.place(x=25, y=385)

                            elif check2 < side1.get():
                                label14 = Label(root, text="Triangle Is Not Possible", fg="Green", font="Arial")
                                label14.place(x=25, y=360)

                                def next1():
                                    for widget in root.winfo_children():
                                        if isinstance(widget, Label):
                                            widget.destroy()
                                        if isinstance(widget, Entry):
                                            widget.destroy()
                                        if isinstance(widget, Button):
                                            widget.destroy()
                                    drop333.destroy()
                                    drop1.destroy()
                                    button7 = Button(root, text="Calculate", command=calculate)
                                    button7.place(x=165, y=40)

                                button_5 = Button(root, text="Next", command=next1)
                                button_5.place(x=100, y=385)

                                def refresh():
                                    label14.destroy()
                                    button_4.destroy()
                                    button_5.destroy()

                                button_4 = Button(root, text="Refresh", command=refresh)
                                button_4.place(x=25, y=385)

                            elif check3 < side2.get():
                                label14 = Label(root, text="Triangle Is Not Possible", fg="Green", font="Arial")
                                label14.place(x=25, y=360)

                                def next1():
                                    for widget in root.winfo_children():
                                        if isinstance(widget, Label):
                                            widget.destroy()
                                        if isinstance(widget, Entry):
                                            widget.destroy()
                                        if isinstance(widget, Button):
                                            widget.destroy()
                                    drop1.destroy()
                                    drop333.destroy()
                                    button7 = Button(root, text="Calculate", command=calculate)
                                    button7.place(x=165, y=40)

                                button_5 = Button(root, text="Next", command=next1)
                                button_5.place(x=100, y=385)

                                def refresh():
                                    label14.destroy()
                                    button_4.destroy()
                                    button_5.destroy()

                                button_4 = Button(root, text="Refresh", command=refresh)
                                button_4.place(x=30, y=385)

                            elif check1 == side3.get():
                                label15 = Label(root, text="Triangle Is A Degenerate Triangle", fg="Green", font="Arial")
                                label15.place(x=25, y=356)
                                label16 = Label(root, text="Area is: " + '0', fg="Red", font="Arial")
                                label16.place(x=25, y=378)
                                label17 = Label(text="Longest side is: " + str("%.3f" % perimeter), fg="Blue", font="Arial")
                                label17.place(x=25, y=398)

                                def next1():
                                    for widget in root.winfo_children():
                                        if isinstance(widget, Label):
                                            widget.destroy()
                                        if isinstance(widget, Entry):
                                            widget.destroy()
                                        if isinstance(widget, Button):
                                            widget.destroy()
                                    drop1.destroy()
                                    drop333.destroy()
                                    button7 = Button(root, text="Calculate", command=calculate)
                                    button7.place(x=165, y=40)

                                button_5 = Button(root, text="Next", command=next1)
                                button_5.place(x=100, y=427)

                                def refresh():
                                    label15.destroy()
                                    label16.destroy()
                                    label17.destroy()
                                    button_5.destroy()
                                    button_4.destroy()

                                button_4 = Button(root, text="Refresh", command=refresh)
                                button_4.place(x=30, y=427)

                            elif check2 == side1.get():
                                label15 = Label(root, text="Triangle Is A Degenerate Triangle", fg="Green", font="Arial")
                                label15.place(x=25, y=356)
                                label16 = Label(root, text="Area is: " + '0', fg="Red", font="Arial")
                                label16.place(x=25, y=378)
                                label17 = Label(text="Longest side is: " + str("%.3f" % perimeter), fg="Blue", font="Arial")
                                label17.place(x=25, y=398)

                                def next1():
                                    for widget in root.winfo_children():
                                        if isinstance(widget, Label):
                                            widget.destroy()
                                        if isinstance(widget, Entry):
                                            widget.destroy()
                                        if isinstance(widget, Button):
                                            widget.destroy()
                                    drop1.destroy()
                                    drop333.destroy()
                                    button7 = Button(root, text="Calculate", command=calculate)
                                    button7.place(x=165, y=40)

                                button_5 = Button(root, text="Next", command=next1)
                                button_5.place(x=100, y=427)

                                def refresh():
                                    label15.destroy()
                                    label16.destroy()
                                    label17.destroy()
                                    button_5.destroy()
                                    button_4.destroy()

                                button_4 = Button(root, text="Refresh", command=refresh)
                                button_4.place(x=30, y=427)

                            elif check3 == side2.get():
                                label15 = Label(root, text="Triangle Is A Degenerate Triangle", fg="Green", font="Arial")
                                label15.place(x=25, y=356)
                                label16 = Label(root, text="Area is: " + '0', fg="Red", font="Arial")
                                label16.place(x=25, y=378)
                                label17 = Label(text="Longest side is: " + str("%.3f" % perimeter), fg="Blue", font="Arial")
                                label17.place(x=25, y=398)

                                def next1():
                                    for widget in root.winfo_children():
                                        if isinstance(widget, Label):
                                            widget.destroy()
                                        if isinstance(widget, Entry):
                                            widget.destroy()
                                        if isinstance(widget, Button):
                                            widget.destroy()
                                    drop1.destroy()
                                    drop333.destroy()
                                    button7 = Button(root, text="Calculate", command=calculate)
                                    button7.place(x=165, y=40)

                                button_5 = Button(root, text="Next", command=next1)
                                button_5.place(x=100, y=427)

                                def refresh():
                                    label15.destroy()
                                    label16.destroy()
                                    label17.destroy()
                                    button_5.destroy()
                                    button_4.destroy()

                                button_4 = Button(root, text="Refresh", command=refresh)
                                button_4.place(x=30, y=427)

                            else:
                                s = float((side1.get() + side2.get() + side3.get()) / 2)
                                area3 = math.sqrt(
                                    float(s) * (float(s) - side1.get()) * (float(s) - side2.get()) * (float(s) - side3.get()))
                                perimeter3 = side1.get() + side2.get() + side2.get()
                                label18 = Label(text="Area is: " + str("%.3f" % area3), fg="Green", font="Arial")
                                label18.place(x=25, y=365)
                                label19 = Label(text="Perimeter is: " + str("%.3f" % perimeter3), fg="Blue", font="Arial")
                                label19.place(x=25, y=389)

                                def next1():
                                    for widget in root.winfo_children():
                                        if isinstance(widget, Label):
                                            widget.destroy()
                                        if isinstance(widget, Entry):
                                            widget.destroy()
                                        if isinstance(widget, Button):
                                            widget.destroy()
                                    drop1.destroy()
                                    drop333.destroy()
                                    button7 = Button(root, text="Calculate", command=calculate)
                                    button7.place(x=165, y=40)

                                button_5 = Button(root, text="Next", command=next1)
                                button_5.place(x=100, y=418)

                                def refresh():
                                    label18.destroy()
                                    label19.destroy()
                                    button_4.destroy()
                                    button_5.destroy()

                                button_4 = Button(root, text="Refresh", command=refresh)
                                button_4.place(x=30, y=418)

                        button4 = Button(root, text="Calculate", command=calculate4)
                        button4.place(x=55, y=330)

                    elif clicked2.get() == "Height And Base":
                        label20 = Label(root, text="Base", font="Arial")
                        label20.place(x=5, y=225)
                        label21 = Label(root, text="Height", font="Arial")
                        label21.place(x=5, y=255)
                        side = DoubleVar()
                        height = DoubleVar()
                        textbox7 = Entry(root, textvariable=side)
                        textbox7.place(x=65, y=225)
                        textbox8 = Entry(root, textvariable=height)
                        textbox8.place(x=65, y=255)

                        def calculate44():
                            area4 = 0.5 * side.get() * height.get()
                            label22 = Label(root, text="Area is:" + str("%.3f" % area4), fg="Green", font="Arial")
                            label22.place(x=25, y=310)
                            label23 = Label(root, text="Perimeter can't be determined accurately", fg="Blue", font="Arial")
                            label23.place(x=25, y=330)

                            def next1():
                                for widget in root.winfo_children():
                                    if isinstance(widget, Label):
                                        widget.destroy()
                                    if isinstance(widget, Entry):
                                        widget.destroy()
                                    if isinstance(widget, Button):
                                        widget.destroy()
                                drop1.destroy()
                                drop333.destroy()
                                button7 = Button(root, text="Calculate", command=calculate)
                                button7.place(x=165, y=40)

                            button_5 = Button(root, text="Next", command=next1)
                            button_5.place(x=100, y=360)

                            def refresh():
                                label22.destroy()
                                label23.destroy()
                                button_4.destroy()
                                button_5.destroy()

                            button_4 = Button(root, text="Refresh", command=refresh)
                            button_4.place(x=30, y=360)

                        button5 = Button(root, text="Calculate", command=calculate44)
                        button5.place(x=60, y=280)

                button33 = Button(root, text="Calculate", command=calculate3)
                button33.place(x=115, y=190)

        button333 = Button(root, text="Calculate", command=calculate333)
        button333.place(x=115, y=120)

    elif clicked.get() == "Odd-Even":
            label = Label(root, text="Number", font="Arial")
            label.place(x=5, y=100)
            number = IntVar()
            textbox = Entry(root, textvariable=number)
            textbox.place(x=70, y=100)

            def calculate1():
                a = number.get()%2
                b = number.get()
                if(b==0):
                    label1 = Label(text="Number is neither odd nor even" , fg="Green", font="Arial")
                    label1.place(x=5, y=163)

                    def next1():
                            for widget in root.winfo_children():
                                if isinstance(widget, Label):
                                    widget.destroy()
                                if isinstance(widget, Entry):
                                    widget.destroy()
                                if isinstance(widget, Button):
                                    widget.destroy()
                            button7 = Button(root, text="Calculate", command=calculate)
                            button7.place(x=165, y=40)

                    button_5 = Button(root, text="Next", command=next1)
                    button_5.place(x=90, y=193)

                    def refresh():
                            label1.destroy()
                            button_1.destroy()
                            button_5.destroy()

                    button_1 = Button(root, text="Refresh", command=refresh)
                    button_1.place(x=20, y=193)
                elif(a==0):
                    label1 = Label(text="Number is even " , fg="Green", font="Arial")
                    label1.place(x=5, y=165)

                    def next1():
                            for widget in root.winfo_children():
                                if isinstance(widget, Label):
                                    widget.destroy()
                                if isinstance(widget, Entry):
                                    widget.destroy()
                                if isinstance(widget, Button):
                                    widget.destroy()
                            button7 = Button(root, text="Calculate", command=calculate)
                            button7.place(x=165, y=40)

                    button_5 = Button(root, text="Next", command=next1)
                    button_5.place(x=90, y=193)

                    def refresh():
                            label1.destroy()
                            button_1.destroy()
                            button_5.destroy()

                    button_1 = Button(root, text="Refresh", command=refresh)
                    button_1.place(x=20, y=193)

                else:
                    label1 = Label(text="Number is Odd " , fg="Green", font="Arial")
                    label1.place(x=5, y=165)

                    def next1():
                        for widget in root.winfo_children():
                            if isinstance(widget, Label):
                                widget.destroy()
                            if isinstance(widget, Entry):
                                widget.destroy()
                            if isinstance(widget, Button):
                                widget.destroy()
                        button7 = Button(root, text="Calculate", command=calculate)
                        button7.place(x=165, y=40)

                    button_5 = Button(root, text="Next", command=next1)
                    button_5.place(x=90, y=193)

                    def refresh():
                        label1.destroy()
                        button_1.destroy()
                        button_5.destroy()

                    button_1 = Button(root, text="Refresh", command=refresh)
                    button_1.place(x=20, y=193)

            button1 = Button(root, text="Calculate", command=calculate1)
            button1.place(x=70, y=130)   
            
    if clicked.get() == "Calculator":
        frame = Frame(master=root, padx=10)
        frame.place(x=90, y=80)
        entry = Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
        entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

        def myclick(number):
            entry.insert(END, number)
    
    
        def equal():
            try:
                y = str(eval(entry.get()))
                entry.delete(0, END)
                entry.insert(0, y)
            except:
                tkinter.messagebox.showinfo("Error", "Syntax Error")
        
        
        def clear():
            entry.delete(0, END)
        
        
        button_1 = Button(master=frame, text='1', padx=15,
                            pady=5, width=3, command=lambda: myclick(1))
        button_1.grid(row=1, column=0, pady=2)
        button_2 = Button(master=frame, text='2', padx=15,
                            pady=5, width=3, command=lambda: myclick(2))
        button_2.grid(row=1, column=1, pady=2)
        button_3 = Button(master=frame, text='3', padx=15,
                            pady=5, width=3, command=lambda: myclick(3))
        button_3.grid(row=1, column=2, pady=2)
        button_4 = Button(master=frame, text='4', padx=15,
                            pady=5, width=3, command=lambda: myclick(4))
        button_4.grid(row=2, column=0, pady=2)
        button_5 = Button(master=frame, text='5', padx=15,
                            pady=5, width=3, command=lambda: myclick(5))
        button_5.grid(row=2, column=1, pady=2)
        button_6 = Button(master=frame, text='6', padx=15,
                            pady=5, width=3, command=lambda: myclick(6))
        button_6.grid(row=2, column=2, pady=2)
        button_7 = Button(master=frame, text='7', padx=15,
                            pady=5, width=3, command=lambda: myclick(7))
        button_7.grid(row=3, column=0, pady=2)
        button_8 = Button(master=frame, text='8', padx=15,
                            pady=5, width=3, command=lambda: myclick(8))
        button_8.grid(row=3, column=1, pady=2)
        button_9 = Button(master=frame, text='9', padx=15,
                            pady=5, width=3, command=lambda: myclick(9))
        button_9.grid(row=3, column=2, pady=2)
        button_0 = Button(master=frame, text='0', padx=15,
                            pady=5, width=3, command=lambda: myclick(0))
        button_0.grid(row=4, column=1, pady=2)
        
        button_add = Button(master=frame, text="+", padx=15,
                            pady=5, width=3, command=lambda: myclick('+'))
        button_add.grid(row=5, column=0, pady=2)
        
        button_subtract = Button(
            master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'))
        button_subtract.grid(row=5, column=1, pady=2)
        
        button_multiply = Button(
            master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'))
        button_multiply.grid(row=5, column=2, pady=2)
        
        button_div = Button(master=frame, text="/", padx=15,
                            pady=5, width=3, command=lambda: myclick('/'))
        button_div.grid(row=6, column=0, pady=2)
        
        button_clear = Button(master=frame, text="clear",
                                padx=15, pady=5, width=12, command=clear)
        button_clear.grid(row=6, column=1, columnspan=2, pady=2)
        
        button_equal = Button(master=frame, text="=", padx=15,
                                pady=5, width=9, command=equal)
        button_equal.grid(row=7, column=0, columnspan=3, pady=2)

        def next22():
            frame.destroy()
            button1110.destroy()
        button1110 = Button(root, text="Next", command=next22)
        button1110.place(x=170,y=400)

    elif clicked.get() == "Quadratic-Cubic":
        label5445 = Label(root, text="Select", font="Arial")
        label5445.place(x = 5, y = 84)
        clicked222 = StringVar()
        clicked222.set("Quadratic")
        options232 = ["Quadratic","Cubic"]
        drop232 = OptionMenu(root, clicked222, *options232)
        drop232.place(x=60, y=80)
        def calculate232():
            if clicked222.get() == "Quadratic":
                    label = Label(root, text="a", font="Arial")
                    label.place(x=5, y=155)
                    number1 = DoubleVar()
                    textbox = Entry(root, textvariable=number1)
                    textbox.place(x=40, y=158)
                    label1 = Label(root, text="b", font="Arial")
                    label1.place(x=5, y=185)
                    number2 = DoubleVar()
                    textbox1 = Entry(root, textvariable=number2)
                    textbox1.place(x=40, y=188)
                    label2 = Label(root, text="c", font="Arial")
                    label2.place(x=5, y=215)
                    number3 = DoubleVar()
                    textbox2 = Entry(root, textvariable=number3)
                    textbox2.place(x=40, y=218)


                    def calculate262():
                        a = number1.get()
                        b = number2.get()
                        c = number3.get()
                        D = ((b*b)-4*a*c)
                        if D >= 0:
                            A = ((-b+cmath.sqrt((b*b)-4*a*c))/(2*a))
                            B = ((-b-cmath.sqrt((b*b)-4*a*c))/(2*a))
                            label88 = Label(root, text="Roots Are : " + str("%.3f" % A.real) 
                                            + " & " + str("%.3f" % B.real), 
                                        font="Arial")
                            label88.place(x=5, y=285)
                        else :
                            A = ((-b+cmath.sqrt((b*b)-4*a*c))/(2*a))
                            B = ((-b-cmath.sqrt((b*b)-4*a*c))/(2*a))
                            label88 = Label(root, text="Roots Are : " + str("%.3f" % A.real) + "+" + str("%.3f" % A.imag) + "j"
                                            + " & " + str("%.3f" % B.real) + str("%.3f" % B.imag) + "j", 
                                        font="Arial")
                            label88.place(x=5, y=285)

                        def next1():
                            for widget in root.winfo_children():
                                if isinstance(widget, Label):
                                    widget.destroy()
                                if isinstance(widget, Entry):
                                    widget.destroy()
                                if isinstance(widget, Button):
                                    widget.destroy()
                                drop232.destroy()
                            button7 = Button(root, text="Calculate", command=calculate)
                            button7.place(x=165, y=40)

                        button_5 = Button(root, text="Next", command=next1)
                        button_5.place(x=90, y=320)

                        def refresh():
                            label88.destroy()
                            button_1.destroy()
                            button_5.destroy()

                        button_1 = Button(root, text="Refresh", command=refresh)
                        button_1.place(x=20, y=320)

                    button262 = Button(root, text="Calculate", command=calculate262)
                    button262.place(x=70, y=250)

            elif clicked222.get() == "Cubic":
                    label = Label(root, text="a", font="Arial")
                    label.place(x=5, y=155)
                    number1 = DoubleVar()
                    textbox = Entry(root, textvariable=number1)
                    textbox.place(x=40, y=158)
                    label1 = Label(root, text="b", font="Arial")
                    label1.place(x=5, y=185)
                    number2 = DoubleVar()
                    textbox1 = Entry(root, textvariable=number2)
                    textbox1.place(x=40, y=188)
                    label2 = Label(root, text="c", font="Arial")
                    label2.place(x=5, y=215)
                    number3 = DoubleVar()
                    textbox2 = Entry(root, textvariable=number3)
                    textbox2.place(x=40, y=218)
                    label3 = Label(root, text="d", font="Arial")
                    label3.place(x=5, y=245)
                    number4 = DoubleVar()
                    textbox3 = Entry(root, textvariable=number4)
                    textbox3.place(x=40, y=248)

                    def calculate262():
                        def cube_root(x):
                            if x.real < 0:
                                x = abs(x)
                                cube_root = x**(1/3)*(-1)
                            else:
                                cube_root = x**(1/3)
                            return cube_root
                        
                        a = number1.get()
                        b = number2.get()
                        c = number3.get()
                        d = number4.get()

                        q = (3*a*c-(b*b))/(9*a*a)
                        div = 54*a*a*a
                        r1 = ((9*a*b*c)-(27*a*a*d)-(2*b*b*b))
                        r = r1/div
                        f = (q**3)+(r**2)

                        if f>=0 :
                            f1 = f**(1/2)
                            s = (r+f1)**(1/3)
                            t = cube_root(r-f1)
                            A = (s+t)-(b/(3*a))
                            B = -((s+t)/2)-(b/(3*a))
                            B1 = (s-t)*(math.sqrt(3)/2)
                            C = -((s+t)/2)-(b/(3*a))
                            C1 = (s-t)*(math.sqrt(3)/2)


                            label88 = Label(root, text="Roots Are : " + str("%.3f" % A)+ " , " +str("%.3f" % B) 
                                           + "+" +str("%.3f" % B1)+"j"+ " & " + str("%.3f" % C) 
                                           + "-" +str("%.3f" % C1)+"j" , font="Arial")
                            label88.place(x=5, y=305)
                        
                        else :
                            f1 = f**(1/2)
                            s = (r+f1)**(1/3)
                            t = (r-f1)**(1/3)
                            A = (s+t)-(b/(3*a))
                            B = -((s+t)/2)-(b/(3*a))
                            B1 = (s-t)*(math.sqrt(3)/2)
                            C = -((s+t)/2)-(b/(3*a))
                            C1 = (s-t)*(math.sqrt(3)/2)
                            BB = B.real + B1.imag
                            CC = C.real - C1.imag

                            label88 = Label(root, text="Roots Are : " + str("%.3f" % A.real)+ " , " +str("%.3f" % BB)+ " & " 
                                            + str("%.3f" % CC), font="Arial")
                            label88.place(x=5, y=305)
                        

        
                        def next1():
                            for widget in root.winfo_children():
                                if isinstance(widget, Label):
                                    widget.destroy()
                                if isinstance(widget, Entry):
                                    widget.destroy()
                                if isinstance(widget, Button):
                                    widget.destroy()
                                drop232.destroy()
                            button7 = Button(root, text="Calculate", command=calculate)
                            button7.place(x=165, y=40)

                        button_5 = Button(root, text="Next", command=next1)
                        button_5.place(x=90, y=337)

                        def refresh():
                            label88.destroy()
                            button_1.destroy()
                            button_5.destroy()

                        button_1 = Button(root, text="Refresh", command=refresh)
                        button_1.place(x=20, y=337)

                    button262 = Button(root, text="Calculate", command=calculate262)
                    button262.place(x=70, y=275)         

        button2322 = Button(root, text="Calculate", command=calculate232)
        button2322.place(x=70, y=120)

    elif clicked.get() == "Root Finder":
        label = Label(root, text="Number", font="Arial")
        label.place(x=5, y=100)
        number = IntVar()
        textbox = Entry(root, textvariable=number)
        textbox.place(x=70, y=100)
        label11 = Label(root, text="Root", font="Arial")
        label11.place(x=5, y=130)
        number11 = IntVar()
        textbox11 = Entry(root, textvariable=number11)
        textbox11.place(x=70, y=130)

        def calculate1():
            a = number.get()
            n = number11.get()
            ans = a**(1/n)
            
            label1 = Label(text="Root is: " + str("%.3f" % ans), fg="Green", font="Arial")
            label1.place(x=5, y=190)

            def next1():
                for widget in root.winfo_children():
                    if isinstance(widget, Label):
                        widget.destroy()
                    if isinstance(widget, Entry):
                        widget.destroy()
                    if isinstance(widget, Button):
                        widget.destroy()
                button7 = Button(root, text="Calculate", command=calculate)
                button7.place(x=165, y=40)

            button_5 = Button(root, text="Next", command=next1)
            button_5.place(x=90, y=223)

            def refresh():
                label1.destroy()
                button_1.destroy()
                button_5.destroy()

            button_1 = Button(root, text="Refresh", command=refresh)
            button_1.place(x=20, y=223)

        button1 = Button(root, text="Calculate", command=calculate1)
        button1.place(x=70, y=160)

    elif clicked.get() == "Power Finder":
        label = Label(root, text="Number", font="Arial")
        label.place(x=5, y=100)
        number = IntVar()
        textbox = Entry(root, textvariable=number)
        textbox.place(x=70, y=100)
        label11 = Label(root, text="Power", font="Arial")
        label11.place(x=5, y=130)
        number11 = IntVar()
        textbox11 = Entry(root, textvariable=number11)
        textbox11.place(x=70, y=130)

        def calculate1():
            a = number.get()
            n = number11.get()
            ans = a**(n)
            
            label1 = Label(text="Answer is: " + str("%.3f" % ans), fg="Green", font="Arial")
            label1.place(x=5, y=190)

            def next1():
                for widget in root.winfo_children():
                    if isinstance(widget, Label):
                        widget.destroy()
                    if isinstance(widget, Entry):
                        widget.destroy()
                    if isinstance(widget, Button):
                        widget.destroy()
                button7 = Button(root, text="Calculate", command=calculate)
                button7.place(x=165, y=40)

            button_5 = Button(root, text="Next", command=next1)
            button_5.place(x=90, y=223)

            def refresh():
                label1.destroy()
                button_1.destroy()
                button_5.destroy()

            button_1 = Button(root, text="Refresh", command=refresh)
            button_1.place(x=20, y=223)

        button1 = Button(root, text="Calculate", command=calculate1)
        button1.place(x=70, y=160)   

    elif clicked.get() == "Matrices-Determinant":
        label = Label(root, text="Operation", font="Arial")
        label.place(x=5, y=91)
        clicked222 = StringVar()
        clicked222.set("Determinant")
        options222 = ["Determinant", "Adjoint", "Transpose", "Addition", "Subtraction", "Multiplication", "Rank"]
        drop222 = OptionMenu(root, clicked222, *options222)
        drop222.place(x=85, y=88)
        def calculate222():
            if clicked222.get() == "Determinant":
                label2 = Label(root, text="No of rows", font=("Arial",10))
                label2.place(x=5, y=170)
                label4 = Label(root, text="No of columns", font=("Arial",10))
                label4.place(x=5, y=200)
                number = IntVar()
                textbox = Entry(root, textvariable=number)
                textbox.place(x=100, y=170)
                number2 = IntVar()
                textbox = Entry(root, textvariable=number2)
                textbox.place(x=100, y=200)
                


        button177 = Button(root, text="Calculate", command=calculate222)
        button177.place(x=65, y=130) 
        


clicked = StringVar()
clicked.set("Factorial")

drop = OptionMenu(root, clicked, *options)
drop.place(x=157, y=0)

button = Button(root, text="Calculate", command=calculate)
button.place(x=165, y=40)

root.mainloop()