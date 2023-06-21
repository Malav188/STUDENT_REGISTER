from tkinter import *
import subprocess as sp


root=Tk(className="  Addmission Form For Students")
root.configure(bg="sky blue")

root.geometry("558x300")


root.wm_resizable(False,False)


def hello():
  try:
      if nameentry.get()==''  or genderentry.get()=='' or DOBentry.get()=='' or ageentry.get()=='' or pyentry.get()=='' or rankentry.get()=='' or branchentry.get()=='' or hostelentry.get()==0:
       raise Exception
    
      else:
        
        print('''Submitting form of Information of student''')

      
        print("Format\n('name','gender','DOB','age','passing year','marit rank','branch name','hostel is 1 is yes or 0 is no')")
        print(f"{namevalue.get() ,gendervalue.get(),DOBvalue.get(), agevalue.get(), pyvalue.get() ,rankvalue.get() ,branchvalue.get(),hostelvalue.get()}") 

        with open("record.txt","a") as f:
          f.write(f"{(namevalue).get() ,gendervalue.get(),DOBvalue.get(), agevalue.get(), pyvalue.get() ,rankvalue.get() ,branchvalue.get(),hostelvalue.get()}\n")
        
        programName = "notepad.exe"
        fileName = "record.txt"
        sp.Popen([programName, fileName])
  except:
     print("ERROR \nEnter All Value First")

  
       
    

Label(text="Addmission form of L.E. college diploma year 2023",bg="sky blue",fg="black",font="comicsans 13 bold").place(x=0,y=0)

name=Label(root,text="Enter  Full Your Name" ,bg="sky blue",fg="black")
gender=Label(root,text="Enter Gender",bg="sky blue",fg="black")
DOB=Label(root,text="Enter Your DOB ",bg="sky blue",fg="black")
age=Label(root,text="Enter Your Age ",bg="sky blue",fg="black")
py=Label(root,text="Enter Your Passout Year Of 10th Standerd",bg="sky blue",fg="black")
rank=Label(root,text="Enter Your Merit Rank",bg="sky blue",fg="black")
branch=Label(root,text="Enter Branch Name Or The Branch You Are Intrested In ",bg="sky blue",fg="black")


name.place(x=0,y=25)
gender.place(x=0,y=50)
DOB.place(x=0,y=75)
age.place(x=0,y=100)
py.place(x=0,y=125)
rank.place(x=0,y=150)
branch.place(x=0,y=175)

namevalue=StringVar()
gendervalue=StringVar()
DOBvalue=StringVar()
agevalue=StringVar()
pyvalue=StringVar()
rankvalue=StringVar()
branchvalue=StringVar()
hostelvalue=IntVar()


nameentry=Entry(root,textvariable=namevalue)
genderentry=Entry(root,textvariable=gendervalue)
DOBentry=Entry(root,textvariable=DOBvalue)
ageentry=Entry(root,textvariable=agevalue)
pyentry=Entry(root,textvariable=pyvalue)
rankentry=Entry(root,textvariable=rankvalue)
branchentry=Entry(root,textvariable=branchvalue)
hostelentry=hostelvalue

nameentry.place(x=400,y=25)
genderentry.place(x=400,y=50)
DOBentry.place(x=400,y=75)
ageentry.place(x=400,y=100)
pyentry.place(x=400,y=125)
rankentry.place(x=400,y=150)
branchentry.place(x=400,y=175)


hostel=Checkbutton(text="Press This Button For \nReserving A Bed in Hostal",background="sky blue",activebackground="brown",variable=hostelvalue).place(x=375,y=200)


Button(text="Submit Your Form To L.E. College",bg="brown",fg="white" ,relief=SUNKEN, activebackground="sky blue",command=hello).place(x=368,y=240)


root.mainloop()