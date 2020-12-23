# Author: Gregory Brunn
# Created: 12/22/2020
# Purpose: Send Post request via SOAP to PAWS API to restart host without switching partitions
# Password for user is hard coded here so create a new user account with "set account name" in unity.  Here I used a priveledge 1 account with username:grinch password:Wh0sIc0me4YOU!
# For running as a task the prints are statements can be removed as no one would see or care. Future adding them to log file to see what breaks down should something.
#import the CSV library built in to python. No installation needed
import csv
#imports the request library. Needs to be installed. pip install requests
import requests
from requests.auth import HTTPBasicAuth
#
import time
#

  

#Defines a function to loop through the IP address supplied in the CSV file to login 
def restartService(ipAddress):
#Define user
  osUser='grinch'
  osPass='Wh0sIc0me4YOU!'
  url = "https://"+ipAddress+"/platform-services/services/RestartSystemService"
  payload="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\r\n<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">\r\n   <SOAP-ENV:Header xmlns:wsa=\"http://schemas.xmlsoap.org/ws/2004/08/addressing\">\r\n      <wsa:Action>urn:restartSystem</wsa:Action>\r\n      <wsa:MessageID>uuid:0b23619d-f88e-43cb-a6f2-e3752827dddd</wsa:MessageID>\r\n      <wsa:ReplyTo>\r\n         <wsa:Address>http://www.w3.org/2005/08/addressing/anonymous</wsa:Address>\r\n      </wsa:ReplyTo>\r\n      <wsa:To>https://server/platform-services/services/RestartSystemService .RestartSystemServiceHttpSoap11Endpoint/</wsa:To>\r\n   </SOAP-ENV:Header>\r\n   <SOAP-ENV:Body>\r\n      <restartSystem xmlns=\"http://services.api.platform.vos.cisco.com\" />\r\n   </SOAP-ENV:Body>\r\n</SOAP-ENV:Envelope>"
  headers = {
  'Content-Type': 'text/xml'
  }
  response = requests.request("POST", url, auth=HTTPBasicAuth(osUser, osPass), headers=headers, data=payload, verify=False)
  print(response.text)
  print("Done Processing on: "+ipAddress)

#Starts Main Program that will read CSV file get the IP addresses and then run them through the above function.
if __name__ == "__main__":
#Opens the CSV file
  connectionsFile=open('connections.csv')
#Pass the open csv file to the csv reader
  connectionsReader=csv.reader(connectionsFile)
#Pass Data to list and just stores it
  connectionsData=list(connectionsReader)

#Prints in loop of Site Names and IP
  for connection in connectionsData:
    print (connection)

#Drop headers for phoneData
    connectionsDataWithoutHeaders=connectionsData[1:]

#define new list of just the second element in the list which is the IP addresses 
  ipAddresses=[ipAddress[1] for ipAddress in connectionsDataWithoutHeaders]
#iterate over a single ip address in that list and sent it to our function/module to remove the ITL
  for ipAddress in ipAddresses:
    print ("Sending:"+ipAddress+" to PAWS Post function. Hold onto your butts")
    restartService(ipAddress)
#A break so you know the script is done. If you want to run this as a task remove this line and additional print statements. 
  done=input("Completed hit enter")
  
    

