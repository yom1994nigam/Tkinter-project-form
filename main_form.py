import tkinter as tk
import sqlite3
from PIL import ImageTk as itk
from tkinter import *
import PIL
from PIL import Image, ImageTk
from PIL import Image, ImageTk
from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt
import random
import pycountry
import unicodedata
import universities
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import re
from functools import partial
import functools
import pyttsx3
import time
import chardet
import phonenumbers
from phonenumbers import COUNTRY_CODE_TO_REGION_CODE
import smtplib

def country_func(list1):
    for country in pycountry.countries:
        list1.append(country.name)
    list1.sort()
    for i in range(len(list1)):
        list1[i]=unicodedata.normalize('NFKD',list1[i]).encode('ascii','ignore')

def create_random_captcha_text(captcha_string_size=3):
    number_list = ['0','1','2','3','4','5','6','7','8','9']
    alphabet_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    captcha_string_list = []
    base_char = alphabet_lowercase + alphabet_uppercase + number_list
    for i in range(captcha_string_size):
        char = random.choice(base_char)
        captcha_string_list.append(char)
    captcha_string = ''    
    for item in captcha_string_list:
        captcha_string += str(item)
    return captcha_string

def create_image_captcha(captcha_text):
    image_captcha = ImageCaptcha()
    image = image_captcha.generate_image(captcha_text)
    image_file = "./captcha_"+captcha_text + ".png"
    image_captcha.write(captcha_text, image_file)
    print(image_file + " has been created.")

def destroy():
    root.destroy()

def generateotp(captcha_string_size=5):
    number_list = ['0','1','2','3','4','5','6','7','8','9']
    captcha_string_list=[]
    base_char=number_list
    for i in range(captcha_string_size):
        char=random.choice(base_char)
        captcha_string_list.append(char)
    captcha_string=''
    for item in captcha_string_list:
        captcha_string+=str(item)
    return captcha_string

def sendotp(otpvalue,email):
        print("hii")
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login("yyom.nigam123@gmail.com", "*****") 
        message = otpvalue
        s.sendmail("yyom.nigam123@gmail.com",email, message) 
        s.quit() 

class ScrollFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent) # create a frame (self)

        self.canvas = tk.Canvas(self, borderwidth=0)          #place canvas on self
        self.viewPort = tk.Frame(self.canvas)                    #place a frame on the canvas, this frame will hold the child widgets 
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self 
        self.canvas.configure(yscrollcommand=self.vsb.set)                          #attach scrollbar action to scroll of canvas
        self.vsb.pack(side="right", fill="y")                                       #pack scrollbar to right of self
        self.canvas.pack(side="left", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window((3,3), window=self.viewPort, anchor="nw",            #add view port frame to canvas
                                  tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind("<Configure>", self.onCanvasConfigure)                       #bind an event whenever the size of the viewPort frame changes.

        self.onFrameConfigure(None)                                                 #perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width = canvas_width)            #whenever the size of the canvas changes alter the window region respectively.


class Example(tk.Frame):
    def database(self):
        print("Now we are in database congrates")
        connection = sqlite3.connect("tkinter_form.db") 
        crsr = connection.cursor() 
        fname=self.entry_0.get()
        lname=self.entry_1.get()
        rollno=self.entry_rollno.get()
        email=self.entry_2.get()
        if self.var.get()==0:
        	sex=""

        elif self.var.get()==1:
            sex="male"
        elif self.var.get()==2:
            sex="female"

        dob=self.cal.get()
        country=self.Country.get()
        insti=institute.get()
        if self.var1.get()==1:
            java="Yes"
        if self.var1.get()==0:
            java="No"
        if self.var2.get()==1:
            c="Yes"
        if self.var2.get()==0:
            c="No"
        if self.var3.get()==1:
            cpp="Yes"
        if self.var3.get()==0:
            cpp="No"
        if self.var4.get()==1:
            Ruby="Yes"
        if self.var4.get()==0:
            Ruby="No"
        if self.var5.get()==1:

            python="Yes"
        if self.var5.get()==0:
            pyhton="No"

        phone_code=self.phonecode.get()
        mobile_number=self.phonenumber.get()
        db_cpi=self.entry_cpi.get()
        db_degree=self.entry_degree.get()
        db_class12=self.entry_class12.get()
        db_class10=self.entry_class10.get()
        crsr.execute("insert into Form_Entries values (?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (fname,lname,rollno,email,sex,dob,country,insti,c,cpp,Ruby,python,java,
                        phone_code,mobile_number,db_degree,db_cpi,db_class12,db_class10)) 
        connection.commit() 
        connection.close() 
        root.destroy()
        print("Data entered into database correctly thanks....")


    def new_pop_up_destroy(self):
        self.new_pop_up.destroy()
    def otp_destroy(self):
        self.otp_pop.destroy()

    def update_clock(self):
        now=self.time+1
        self.time=self.time+1
        minutes=now//60
        seconds=now-minutes*60
        if minutes==5:
            self.otp_destroy()
            root.destroy()
        else:
            self.label.configure(text='%02d:%02d'%(minutes,seconds))
            self.otp_pop.after(1000, self.update_clock)

    def otp_check(self):
        print(self.otp_value_enter)
        print(self.stringotp)
        if self.otp_value_enter.get()==self.stringotp:
            self.otp_pop.destroy()
            self.database()
        else:
            self.show_eror(12)


    def otp_verification(self):

        self.otp_pop=tk.Toplevel(root)
        self.otp_value_enter=StringVar()
        self.otp_pop.title("OTP VERIFICATION")
        self.time=0
        self.otp_pop.geometry('400x300')
        self.label = tk.Label(self.otp_pop,text="",font=("bold",13))
        self.label_otp=tk.Label(self.otp_pop,text="Enter Otp sent on Email id within 5 minutes",font=("bold",12))
        self.label_otp.place(x=30,y=50)
        self.otp_entry_value=tk.Entry(self.otp_pop,textvar=self.otp_value_enter)
        self.otp_entry_value.place(x=100,y=80)

        self.otp_tag=tk.Label(self.otp_pop,text="OTP",font=("bold,12"))
        self.otp_tag.place(x=60,y=80)
        self.otp_submit_button=tk.Button(self.otp_pop, width=10,text='Submit',command=self.otp_check,bg='brown',fg='white')
        self.otp_submit_button.place(x=120,y=120)
        self.label.pack()
        self.update_clock()



    def captcha_check(self):
        if self.captcha_text==self.entry_captcha.get():
            self.pop_up.destroy()
            self.stringotp=generateotp()
            sendotp(self.stringotp,self.entry_2.get())
            self.otp_verification()

        else:
            self.new_pop_up=tk.Toplevel(self.pop_up)
            self.new_pop_up.geometry('300x300')
            self.new_label_captcha=tk.Label(self.new_pop_up,text="Please Enter Correct Captcha",font=("bold", 10))
            self.new_label_captcha.place(x=50,y=50)
            self.new_button_captcha=tk.Button(self.new_pop_up,width=10,text="Ok",command=self.new_pop_up_destroy,bg='brown',fg='white')
            self.new_button_captcha.place(x=100,y=100)
    
    def audio(self):
        engine = pyttsx3.init()
        engine.say(self.captcha_text)
        engine.runAndWait()

    def refersh(self):
        self.captcha_text = create_random_captcha_text()
        create_image_captcha(self.captcha_text)
        self.img = ImageTk.PhotoImage(Image.open("captcha_"+self.captcha_text + ".png"))
        self.panel.config(image=self.img)


    def captcha_verification(self):
        self.b_clear["state"]="disabled"
        self.b_submit["state"]="disabled"
        self.pop_up=tk.Toplevel(self)
        self.pop_up.wm_title("Captcha Verification")
        self.pop_up.geometry('500x300')
        self.captcha_value=StringVar()
        self.captcha_text = create_random_captcha_text()
        create_image_captcha(self.captcha_text)
        self.img = ImageTk.PhotoImage(Image.open("captcha_"+self.captcha_text + ".png"))
        self.panel=tk.Label(self.pop_up, image = self.img)
        self.panel.place(x=175,y=30)

        self.audio_button=tk.Button(self.pop_up, width=10,text='Audio',command=self.audio,bg='brown',fg='white')
        self.audio_button.place(x=330,y=60)

        self.photo = PhotoImage(file = r"refresh.png") 
        self.photoimage = self.photo.subsample(25,25) 

        self.refresh_button=tk.Button(self.pop_up,image=self.photoimage,command=self.refersh)
        self.refresh_button.place(x=340,y=30)

        self.label_captcha=tk.Label(self.pop_up,text="Enter Captcha",font=("bold", 13))
        self.label_captcha.place(x=193,y=120)

        self.entry_captcha=tk.Entry(self.pop_up,textvar=self.captcha_value)
        self.entry_captcha.place(x=180,y=160)

        self.captcha_submit=tk.Button(self.pop_up, width=10,text='Submit',command=self.captcha_check,bg='brown',fg='white')
        self.captcha_submit.place(x=200,y=190)
    
    def enable(self):

        self.b_clear["state"]="normal"
        self.b_quit["state"]="normal"
        self.b_submit["state"]="normal"

    def clear(self):
        self.entry_0.delete(0, 'end')
        self.entry_1.delete(0, 'end')
        self.entry_2.delete(0, 'end')
        self.radio1.deselect()
        self.radio2.deselect()
        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var.set(0)
        self.phonecode.set("Code")
        self.entry_phone.delete(0, 'end')
        self.entry_cpi.set("0.0")
        self.entry_class12.delete(0,'end')
        self.entry_class10.delete(0,'end')
        self.Country.set("Select Country")
        self.entry_degree.delete(0,'end')
        institute.set("Select institute")

    def lock_entries(self):
        self.entry_0["state"]="disabled"
        self.entry_1["state"]="disabled"
        self.entry_2["state"]="disabled"
        self.radio1["state"]="disabled"
        self.radio2["state"]="disabled"
        self.label_country["state"]="disabled"
        self.label_institute["state"]="disabled"
        self.entry_class12["state"]="disabled"
        self.entry_class10["state"]="disabled"
        self.entry_degree["state"]="disabled"
        self.entry_code["state"]="disabled"
        self.entry_cpi["state"]="disabled"
        self.prog_java["state"]="disabled"
        self.prog_C["state"]="disabled"
        self.prog_Cpp["state"]="disabled"
        self.prog_Ruby["state"]="disabled"
        self.prog_python["state"]="disabled"
        self.entry_phone["state"]="disabled"
        self.cal["state"]="disabled"
        self.captcha_verification()

    def clear_data(self):
        self.b_clear["state"]="disabled"
        self.b_quit["state"]="disabled"
        self.b_submit["state"]="disabled"
        pop_up=tk.Tk()
        pop_up.geometry('500x200')
        pop_up.title("Message")
        tk.Label(pop_up,text="Sure You Want to Clear the form Entries",font=("bold", 10)).pack(side="top", fill="x", pady=10)
        y=tk.Button(pop_up,text="Yes",command=lambda : [pop_up.destroy(),self.clear(),self.enable()])
        n=tk.Button(pop_up,text="No",command=lambda : [pop_up.destroy(),enable(1)])
        y.place(x=190,y=50)
        n.place(x=250,y=50)
        pop_up.mainloop()


    def show_eror_destroy(self):
        self.eror_pop_up.destroy()


    def show_eror(self,case):
        self.eror_pop_up=tk.Toplevel(root)
        self.eror_pop_up.title("Error")
        self.eror_pop_up.geometry('500x300')
        if case==1:
            string="Full Name"
        elif case==2:
            string="Correct Email Id"
        elif case==3:
            string="Sex"
        elif case==4:
            string="Country"
        elif case==5:
            string="Institute"
        elif case==6:
            string= "Language"
        elif case==7:
            string="Phone Number"
        elif case==8:
            string="Degree"
        elif case==9:
            string="CPI"
        elif case==10:
            string="Class 12 Percentage"
        elif case==11:
            string="Class 10 Percentage"
        elif case==12:
            string="Correct Otp"
        elif case==13:
            string="Correct CPI/Percentage"
        elif case==14:
            string="Correct 12 Percentage"
        elif case==15:
            string="Correct 10 Percentage"
        elif case==16:
            string="Roll Number"


        string ="Please Enter " + string 
        eror_label_captcha=tk.Label(self.eror_pop_up,text=string,font=("bold", 13))
        eror_label_captcha.place(x=160,y=120)
        b_error=tk.Button(self.eror_pop_up, text='OK',bg='brown',fg='white',command=self.show_eror_destroy)
        b_error.place(x=220,y=150)

    def check_email(self):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if re.search(regex,self.entry_2.get()):
            return 'valid'
        else:
            return 'invalid'

    def check_entries(self):
        alpha = 'a'
        flag1=0
        flag2=0
        flag3=0
        for i in range(0, 26):
            if alpha in self.entry_cpi.get():
                flag1=1
            if alpha in self.entry_class12.get():
                flag2=1
            if alpha in self.entry_class10.get():
                flag3=1
            alpha=chr(ord(alpha) + 1) 

        alpha='A'
        for i in range(0, 26):
            if alpha in self.entry_cpi.get() and flag1==0:
                flag1=1
            if alpha in self.entry_class12.get() and flag2==0:
                flag2=1
            if alpha in self.entry_class10.get() and flag3==0:
                flag3=1
            alpha=chr(ord(alpha) + 1) 


        if self.entry_0.get()=="" or self.entry_1.get()=="":
            self.show_eror(1)
        elif self.entry_2.get()=="" or self.check_email()=="invalid":
            self.show_eror(2)
        elif self.var.get()==0:
            self.show_eror(3)
        elif self.Country.get()=="Select Country":
            self.show_eror(4)
        elif institute.get()=="Select Institute":
            self.show_eror(5)
        elif self.var1.get()==0 and self.var2.get()==0 and self.var3.get()==0 and self.var4.get()==0 and self.var5.get()==0:
            self.show_eror(6)
        elif self.phonecode.get()=="Code" or self.phonenumber.get()=="":
            self.show_eror(7)
        elif self.degree.get()=="":
            self.show_eror(8)
        elif self.entry_cpi.get()=="":
            self.show_eror(9)
        elif self.entry_class12.get()=="":
            self.show_eror(10)
        elif self.entry_class10.get()=="":
            self.show_eror(11)

        elif self.rollno.get()=="":
            self.show_eror(16)
        elif flag1==1 or flag2==1 or flag3==1:
            if flag1==1:
                self.show_eror(13)
            elif flag2==1:
                self.show_eror(14)
            elif flag3==1:
                self.show_eror(15)
        else:
            self.lock_entries()

    def update_institute(event,self):
        if len(list2)>0:
            list2.clear()
        string=self.Country.get()
        print(string)
        uni = universities.API()
        init = uni.search(country = string)
        for i in init:
            list2.append(i.name)
        self.label_institute.config(value=list2)
        val=pycountry.countries.get(name=string)
        for k, vs in phonenumbers.COUNTRY_CODE_TO_REGION_CODE.items():
            if vs[0]==val.alpha_2:
                code="+"+str(k)
        self.phonecode.set(code)

    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self)
        self.Firstname=tk.StringVar()
        self.Lastname=tk.StringVar()
        self.Email=tk.StringVar()
        self.Country=tk.StringVar()
        self.var=tk.IntVar()
        self.var.set(0)
        self.rollno=tk.StringVar()
        self.var1= tk.IntVar()
        self.var1.set(0)
        self.var2=tk.IntVar()
        self.var2.set(0)
        self.var3=tk.IntVar()
        self.var3.set(0)
        self.var4=tk.IntVar()
        self.var4.set(0)
        self.var5=tk.IntVar()
        self.var5.set(0)
        self.phonecode=tk.StringVar()
        self.phonecode.set("Code")
        self.phonenumber=tk.StringVar()
        self.degree=tk.StringVar()
        self.cpi=tk.DoubleVar()
        self.class_10=tk.DoubleVar()
        self.class_12=tk.DoubleVar()
        self.captcha=tk.StringVar()


        #label_0 = tk.Label(self.scrollFrame.viewPort, text="Registration form",width=30,font=("bold",15)).grid(row=0,column=0,columnspan=6)
        label_1 = tk.Label(self.scrollFrame.viewPort, text="First Name").grid(row=1,column=0,sticky = W,pady=2)
        label_2 = tk.Label(self.scrollFrame.viewPort, text="Last Name").grid(row=2,column=0,sticky = W,pady=2)
        label_12 = tk.Label(self.scrollFrame.viewPort, text="Roll No").grid(row=3,column=0,sticky = W,pady=2)
        label_3 = tk.Label(self.scrollFrame.viewPort, text="Email").grid(row=4,column=0,sticky = W,pady=2)
        label_4 = tk.Label(self.scrollFrame.viewPort, text="Gender").grid(row=5,column=0,sticky = W,pady=2)
        label_5 = tk.Label(self.scrollFrame.viewPort, text="DOB").grid(row=6,column=0,sticky = W,pady=2)
        label_6 = tk.Label(self.scrollFrame.viewPort, text="Country").grid(row=7,column=0,sticky = W,pady=2)
        label_7 = tk.Label(self.scrollFrame.viewPort, text="Institute").grid(row=8,column=0,sticky = W,pady=2)
        label_8 = tk.Label(self.scrollFrame.viewPort, text="Programing").grid(row=9,column=0,sticky = W,pady=2)
        label_9 = tk.Label(self.scrollFrame.viewPort, text="Mobile No").grid(row=10,column=0,sticky = W,pady=2)
        label_10=tk.Label(self.scrollFrame.viewPort, text="Degree").grid(row=11,column=0,sticky = W,pady=2)
        label_11=tk.Label(self.scrollFrame.viewPort, text="CPI/Percentage").grid(row=12,column=0,sticky = W,pady=2)
        label_13=tk.Label(self.scrollFrame.viewPort, text="Class 12").grid(row=13,column=0,sticky = W,pady=2)
        label_14=tk.Label(self.scrollFrame.viewPort, text="Class 10").grid(row=14,column=0,sticky = W,pady=2)

        self.entry_0=tk.Entry(self.scrollFrame.viewPort,textvar=self.Firstname)
        self.entry_0.grid(row=1,column=1,sticky="W",columnspan=15)
        self.entry_1=tk.Entry(self.scrollFrame.viewPort,textvar=self.Lastname)
        self.entry_1.grid(row=2,column=1,sticky="W",columnspan=15)

        self.entry_rollno=tk.Entry(self.scrollFrame.viewPort,textvar=self.rollno)
        self.entry_rollno.grid(row=3,column=1,sticky="W",columnspan=15)

        self.entry_2=tk.Entry(self.scrollFrame.viewPort,textvar=self.Email)
        self.entry_2.grid(row=4,column=1,sticky="W",columnspan=15)
        self.var.set(0)

        self.radio1=Radiobutton(self.scrollFrame.viewPort, text="Male", variable=self.var, value=1)
        self.radio1.grid(row=5,column=1,sticky="W")
        self.radio2=Radiobutton(self.scrollFrame.viewPort, text="Female", variable=self.var, value=2)
        self.radio2.grid(row=5,column=2,sticky="W")

        self.cal = DateEntry(self.scrollFrame.viewPort,background='darkblue',
                    foreground='white', year=2019)
        x=self.cal.get()
        print(x)
        self.cal.grid(row=6,column=1,columnspan=10,sticky=W)
        
        list1=[]
        country_func(list1)
        self.Country.set("Select Country")
        self.label_country =ttk.Combobox(self.scrollFrame.viewPort, textvariable=self.Country,values=list1,state='readonly',width=40)
        self.label_country.grid(row=7,column=1,columnspan=15,sticky=W)

        list2=[]
        institute.set("Select Institute")
        self.label_institute=ttk.Combobox(self.scrollFrame.viewPort,textvariable=institute,values=list2,state='readonly',width=40)
        self.label_institute.grid(row=8,column=1,columnspan=15)

        
        self.prog_java=tk.Checkbutton(self.scrollFrame.viewPort ,text="java", variable=self.var1)
        self.prog_java.grid(row=9,column=1)
        self.prog_C=tk.Checkbutton(self.scrollFrame.viewPort, text=" C", variable=self.var2)
        self.prog_C.grid(row=9,column=2)
        self.prog_Cpp=tk.Checkbutton(self.scrollFrame.viewPort, text="C++", variable=self.var3)
        self.prog_Cpp.grid(row=9,column=3)
        self.prog_Ruby=tk.Checkbutton(self.scrollFrame.viewPort, text="Ruby", variable=self.var4)
        self.prog_Ruby.grid(row=9,column=4)
        self.prog_python=tk.Checkbutton(self.scrollFrame.viewPort, text="Python", variable=self.var5)
        self.prog_python.grid(row=9,column=5)

        self.entry_code=tk.Entry(self.scrollFrame.viewPort,textvar=self.phonecode)
        self.entry_code.grid(row=10,column=1,columnspan=3,sticky=W)

        self.entry_phone=tk.Entry(self.scrollFrame.viewPort,textvar=self.phonenumber)
        self.entry_phone.grid(row=10,column=2,columnspan=20,sticky=W)

        self.entry_degree=tk.Entry(self.scrollFrame.viewPort,textvar=self.degree)
        self.entry_degree.grid(row=11,column=1,sticky=W,columnspan=5)

        self.label_country.bind("<<ComboboxSelected>>",lambda event:self.update_institute(self))

        list3=[]
        i=0.0
        while(i<10.1):
            i = float("{0:.2f}".format(i))
            list3.append(str(i))
            i=i+.1
        self.cpi.set(0.0)
        self.entry_cpi=ttk.Combobox(self.scrollFrame.viewPort,textvariable=self.cpi,value=list3)
        self.entry_cpi.grid(row=12,column=1,sticky=W,columnspan=20)

        self.entry_class12=tk.Entry(self.scrollFrame.viewPort,textvariable=self.class_10)
        self.entry_class12.grid(row=13,column=1,columnspan=5,sticky=W)
        self.entry_class10=tk.Entry(self.scrollFrame.viewPort,textvariable=self.class_12)
        self.entry_class10.grid(row=14,column=1,columnspan=5,sticky=W)


        self.b_clear=tk.Button(self.scrollFrame.viewPort, text='Clear',bg='brown',fg='white',command=self.clear_data)
        self.b_clear.grid(row=16,column=2,sticky=W,pady=5)
        self.b_quit=tk.Button(self.scrollFrame.viewPort,text="Quit",width=6,bg='brown',fg='white',command=destroy)
        self.b_quit.grid(row=16,column=1,sticky=W,pady=5,padx=5)
        self.b_submit=tk.Button(self.scrollFrame.viewPort, width=15,text='Submit',command=self.check_entries,bg='brown',fg='white')
        self.b_submit.grid(row=17,column=1,sticky=W,pady=5,columnspan=8)
        self.scrollFrame.pack(side="top", fill="both", expand=True)
  
root=tk.Tk()
root.geometry('600x200')
root.title("Registration Form")
list2=[]
institute=tk.StringVar()
Example(root).pack(side="top", fill="both", expand=True)
root.mainloop()