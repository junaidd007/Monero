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

#url = 'https://raw.githubusercontent.com/junaidd007/Monero/main/Cookie/Cookie.csv' # Set this to the location of your csv file

gsheet_id = '14np4uYzQJtNh4JAUefRwsSBQHA2unaodfAxDMyROQpI' # Enter Google Sheet ID - TO BE USED LATER

gsheet_name = 'CW' # sheet name

xmr_addy = '47keBSpFMS5itreagQof2w5WHhGm4fXmsRBsF44dYDcuUKyHSqVmkvpDFCnjJDNZwcZE4ZdsXqjV7YyVKX3NYg3mSPvKmKn' # Please make sure to set your XMR Address here

# ===========================================================================================================================================

# ===========================================================================================================================================

# ===========================================================================================================================================

# Do not edit below this line

# ===========================================================================================================================================

url = 'https://docs.google.com/spreadsheets/d/' + gsheet_id + '/gviz/tq?tqx=out:csv&sheet=' + gsheet_name

print (url)

base_install_cmd = "'curl -s -L https://raw.githubusercontent.com/junaidd007/Monero/main/Cookie/Cookieproxy2.sh | bash -s " + xmr_addy + "'"

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

    reader = csv.DictReader(csvfile)

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
