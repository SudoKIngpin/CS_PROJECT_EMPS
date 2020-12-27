import requests 
import json # for data to be converted in json format
from  plyer import notification
from termcolor import cprint,colored
from  colorama import init
from time import sleep
from beepy import beep


def coronainfo():
	init()  # Windows color formatting
	try:
		a=requests.get('https://corona-rest-api.herokuapp.com/Api/India')
	except:
		cprint(colored('Please connect to internet !','white','on_red'))
		sleep(4)
		print()
		cprint(colored('Terminating the program....,','white','on_green'))
		exit()

	t=a.json() # Converting above data to json format

	

	''' JavaScriptObjectNotation is a standardized format for reading
	and transfering data it is readable by both human and machine
	'''
	 # {'country': 'India', 'cases': 10188204, 'todayCases': 18386, 
	 # 'deaths': 147656,
	 #  'todayDeaths': 277, 'recovered': 9760664, 'active': 279884,
	 #   'critical': 8944,
	 #  'casesPerOneMillion': 7348, 'deathsPerOneMillion': 106, 
	 #  'totalTests': 167159289, '
	 #  testsPerOneMillion': 120556}
	# t is a(nested)dictionary containing all info about covid cases
	#with key "Success"
	di=t["Success"]
	
	info=f'''
Country :{di['country']}
Total Cases: {di['cases']}
Cases Active: {di['active']}
Cases Today: {di['todayCases']}
Total Deaths: {di['deaths']}
Deaths Today: {di['todayDeaths']}
Critical : {di['critical']}
Recovered : {di['recovered']}
Tests Today: {di['totalTests']}
	'''

	


	notification.notify(title="Covid Info India",message=info,app_icon='update.ico',timeout=15,app_name="CovidStats")
	beep(sound='ready')
# coronainfo()
				 


