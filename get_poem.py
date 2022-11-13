import requests
import json

AUTHOR='Edgar Allan Poe'
POEM = 'A Dream Within A Dream'

#only certain poets and titles are available
#to see the available poets, go to (in a web browser)
# https://poetrydb.org/author
#To see which poems that author has available, go to 
# https://poetrydb.org/author/AUTHOR NAME
# e.g.: https://poetrydb.org/author/Edgar Allan Poe
#The spaces will get handled by your web browser

# A cool pythonism (introduced in Python 3): f strings
# https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings
URL = f'https://poetrydb.org/author,title/{AUTHOR};{POEM}'
result = json.loads(requests.get(URL).text)
poem = '\n'.join(result[0]['lines']) 

def functionz(author, poem):
    #going to URL
    #
    
    

