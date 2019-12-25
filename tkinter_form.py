import sqlite3
import tkinter as tk
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
import pyttsx3
import time
import chardet
import phonenumbers
from phonenumbers import COUNTRY_CODE_TO_REGION_CODE
import smtplib

timeleft = 30
def database(fname,lname):
	b4["state"]="disabled"
	conn=sqlite3.connect('form1.db')
	print("open databse successfully")
	conn.execute("insert into user_information values (?, ?)", (fname,lname)) 
	print("data insert into database succesfully")
	conn.commit()
	conn.close()
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
		captcha_string+=str(len)
	return captcha_string

def sendotp(otpvalue,email):
	print(email)
	print(otpvalue)
	print(type(email))
	print(type(otpvalue))
	gmail_user="yyom.nigam123@gmail.com"
	gmail_app_password = "SUNNYleone1994@"
	sent_from=gmail_user
	sent_to = email

	print(sent_to)
	sent_subject = "Otp verifaction"
	sent_body = otpvalue
	email_text = """\
	From: %s
	To: %s
	Subject: %s
	%s
	""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)
	try:
		server=smtplib.SMTP_SSL('smtp.gmail.com',465)
		server.ehlo()
		server.login(gmail_user,gmail_app_password)
		server.sendmail(sent_from,sent_to,email_text)
		server.close()
		print("Email Sent")
	except Exception as exception:
		print("Error:%s"%exception)

def value():
	global timeleft
	timeleft=timeleft-1
	print(timeleft)
	return timeleft


class App():
    def __init__(self):
        self.otp_win = tk.Tk()
        self.otp_win.title("OTP VERIFICATION")
        self.otp_win.geometry('500x300')
        #self.timestr = tk.StringVar() 
        self.label_c = tk.Label(self.otp_win, textvariable=timestr, font=("times new roman", 30), fg="black")
        self.label_c.place(x="10",y="10")

        self.label_otpp=tk.Label(self.otp_win,text="Enter Otp Send on Email Id Within 5 min",font=("bold",15))
        self.label_otpp.place(x="50",y="50")

        self.Exit = tk.Button(self.otp_win, text='Submit', width=6, height=1)
        self.Exit.place(x="210",y="150")

        self.label_otp=tk.Label(self.otp_win, text="OTP", font=("bold",10), fg="black")
        self.label_otp.place(x="120",y="100")
        self.value=tk.StringVar()
        self.entry_otp=tk.Entry(self.otp_win,text=self.value)
        self.entry_otp.place(x="165",y="100")
        self.time_var=0
        self.update_clock()
        self.otp_win.mainloop()

    def update_clock(self):
        #self.time_var=self.time_var+1
        #minutes=self.time_var/60
        #seconds=self.time_var-minutes*60
        #if minutes==1:
            #self.otp_win.destroy()
        #else:
            #self.timestr.set('%02d:%02d' % (minutes, seconds))
            #self.otp_win.after(1000, self.update_clock)
        timestr.set('%02d:%02d'%(0,value()))
        self.otp_win.after(1000, self.update_clock)



def otpverifcation():
	email=entry_2.get()
	otpvalue=generateotp()
	#sendotp(otpvalue,email)
	app=App()
	

def push():
	Firstname=entry_1.get()
	Lastname=entry_lname.get()
	sex_value=var.get()
	if sex_value==1:
		male=1
		female=0
	else:
		male=0
		female=1
	print("First Name: %s\nLast Name: %s \nmale:%s \nfemale:%s" % (Firstname,Lastname,male,female))
	otpverifcation()

def verify_captcha(captcha):
	if captcha==captcha_text:
		return True
	return False

def check_email(email):
	regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
	if re.search(regex,email):
		return 'valid'
	else:
		return 'invalid'
def enable(val):
	if val==1:
		b1["state"]="normal"
		b2["state"]="normal"
		b3["state"]="normal"
		b4["state"]="normal"
	if val==0:
		b3["state"]="normal"
	return 

def show_entry_fields():
	Firstname=entry_1.get()
	Lastname=entry_lname.get()
	email=entry_2.get()
	sex_value=var.get()
	prog_value=var1.get() or var2.get()
	captcha_value=captcha.get()
	vc_cap=verify_captcha(captcha_value)
	country=c.get()
	institute_val=institute.get()

	if Firstname=="" or Lastname=="":
		error_dialog(0)
	elif check_email(email)=="invalid":
		error_dialog(4)
	elif sex_value==0:
		error_dialog(1)
	elif country=="Select Country":
		error_dialog(2)
	elif institute_val=="Select institue":
		error_dialog(6)
	elif prog_value==0:
		error_dialog(5)
	elif vc_cap==0:
		error_dialog(3)
	else:
		b4["state"]="normal"
		b3["state"]="disabled"
		b1["state"]="disabled"
		entry_1["state"]="disabled"
		entry_2["state"]="disabled"
		entry_lname["state"]="disabled"
		check1["state"]="disabled"
		check2["state"]="disabled"
		check3["state"]="disabled"
		check4["state"]="disable"
		check5["state"]="disabled"
		entry_captcha["state"]="disabled"
		radio1["state"]="disabled"
		radio2["state"]="disabled"
		w1["state"]="disabled"
		w["state"]="disabled"
		cpi_comb["state"]="disabled"
		entry_phcode["state"]="disabled"
		button_audio["state"]="disabled"
		button_cref["state"]="disabled"
		entry_degree["state"]="disabled"
		label_code["state"]="disabled"





def error_dialog(case):
	b3["state"]="disabled"
	pop_up=tk.Tk()
	pop_up.title("Error")
	if case==0:
		tk.Label(pop_up,text="Please enter full name").pack(side="top", fill="x", pady=10)
	elif case==1:
		tk.Label(pop_up,text="Please choose sex").pack(side="top", fill="x", pady=10)
	elif case==2:
		tk.Label(pop_up,text="Please Select Country").pack(side="top", fill="x", pady=10)
	elif case==3:
		tk.Label(pop_up,text="Please enter correct captcha").pack(side="top", fill="x", pady=10)
	elif case==4:
		tk.Label(pop_up,text="Please enter correct email id").pack(side="top", fill="x", pady=10)
	elif case==5:
		tk.Label(pop_up,text="Please choose one Programming language").pack(side="top", fill="x", pady=10)
	elif case==6:
		tk.Label(pop_up,text="Please choose institute").pack(side="top",fill="x",pady=10)

	B1=tk.Button(pop_up,text="Exit",command=lambda : [pop_up.destroy(),enable(0)])
	B1.pack()
	pop_up.mainloop()
		
def clear():
	entry_1.delete(0, 'end')
	entry_lname.delete(0,'end')
	entry_2.delete(0,'end')
	entry_captcha.delete(0,'end')
	radio1.deselect()
	radio2.deselect()
	var1.set(0)
	var2.set(0)
	var3.set(0)
	var4.set(0)
	var5.set(0)
	var.set(0)
	c.set("Select Country") 
	institute.set("Select Institute")
	cpi_comb.set("0.0")
	code_val.set('code')
	label_code.delete(0,'end')
	entry_degree.delete(0,'end')
	entry_phcode.delete(0,'end')


def clear_data():
	b1["state"]="disable"
	b2["state"]="disable"
	b3["state"]="disable"
	b4["state"]="disable"
	pop_up=tk.Tk()
	pop_up.geometry('500x200')
	pop_up.title("Message")
	tk.Label(pop_up,text="Sure You Want to Clear the form Entries",font=("bold", 10)).pack(side="top", fill="x", pady=10)
	y=tk.Button(pop_up,text="Yes",command=lambda : [pop_up.destroy(),clear(),enable(1)])
	n=tk.Button(pop_up,text="No",command=lambda : [pop_up.destroy(),enable(1)])
	y.place(x=190,y=50)
	n.place(x=250,y=50)
	pop_up.mainloop()

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


def update_institute(event):
	list2=[]
	if len(list2)>0:
		list2.clear()
	string=c.get()
	uni = universities.API()
	init = uni.search(country = string)
	for i in init:
		list2.append(i.name)
	w1.config(value=list2)
	val=pycountry.countries.get(name=string)
	for k, vs in phonenumbers.COUNTRY_CODE_TO_REGION_CODE.items():
		if vs[0]==val.alpha_2:
			code="+"+str(k)
	code_val.set(code)


def ref_captcha(lsit_cap):
	captcha_text2 = create_random_captcha_text()
	list_cap[0]=captcha_text2
	create_image_captcha(captcha_text2)
	img = ImageTk.PhotoImage(Image.open("captcha_"+captcha_text2 + ".png"))
	panel.config(image=img)
	panel.image = img



def audio(list_cap):
	engine = pyttsx.init()
	engine.say(list_cap[0])
	engine.runAndWait()



root = Tk()
root.geometry('500x500')
root.title("Registration Form")

#app = Tk()

frame=Frame(root,width=500,height=500)
frame.grid(row=0,column=0)
canvas=Canvas(frame,width=500,height=500,scrollregion=(0,0,500,500))

vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(yscrollcommand=vbar.set)
canvas.pack()


Firstname=tk.StringVar()
Lastname=tk.StringVar()
Email=tk.StringVar()
captcha=tk.StringVar()
c=tk.StringVar()
cpi=tk.DoubleVar()
institute=tk.StringVar()
var = tk.IntVar()
var1= tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()
var4=tk.IntVar()
var5=tk.IntVar()
degree=tk.StringVar()
code_val=tk.StringVar()
code_val.set('code')
phone_number=tk.StringVar()
timestr=tk.StringVar()





             
label_0 = tk.Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = tk.Label(root, text="FirstName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = tk.Entry(root,textvar=Firstname)
entry_1.place(x=240,y=130)

label_lname=tk.Label(root,text="LastName",width=20,font=("bold",10))
label_lname.place(x=80,y=160)

entry_lname=tk.Entry(root,textvar=Lastname)
entry_lname.place(x=240,y=160)

label_2 = tk.Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=190)

entry_2 = tk.Entry(root,textvar=Email)
entry_2.place(x=240,y=190)

label_3 = tk.Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

var.set(0)
radio1=tk.Radiobutton(root, text="Male",padx = 5, variable=var, value=1)
radio1.place(x=225,y=230)
radio2=tk.Radiobutton(root, text="Female",padx = 20, variable=var, value=2)
radio2.place(x=290,y=230)

dob_label=ttk.Label(root, text='DOB')
dob_label.place(x=140,y=260)

cal = DateEntry(root, width=12, background='darkblue',
                    foreground='white', borderwidth=2, year=2010)
cal.place(x=240,y=260)


label_4 = tk.Label(root, text="Country",width=20,font=("bold", 10))
label_4.place(x=70,y=300)

label_5=tk.Label(root,text="Institute",width=20,font=("bold",10))
label_5.place(x=70,y=340)

list1=[]
for country in pycountry.countries:
    list1.append(country.name)
list1.sort()
for i in range(len(list1)):
	list1[i]=unicodedata.normalize('NFKD',list1[i]).encode('ascii','ignore')

c=tk.StringVar(root)
c.set("Select Country") 
w =ttk.Combobox(root, textvariable=c,values=list1,state='readonly',width=60)
w.place(x=240,y=300)

list2=[]
institute=tk.StringVar(root)
institute.set("Select Institute")
w1=ttk.Combobox(root,textvariable=institute,state='readonly',value=list2,width=60)
w1.place(x=240,y=340)

list3=[]
i=0.0
while(i<10.1):
	i = float("{0:.2f}".format(i))
	list3.append(str(i))
	i=i+.1

label_cpi=tk.Label(root,text="CPI/Percentage",width=20,font=("bold",10))
label_cpi.place(x=70,y=410)
cpi=tk.DoubleVar(0.0)
cpi_comb=ttk.Combobox(root,textvariable=cpi,value=list3,width=60)
cpi_comb.place(x=240,y=410)

label_degree = tk.Label(root, text="Degree",width=20,font=("bold", 10))
label_degree.place(x=80,y=380)
entry_degree = tk.Entry(root,textvar=degree)
entry_degree.place(x=240,y=380)

label_4 = tk.Label(root, text="Programming",width=20,font=("bold", 10))
label_4.place(x=85,y=440)
check1=tk.Checkbutton(root, text="java", variable=var1)
check1.place(x=235,y=440)
check2=tk.Checkbutton(root, text="python", variable=var2)
check2.place(x=290,y=440)
check3=tk.Checkbutton(root,text="C",variable=var3)
check3.place(x=360,y=440)
check4=tk.Checkbutton(root,text="C++",variable=var4)
check4.place(x=400,y=440)
check5=tk.Checkbutton(root,text="Ruby",variable=var5)
check5.place(x=460,y=440)


label_phn=tk.Label(root,text="Mobile No.",width=20,font=("bold",10))
label_phn.place(x=85,y=480)

label_code=tk.Entry(root,textvar=code_val,width=5,font=("bold"))
label_code.place(x=240,y=480)

entry_phcode=tk.Entry(root,textvar=phone_number)
entry_phcode.place(x=300,y=480)


b1=tk.Button(root, text='Clear',width=10,bg='brown',fg='white',command=clear_data)
b1.place(x=170,y=700)
b2=tk.Button(root,text="Quit",width=11,bg='brown',fg='white',command=root.destroy)
b2.place(x=170,y=650)
b3=tk.Button(root,text="Done",width=10,bg='brown',fg='white',command=show_entry_fields)
b3.place(x=320,y=700)
b4=tk.Button(root, text='Submit',width=10,bg='brown',fg='white',command=push)
b4.place(x=320,y=650)


captcha_text = create_random_captcha_text()
list_cap=[]
list_cap.append(captcha_text)
create_image_captcha(captcha_text)
img = ImageTk.PhotoImage(Image.open("captcha_"+captcha_text + ".png"))
panel=tk.Label(root, image = img)
panel.place(x=200,y=520)

button_audio=tk.Button(root,text="Audio",width=2,bg='brown',fg='white',command=partial(audio,list_cap))
button_audio.place(x=370,y=550)


photo = tk.PhotoImage(file ="refresh.png") 
photoimage = photo.subsample(30,30) 
button_cref=tk.Button(root,text="Refresh",image=photoimage,command=partial(ref_captcha,list_cap))
button_cref.place(x=370,y=525)

label_captcha=tk.Label(root, text='Enter Captcha',font="bold").place(x=220,y=590) 
entry_captcha=tk.Entry(root,textvar=captcha)
entry_captcha.place(x=200,y=610)
w.bind("<<ComboboxSelected>>",update_institute)
root.mainloop()
