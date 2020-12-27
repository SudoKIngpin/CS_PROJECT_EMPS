#ALL OPEARTIONS EC=XCEPT MODREC WHICH IS A 
# BIG FUNCTION TO AVOID CONFUSION IT IS SHIFTED IN modfun.py

#THIS FILE CONTAINS FOLLOWING FUNCTIONS 
# 1. ADDREC()       2.DELREC     3.SEARCHREC     4.DISPREC  5. MAILFUN()

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from termcolor import cprint,colored
from colorama import init # WINDOWA PLATFORM

import mysql.connector as ms# for line 15
from time import sleep  # FOR LINE 19

from plyer import notification as nt # Notification system
from beepy import beep #Notification sound

init() #WNDOWS PLATFORM

try:
        mycon=ms.connect(host='localhost',user='root',passwd='Kali',database='Emplmgs',autocommit=True) #,autocommit=True
        cursor=mycon.cursor()

except Exception as e:
        cprint(colored("Error connecting to databse!!",'white','on_yellow'))
        sleep(4)# TIME FOR USER TO READ ERROR MESSAGE
        exit() #TERMINATING THE PROGRAM 

def addrec():
                        EmpName=input('Enter Employee name :').upper()
                        Gender=input("Enter gender [M]/[F] :").upper()
                        EmpId=input('Enter unique 5 Digit Employee ID:').upper()
                        Designation=input("Enter Designation :").upper()
                        Age=int(input('Enter age of Employee:'))
                        Emp_Mail=input("Enter E-Mail id of Employee:").lower()
                        Sal=int(input("Enter Salary of Employee :"))
                        add_query="insert into Emplrec values('{}','{}','{}','{}',{},'{}',{})".format(EmpName,Gender,EmpId,Designation,Age,Emp_Mail,Sal)
                        # print(query)
                        cursor.execute(add_query)
                        mycon.commit()
                        cprint(colored("RECORD ADDED SUCCESSULLY !",'white','on_red'))
                        nt.notify(title='Success',message='RECORDS ADDED SUCCESSULLY',app_icon='gtick.ico',timeout=3)
                        beep(sound='ping')  
                        #Notification SYSTEM 

def delrec():
                        EmpId=input("Enter unique 5 Digit Employee ID:").upper()
                        CHK_QUERY='Select * from Emplrec where EmpId="{}"'.format(EmpId)
                        cursor.execute(CHK_QUERY)
                        datachk=cursor.fetchone() #NONE IF IT IS EMPTY

                        if datachk!=None:

                                EmpName,Gender,EmpId,Designation,Age,Emp_Mail,Salary=datachk#Unpacking for storing emailid

                                del_query='Delete from Emplrec where EmpId="{}"'.format(EmpId) # NO METHOD TO CHECK/VALIDATE EMPID
                                cursor.execute(del_query)
                                mycon.commit()
                                cprint(colored("RECORD DELETED SUCCESSULLY !",'white','on_red'))
                                nt.notify(title='Success',message='Record deleted successfully',app_icon='gtick.ico',timeout=3)
                                beep(sound='ping')  

                        else:
                                cprint(colored("INVALID EMPID , ID DOES NOT EXIST IN DATABASE !",'green','on_white'))
                                nt.notify(title='Error!',message='EMPID DOES NOT EXIST IN DATABASE !',app_icon='error.ico',timeout=3)
                                beep(sound='error')  


def searchrec():
        Id=input("Enter unique 5 Digit Employee ID:").upper()
        search_q="Select * from Emplrec where EmpId='{}'".format(Id)
        cursor.execute(search_q)
        data=cursor.fetchone() #iT RETURNS NONE IF IT IS EMPTY
        if data!=None:
                # print(data)
                EmpName,Gender,EmpId,Designation,Age,Emp_Mail,Salary=data
                L=[EmpName,Gender,EmpId,Designation,Age,Emp_Mail,Salary]
                return L

        else:
                cprint(colored('INVALID ID !!, ID DOES NOT EXIST','grey','on_white'))



def disprec():
        l=[]#TO HOLD ALL RECORDS
        dis_q='Select * from Emplrec'
        cursor.execute(dis_q)
        data=cursor.fetchall() # LIST TYPE ELEMENT 

        if data!=[]:  #IF RECORDS ARE PRESENT 
                for row in data:   # iTERATING THROUGH THE RESULT SET 
                        # print(row) NOT PRINTING TUPLE , SHOWING TABLE..
                        l.append(list(row)) #CONVERTING TUPLE TO LIST(NESTED) FOR ADDING IN PRETTYTABLE
                return l

        else: # IF NO RECORDS IN DATABASE
                cprint(colored('NO RECORDS EXIST!, DATABASE EMPTY!','white','on_blue'))

def mailfun():
        EmpId=input("Enter EmpId of Employee:")
        EmpId=EmpId.upper()
        q="Select * from Emplrec where EmpId='{}'".format(EmpId)
        cursor.execute(q)
        r=cursor.fetchone()
        if r!=None:     

                        EmpName,Gender,EmpId,Designation,Age,Emp_Mail,Salary=r # UNPACKING .....

                        Msg=MIMEMultipart()
                        BOT_ID='sudocorporations@gmail.com'
                        BOT_PWD='sudo_tech@#'
                        server=smtplib.SMTP('smtp.gmail.com',587) #HOST AND PORT
                        # server.ehlo()
                        server.starttls()#Transport layer secuirity encryption
                        server.login(BOT_ID,BOT_PWD)

                        Subject=input('Enter Subject of mail:')
                        body=input('Enter body of mail:')
                        body=body+'\n'+ '\n' + "Thank you"+ '\n' +"Sudo Corporations"
                        Msg["From"]=BOT_ID
                        Msg['To']=Emp_Mail
                        Msg["Subject"]=Subject
                        Msg.attach(MIMEText(body,'plain')) #ATTACHING BODY
                        content=Msg.as_string()
                        server.sendmail(BOT_ID,Emp_Mail,content)
                        print()
                        o=f"MAIL SENT SUCCESSFULLY TO {EmpName} whose EmpID is: {EmpId}"
                        cprint(colored(o,'white','on_red'))
                        server.quit()
                        nt.notify(title='Success',message='Mail sent successfully',app_icon='gtick.ico',timeout=3)
                        beep(sound="ping") # Notification sound



        else:
                cprint(colored("INVALID EmpId !!",'white','on_green'))
                nt.notify(title='INVALID ID',message='Id does not exist in database!',app_icon='error.ico',timeout=3)
                beep(sound="error")# Notifiication sound

