import hashlib
import urllib.request
import urllib.error
import smtplib 
import os
import urllib.parse
from urllib.request import urlopen, Request 
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
import time 
import requests


hashedArray = []
websiteList = []
#Create a hash when a website is passed
def createHash(website):
    url = urllib.request.Request(website, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    currentHash = hashlib.sha224(content.encode()).hexdigest()
    return currentHash

def websitesHash(websites):
    for website in websites:
        hashedArray.append(createHash(website))


def getHashArray():
    return hashedArray

def updateHashArray(index, newHash):
    hashedArray[index] = newHash

def sendEmail(url, senderAddress, passkey, recievers):
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 
    smtp.ehlo() 
    smtp.starttls() 
    smtp.login(senderAddress, passkey)
    msg = MIMEMultipart() 
    msg['Subject'] = "Change to " + url  
    msg.attach(MIMEText("Hurry! There was a change recently made to one of the URL's you were following!"))
    smtp.sendmail(from_addr=senderAddress, to_addrs=recievers, msg=msg.as_string()) 
    smtp.quit()

def websiteExist():
    return len(readWebsites()) != 0

def readWebsites():
    websites = []
    with open('webUpdate/websites.txt', 'r') as file:
        for line in file:
            websites.append(line.strip())
    return websites

def getWebsites():
    return websiteList

def checkWebsites():
    return set(websiteList) == set(readWebsites())

def updateLists():
    websiteList[:] = readWebsites()
    websitesHash(websiteList)



sendEmail("Hello", "kavitastarot@gmail.com", "hdkr mdjl bttz jcml", ["adityachowdhri123@gmail.com"])

websiteList = readWebsites()
websitesHash(websiteList)