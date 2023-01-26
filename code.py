from tkinter import *
# from PIL import ImageTk,Image
import tkinter.messagebox as tmsg
#mport mysql.connector as mysql
import random , string
root=Tk()
root.iconbitmap(r'C:\\Users\\Lenovo\\Documents\\Project\\logo.ico')
root.title("                                                                         The Imperial Hotel              ")
root.geometry("2100x800+0+0")



def window():
    new = Toplevel(root)
    #root=Tk()
    new.iconbitmap(r'C:\\Users\\Lenovo\\Documents\\Project\\logo.ico')
    new.title("                                                                         Booking              ")

    new.minsize(800, 550)
    new.maxsize(800, 550)




    def getvals():
        password = []
        for i in range(5):
            alpha = random.choice(string.ascii_letters)
            # symbol=random.choice(string.punctuation)
            numbers = random.choice(string.digits)
            password.append(alpha)
            # password.append(symbol)
            password.append(numbers)
        y = "".join(str(x) for x in password)
        lbl.config(text=y)

        '''nam=name1.get()
        phon=phone1.get()
        emai=email1.get()
        checki=checkin2.get()
        checkou=checkout2.get()
        packag=package1.get()'''
        '''if name=="":
            tmsg.showinfo("Error", "fill all the requirements")

        elif phone=="":
            tmsg.showinfo("Error", "fill all the requirements")

        elif email=="":
            tmsg.showinfo("Error", "fill all the requirements")

        elif checkin=="":
            tmsg.showinfo("Error", "fill all the requirements")

        elif checkout=="":
            tmsg.showinfo("Error", "fill all the requirements")'''

        '''con = mysql.connect(host="localhost", user="root", password="root", database="gui")
        cursor = con.cursor()
        cursor.execute("INSERT INTO booking VALUES('" + nam+ "','" + phon + "','" + emai + "','" + checki.get() + "','" + checkou.get() + "','" + packag.get() + "')")
        cursor.execute("commit")'''


        print("values are")
        print(f"{name.get(), phone.get(), email.get(), checkin1.get(), checkout1.get(), package.get()}")
        with open("mainproject.txt", "a") as f:
            f.write(f"{name.get(), phone.get(), email.get(), checkin1.get(), checkout1.get(), package.get()}\n")
        tmsg.showinfo("Thank You", "You will get a confirmation message for you booking")
        #tmsg.showinfo("Submitted","you have sucessfully booked a room")

    Label(new, text="        ", ).grid(row=0, column=1)
    Label(new, text="The Imperial Hotel", fg="purple", font="times 25 bold").grid(row=0, column=2)
    Label(new, text="           ").grid(row=1, column=1)
    Label(new, text="Name", fg="black", font="arial 15 bold").grid(row=2, column=1)
    Label(new, text="       Phone no.", fg="black", font="arial 15 bold").grid(row=3, column=1)
    Label(new, text="    Email-Id", fg="black", font="arial 15 bold").grid(row=4, column=1)
    Label(new, text="              Check - In Date", fg="black", font="arial 15 bold").grid(row=5, column=1)
    Label(new, text="                 Check - Out Date", fg="black", font="arial 15 bold").grid(row=6, column=1)
    Label(new, text="    Package ", fg="black", font="arial 15 bold").grid(row=7, column=1)




    name = StringVar()
    phone = StringVar()
    email = StringVar()
    checkin1 = StringVar()
    checkout1 = StringVar()
    package = StringVar()

    name1 = Entry(new, textvariable=name, width=50).grid(row=2, column=2)
    phone1 = Entry(new, textvariable=phone, width=50).grid(row=3, column=2)
    email1 = Entry(new, textvariable=email, width=50).grid(row=4, column=2)
    checkin2 = Entry(new, textvariable=checkin1, width=50).grid(row=5, column=2)
    checkout2 = Entry(new, textvariable=checkout1, width=50).grid(row=6, column=2)
    package1 = Entry(new, textvariable=package, width=50).grid(row=7, column=2)

    lbl = Label(new, font="times 20 bold", fg="red")
    lbl.grid(row=9, column=2)
    Label(new, text="Your Check In Password is", font="times 20 bold").grid(row=9, column=1)
    Button(new, text="  SUBMIT  ", fg="white", width=20, bg="red", font=" bold", command=getvals).grid(row=8, column=2)

    lbx = Listbox(new, width=50)
    lbx.grid(row=10, column=2)
    lbx.insert(END, "         ROOM PACKAGE - ")
    lbx.insert(END, " 1:   Luxury-9,999/Night")
    lbx.insert(END, " 2:   Luxury Duo-17,999/Night")
    lbx.insert(END, " 3:   Superior-7,999/Night")
    lbx.insert(END, " 4:   Family Package-4,999/Night")
    lbx.insert(END, " 5:   Couple Package-2,999 ")
    lbx.insert(END, " 6:   Tourist Package-6,999")

    Label(new, text="       Packages:", font="times 20 bold").grid(row=10, column=1)

    def moreinfo():
        new1 = Toplevel(root)
        #root = Tk()
        new1.iconbitmap(r'C:\\Users\\Lenovo\\Documents\\Project\\logo.ico')
        new1.title("                                                                         DETAILS              ")
        new1.minsize(800, 550)
        new1.maxsize(800, 550)

        Label(new1, text="Package Details", fg="white", font="times 25 bold", bg="blue").pack()

        Label(new1, text="Luxery-", fg="purple", font="arial 15 bold").pack()
        Label(new1,
              text="24x7 Room Service, Excellent Food Quality, Entry to private pool,\n Acess to Gym, Sunset View, Sea View, Night Club Bar",
              fg="black", font="arial 12 bold").pack()
        Label(new1, text="Luxery Duo-", fg="purple", font="arial 15 bold").pack()
        Label(new1,
              text="Double Room, 24x7 Room Service, Excellent Food Quality,\n Entry to private pool, Acess to Gym, Sunset View, Sea View",
              fg="black", font="arial 12 bold").pack()
        Label(new1, text="Superior-", fg="purple", font="arial 15 bold").pack()
        Label(new1, text="16x7 Room Service, Excellent Food Quality, Entry to pool,\n Acess to Gym",
              fg="black", font="arial 12 bold").pack()
        Label(new1, text="Family Package-", fg="purple", font="arial 15 bold").pack()
        Label(new1, text="12X7 Room Service, Double Room, Entry to Pool", fg="black", font="arial 12 bold").pack()
        Label(new1, text="Couple Package-", fg="purple", font="arial 15 bold").pack()
        Label(new1, text="12X7, Single Room, Candle Light Dinner, Entry to Pool", fg="black",
              font="arial 12 bold").pack()
        Label(new1, text="Tourist Package-", fg="purple", font="arial 15 bold").pack()
        Label(new1, text="20x7 Room Service, Single Room, Entry to Pool,\n Guide also Available", fg="black",
              font="arial 12 bold").pack()

        #root.mainloop()

    Button(new, text="More Info", fg="white", bg="red", width=10, font="bold", command=moreinfo).grid(row=11, column=2)

    # Button(root, text="Add item ", command=add).pack()

    #root.mainloop()



room=PhotoImage(file=r'C:\\Users\\Lenovo\\Documents\\Project\\pic1.png')
room1=Label(image=room)
room1.pack(fill="x")

Label(root,text="Welcome To The Imperial Hotel Booking",font="times 50 bold",fg="red",bg="pink").place(x=250,y=100)

booknow=PhotoImage(file=r'C:\\Users\\Lenovo\\Documents\\Project\\BookNow.png')
book=Label(image=booknow)

bookbutton=Button(root,image=booknow,command=window)
bookbutton.place(x=650,y=250)

checkin=PhotoImage(file=r'C:\\Users\\Lenovo\\Documents\\Project\\CheckIn.png')
check=Label(image=checkin)



def secondwindow():

    new2 = Toplevel(root)
    new2.iconbitmap(r'C:\\Users\\Lenovo\\Documents\\Project\\logo.ico')
    new2.title("                                                                         Check In              ")
    new2.minsize(744, 433)
    new2.maxsize(744, 433)

    Label(new2,text="CHECK IN",fg="purple",font="times 25 bold").grid(row=0,column=0)
    Label(new2,text="User Name",fg="black",font=" times 15 bold").grid(row=1,column=0)
    Label(new2, text="password",fg="black", font="times 15 bold").grid(row=2, column=0)

    username = StringVar()
    password = StringVar()

    username1 = Entry(new2, textvariable=username,width=25).grid(row=1,column=1)
    password1 = Entry(new2, textvariable=password, width=25).grid(row=2, column=1)
    def second():
        '''if name.get() == username.get():
            password.get() == lbl'''
        tmsg.showinfo("checked in", "You Have Sucessfully Checked In")


    Button(new2, text="  SUBMIT  ", fg="white", width=20, bg="red", font=" bold", command=second).grid(row=3, column=2)



checkbutton=Button(root,image=checkin,command=secondwindow)
checkbutton.place(x=650,y=350)



exit=PhotoImage(file=r'C:\\Users\\Lenovo\\Documents\\Project\\Exit.png')
exit1=Label(image=exit)
exitbutton=Button(root,image=exit)
exitbutton.place(x=1300,y=650)
exitbutton.bind('<Button-1>',quit)


def Contact():
    value=tmsg.showinfo("contact us","contact us on 3535345343")
    if value=="ok":
        tmsg.showinfo("Contact Us","Thankyou for contacting us")

contact=PhotoImage(file=r'C:\\Users\\Lenovo\\Documents\\Project\\BookNow.png')
contact1=Label(image=contact)
contactbutton=Button(root,image=contact,command=Contact)
contactbutton.place(x=25,y=15)

Label(root,text="Address:-ITC Grand Goa, a Luxury Collection Hotel & Spa, Goa",font="arial 15 bold",bg="black",fg="white").place(x=250,y=185)


def check_out():
    new3=Toplevel(root)
    new3.iconbitmap(r'C:\\Users\\Lenovo\\Documents\\Project\\logo.ico')
    new3.title("                                                                         Check Out               ")
    new3.minsize(744, 433)
    new3.maxsize(744, 433)

    Label(new3,text="CHECK OUT",fg="purple",font="times 25 bold").grid(row=0,column=0)
    Label(new3,text="User Name",fg="black",font=" times 15 bold").grid(row=1,column=0)
    Label(new3, text="password",fg="black", font="times 15 bold").grid(row=2, column=0)

    username=StringVar()
    password=StringVar()

    usename1=Entry(new3,textvariable=username,width=25).grid(row=1,column=1)
    password1=Entry(new3,textvariable=password, width=25).grid(row=2, column=1)
    def third():
        #if x==username1.get()
        #lbl==password1.get():
            tmsg.showinfo("Checked Out","You Have Sucessfully Checked Out")

    Button(new3, text="  SUBMIT  ", fg="white", width=20, bg="red", font=" bold", command=third).grid(row=3, column=2)


checkout=PhotoImage(file=r'C:\\Users\\Lenovo\\Documents\\Project\\CheckOut.png')
checkout1=Label(image=checkout)
checkoutbutton=Button(root,image=checkout,command=check_out)
checkoutbutton.place(x=650,y=450)


root.mainloop()