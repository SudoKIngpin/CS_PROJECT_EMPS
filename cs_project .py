#!/usr/bin/python3
# import mysql.connector as ms
from termcolor import colored,cprint
from colorama import init
import pyfiglet 
from basic_op import addrec,delrec,searchrec,disprec,mailfun
from modfun import modrec
from tqdm import tqdm,trange
from time import sleep
from filereader import freader
from prettytable import PrettyTable

x=PrettyTable()
init() #WINDOWS PLATFORM FOR PRINIRING COLOrs on cmd/powershell prompt!

x.field_names=['EmpName','Gender','EmpId','Designation','Age','Emp_Mail','Salary']
# ATTRIBUTES OF TABLE 


def progressbar():
	for i in trange(100):
		pass
		sleep(0.02) #LOADING INTERFACE FUNCTION


def menu():
	  cprint(colored('[1] Enter 1 to use Employee Management System ','white','on_red'))
	  print()
	  cprint(colored('[2] Enter 2 to use File Reader                  ','magenta','on_white'))
	  print()
	  cprint(colored('[3] Enter 3 to use Assistant                  ','grey','on_green'))
	  print()


a=pyfiglet.figlet_format('MENU')
print()
print('=================================================')
print(a)
menu()

choice=int(input('Enter your choice:'))
print()
print('-------------------------------------------------')

if choice==1:

		def sqlmenu():
			print(
				'''
				   [1]. ADD RECORD

				   [2]. DELETE RECORD

				   [3]. MODIFY RECORD

				   [4]. DISPLAY ALL RECORDS

				   [5]. SEARCH RECORDS

				   [6]. SEND A MAIL TO EMPLOYEE

				   [7]. EXIT THE PROGRAM''')	

		print() #FORMATTING PURPOSE
		print()#fORMATTING
		print("[!] Connecting to Database !")
		sleep(1.0)
		print("[!] Initializing Database !")
		sleep(1)
		print('[!] Loading database records !')
		progressbar()
		sleep(1)
		print('DATABASE LOADED  SUCCESSULLY !')
		cprint(colored('******EMPLOYEE MANAGEMENT SYSTEM******','white','on_red'))
		banner=pyfiglet.figlet_format('EMS')
		print(banner)
		cprint(colored("options:",'blue','on_white'))
		print()
		ans='y'
		while ans=='y' or ans=='Y':

			sqlmenu()
			menu=input("Type your option : ")

			if menu==1:
				addrec()
				print()# For  some gap b/w records and y/n input
				
			elif menu==2:
				delrec()
				print()# For  some gap b/w records and y/n input
				
			elif menu==3:
				modrec()
				print()# For  some gap b/w records and y/n input
				
			elif menu==4:
				try:
					L=disprec() #L WILL STORE NESTED LIST OF RECORDS 
					for data in L:
						x.add_row(data)
					print(x)
					x.clear_rows()
				except Exception as e: #RUNTIME ERROR IF THERE ARE NO RECORDS
					cprint(colored('ERROR!!','white','on_red'))
					print()# For  some gap b/w records and y/n input
				
			elif menu==5:
				try:
					L=searchrec() #L WILL STORE LIST OTHERWISE NONE
					x.add_row(L)
					print(x)
					x.clear_rows()
				except Exception as e:
					cprint(colored('ERROR!!','white','on_red'))
					print()# For  some gap b/w records and y/n input
				
			elif menu==6:
				try:
				 	mailfun()
				except Exception as e:
					cprint(colored("MAIL NOT SENT , PLEASE CONNECT TO INTERNET!",'white','on_blue'))
				

			elif menu==7:
				cprint(colored('BYE USER !!','white','on_red'))
				sleep(4)
				exit()
			else:
				print('Invalid option !!')
				print()# For  some gap b/w records and y/n input
				
			ans=input("Want to continue type[y], else[n] :")
			




elif choice==2:
		freader()
		
else:
		pass
