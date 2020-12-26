import mysql.connector as ms
from colorama import init
from time import sleep

from termcolor import cprint,colored
init()
try:
        mycon=ms.connect(host='localhost',user='root',passwd='',database='Emplmgs',autocommit=True)   #,autocommit=True
        cursor=mycon.cursor()

except Exception as e:
        cprint(colored("Error connecting to databse!!",'white','on_red'))
        sleep(4)# TIME FOR USER TO READ ERROR MESSAGE
        exit() #TERMINATING THE PROGRAM 
init()

def modrec():
#EMPID HAS ALREADY UNIQUE CONSTRAINT CHECK IN MYSQL
                print(
                '''
                [1]. EmpName

                [2]. Gender

                [3]. Designation   

                [4]. Age

                [5]. Emp_Mail

                [6]. Salary

                [7]. Increase Salary by %

                [8]. Decrease Salary by %
                '''
                )


                ch=int(input('Enter your choice:'))
                EID=input("Enter unique 5 Digit Employee ID:").upper() #to match casing 

                chk_q="Select * from Emplrec where EMPID='{}'".format(EID)
                cursor.execute(chk_q)
                r=cursor.fetchone()
                if r!=None:
                        EmpName,Gender,EmpId,Designation,Age,Emp_Mail,Salary=r
                       
                        if ch==1:

                                        field="Name" # For sending in mail
                                        New_Name=input('Enter new name :').upper()
                                        query='update Emplrec set EmpName="{}" where EmpId="{}"'.format(New_Name,EID)
                                        cursor.execute(query)
                                        mycon.commit()
                                        o=f'NAME UPDATED SUCCESSULLY TO : {New_Name} '
                                        cprint(colored(o,'white','on_red'))

                        
                        elif ch==2:

                                        field="Gender"
                                        Gen=input("Enter new gender [M]/[F]:").upper()
                                        query='update Emplrec set Gender="{}" where EmpId="{}"'.format(Gen,EID)
                                        cursor.execute(query)
                                        mycon.commit()
                                        o=f"GENDER UPDATED SUCCESSULLY TO: {Gen}"
                                        cprint(colored(o,'white','on_red'))


                        
                        elif ch==3:
                                        field="Designation"
                                        Des=input("Enter New Designation:").upper()
                                        query='update Emplrec set Designation="{}" where EmpId="{}"'.format(Des,EID)
                                        cursor.execute(query)
                                        mycon.commit()
                                        o=f"DESIGNATION UPDATED SUCCESSULLY TO : {Des}"
                                        cprint(colored(o,'white','on_red'))




                        elif ch==4:
                                        field='Age'
                                        age=int(input("Enter new age:"))
                                        query='update Emplrec set Age={} where EmpId="{}"'.format(age,EID)
                                        cursor.execute(query)
                                        mycon.commit()
                                        o=f"AGE UPDATED SUCCESSULLY TO :{age}"
                                        cprint(colored(o,'white','on_red'))



                        elif ch==5:
                                        field="MAIL ID"
                                        mail_id=input("Enter new mail id :").lower()

                                        query='update Emplrec set Emp_Mail="{}" where EmpId="{}"'.format(mail_id,EID)
                                        cursor.execute(query)
                                        mycon.commit()
                                        o=f'MAIL ID UPDATED SUCCESSULLY TO:{mail_id}'
                                        cprint(colored(o,'white','on_red'))



                        elif ch==6: 
                                        field="Salary"
                                        sal=int(input("Enter updated Salary :"))
                                        sal_q="update Emplrec set Salary={} where EmpId='{}'".format(sal,EID)
                                        cursor.execute(sal_q)
                                        mycon.commit()
                                        o=f"SALARY UPDATED SUCCESSULLY TO: {sal}"
                                        cprint(colored(o,'white','on_red'))


                        elif ch==7:
                                per=int(input("Enter the % by which salary to be Increased:"))
                                r_per=per/100
                                in_sal=int((Salary)+(Salary*r_per))
                                q="Update Emplrec set Salary={} where EmpId='{}'".format(in_sal,EID)
                                cursor.execute(q)
                                mycon.commit()
                                o=f"SALARY HAS BEEN INCREASED BY {per}%"
                                cprint(colored(o,'white','on_red'))



                        elif ch==8:
                                per=int(input("Enter the % by which salary to be Decreased:"))
                                r_per=per/100
                                de_sal=int((Salary)-(Salary*r_per))
                                # print(de_sal)
                                q="Update Emplrec set Salary={} where EmpId='{}'".format(de_sal,EID)
                                cursor.execute(q)
                                mycon.commit()
                                o=f"SALARY HAS BEEN DECREASED BY {per}%"
                                cprint(colored(o,'white','on_red'))




                        else:
                                cprint(colored("INVALID OPTION!!",'green','on_white'))


                else:
                        cprint(colored("INVALID EMPLOYEE ID , ID DOES NOT EXIST IN DATABASE",'white','on_red'))















