# PAWS Restart Service Via CSV

A customer has a large amount of CUCM/ CUC/ IMP nodes that they wanted to restart in bulk. This python program was created to do that. Utilzing the PAWS API on before listed cisco products.


## Project Description

Python script takes IP address in a CSV file and iterates them in a loop to send them to a function that sends PWS XML post messages to the application via the requests library in python.  Script was created in python 3.9.1 and needs the request library to be installed via pip install requests.
The CSV file is named connections.csv and has two fields.  Site and IP. Site is not really used other than print statements in the script. IP is the more important fields.
Script was tested against CUCM and CUC nodes multiple version of 11.5


## Most Importantly
Have fun. 

