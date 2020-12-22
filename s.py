import pyttsx3
from colorama  import init
from termcolor import cprint,colored
from time import sleep
import PyPDF2
import pyfiglet 
init()
cprint(colored('****PDF READER****','white','on_red'))


a=pyfiglet.figlet_format('PDF READER')

init()


engine=pyttsx3.init('sapi5') #SAPI5 IS THE WINDOWS API FOR IN-BUILT VOICES OF WINDOWS
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[2].id)

def speak(text):
	engine.say(text)
	engine.runAndWait()






# F=open('sample.pdf','rb')
# pdfr=PyPDF2.PdfFileReader(F)

# page=pdfr.numPages
# print('No of pages in pdf :',page)

# for i in range(page):
# 	t=pdfr.getPage(i)
# 	text=t.extractText()
# 	speak(text)



    
    
