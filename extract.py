#Extract WordPress Username 
#Author: @jomonthomaslobo

import sys
import requests
# Commandline argument count check
print("WordPress User Extractor")
print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
print("Author: @jomonthomaslobo")
print("------------------------------------------------------------------------------------------------")
print("This application is for eductional purposes only.This Application is not responsible for any ");print("misuse.")
print("------------------------------------------------------------------------------------------------")
n = len(sys.argv)
#print(sys.argv[2])
if (n == 1):
    print("Arguments are missing Usage: python3 extract.py --url <url>")
    sys.exit(1) 
if(n > 3):
    print("Too many arguments Usage: python3 extract.py --url <url>")
    sys.exit(1)
if(sys.argv[1] == "--url"):
    if(len(sys.argv[2])==0):
        print("Arguments are missing Usage: python3 extract.py --url <url>")
        sys.exit(1)
    else:
        print(" Connecting to " + sys.argv[2]) 
        initialUserLimit = 100
        x=range(initialUserLimit)
        print(" Checking First "+ str(initialUserLimit) +" users")
        for i in x:
            url = sys.argv[2] + "/?author=" + str(i)
            #print(url)
            
            r = requests.get(url)
            if(r.status_code == 200):
                print("Found User: " + str(i)+" : Username :"+r.url.split("/")[-2])
            else:
                print("User " + str(i) + " does not exist")
        print("------------------------------------------------------------------------------------------------")
        print("Checking for more users")
       # for(i=initialUserLimit+1;i<=initialUserLimit+100;i++):
        initialUserLimit+=100
        i=initialUserLimit+1
        y=range(initialUserLimit,initialUserLimit+100)
        errorCount=0
        for j in y:
            url = sys.argv[2] + "/?author=" + str(j)
            #print(url)
            r = requests.get(url)
            if(r.status_code == 200):
                 print("Found User: " + str(i)+" : Username :"+r.url.split("/")[-2])
            else:
                print("User " + str(j) + " does not exist")
                errorCount+=1
            if(r.status_code== 404):
                print("------------------------------------------------------------------------------------------------")
                print("No more users found")
                print("------------------------------------------------------------------------------------------------")
                sys.exit(1)
            if(errorCount==20):
                print("------------------------------------------------------------------------------------------------")
                print("No more users found")
                print("------------------------------------------------------------------------------------------------")
                sys.exit(1)
        print("------------------------------------------------------------------------------------------------")
        
        print("------------------------------------------------------------------------------------------------")
        print("Checking for more users")
        #for(i=initialUserLimit+1;i<=initialUserLimit+100;i++):
        initialUserLimit+=100
        #i=initialUserLimit+1
        y=range(initialUserLimit,initialUserLimit+100)
        for j in y: 
            url = sys.argv[2] + "/?author=" + str(i)
            #print(url)
            r = requests.get(url)
            if(r.status_code == 200):
                 print("Found User: " + str(i)+" : Username :"+r.url.split("/")[-2])
            else:
                print("User " + str(i) + " does not exist")
        print("------------------------------------------------------------------------------------------------")
       
        print("No more users found")


print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")

