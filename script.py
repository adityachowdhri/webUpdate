from helper import *
import time

# Logic to do 
while True:
    time.sleep(3)
    if not checkWebsites():
        print("Website change detected")
        updateLists()
        print(getWebsites())
    else:
        index = 0
        for website in getWebsites():
            newHash = createHash(website)
            if getHashArray()[index] == newHash:
                print("No change to " + website)
            else:
                updateHashArray(index, newHash)
                sendEmail(getHashArray()[index], "kavitastarot@gmail.com", "hdkr mdjl bttz jcml", ["adityachowdhri123@gmail.com"])
                print("Changs made to " + website + " with new hash " + getHashArray()[index]) 
            index += 1










