#!/usr/local/bin/python
# deploy.py: Deploy Multiple VM's from csv on github

import csv # working with csv
import paramiko # SSH Client
import requests # used for Downloading the CSV file



# ===========================================================================================================================================
# VARS
# ===========================================================================================================================================

#set your URL HERE
url = 'https://raw.githubusercontent.com/junaidd007/Monero/main/vms.csv'

# Set your commands here, one per line
sshcmd = [
    #" df -h" # Only used for Testing
    "47TFyE1CiWNgcB5AMn9MSNKA4Lap9TcRwAvdbKedrK7VYWyqVTwE5qWWhW4Tdm4y2nNf9deqPdagqXWXwezwoSfPSx8jk3q"    
]



# ===========================================================================================================================================
# Do not edit below this line
# ===========================================================================================================================================

#download the latest csv file and save it as list.csv
req = requests.get(url)
url_content = req.content
csv_file = open("list.csv","wb")
csv_file.write(url_content)
csv_file.close()


with open('list.csv', 'r') as csvfile:  # opens file on desktop that we just saved
    reader = csv.DictReader(csvfile)
    for row in reader:


        print("Connecting to VM")
        print('IP Address: ', row['ip'], ' Username: ', row['user'], ' Password: ', row['pass'])

        # Make the connection
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                client.connect(hostname= row['ip'], username=row['user'], password=row['pass'])
            except:
                print( "[!] ERROR CONNECTING TO ", row['ip'])
                
            
            #If we are here we should be connected?
            for command in sshcmd:
                print("="*50, command, "="*50)
                stdin, stdout, stderr = client.exec_command(command)
                print(stdout.read().decode())
                err = stderr.read().decode()
                if err:
                    print(err)
        except:
            print( "[!] ERROR, Timed out")
            
# TODO: Delete CSV file after, but fuck it i'm lazy

