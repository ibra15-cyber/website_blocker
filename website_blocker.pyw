import time
from datetime import datetime  as dt #from the module datetime import the class datetime

#both will do
# host_file_temp = 'hosts' #local to the folder im working in

#any of the two will do
host_file_path = "C:\\Windows\\System32\\drivers\\etc\\hosts" 
# host_file_path = r"C\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1" #a redirect local host
websites_to_block = ["www.facebook.com", "facebook.com", "fb.com", "twitter.com", "www.sakai.ug.edu.gh", "https://sakai.ug.edu.gh/portal"] #list of sites to block

while True: #this code will continue running because the condition will continue to remain true

    #because the code is using datetime.now between 8 and 16
    #if the condition is right it will keep running this code every now()
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("We are in a working hours")

        with open(host_file_path, 'r+') as file:
            content = file.read() #all the content of the file as string
            # print(content) 

            #for any item/website in our list/website_to_block
            for website in websites_to_block:
                #if the item also in the the content of the host file, pass
                #else write it into the file ie. during this working hours
                if website in content:
                    # print(website)
                    pass
                else:
                    #write the redirect string, then space, then website/item, then new line
                    file.write(redirect + " " + website + "\n") 
    # eles if we are not in the working hours i.e. betweeen 8 to 4pm
    #remove the files in the host file
    else:
        print("We are in free time") #great us we the alert message
        
        #then open the file in r and a mode 
        #this time we are not reading the whole file as string but as a list of lines
        #but because there is a possibilty the cursor is at the end after the first if block ran
        #we use seek(0) to return the cursor to the start of the file
        #then we iterate through the host line by line
        #and for each line without a website
        #rewrite them 
        #truncate the rest
        #which gives us a host file without any website
        with open(host_file_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content: #for each of the lines

                ##this code below didn't work for me
                # for website in websites_to_block:
                    # if website in line:
                    #     pass
                    # else: 
                    #     file.write(line) #wil rewrite the lines again when it finds a website in any line
                        
                    if not any(website in line for website in websites_to_block): #that has no website
                        file.write(line)                  #rewrite it again
                
            file.truncate()  #trancate the rest of the file

    
    time.sleep(5) #controls the printing every now to 5 mill
