import argparse
import requests
import json
import sys
from sys import argv
import os

parser = argparse.ArgumentParser()

parser.add_argument("-t",help="Ip", type=str, dest='target', required=True)

args = parser.parse_args()

lightblue =  '\033[94m'
lightgreen = '\033[92m'
clear =      '\033[0m'
boldblue =   '\033[01m'
cyan =       '\033[36m'
bold =       '\033[01m'
red =        '\033[31m'
lightcyan =  '\033[96m'
yellow =     '\033[93m'
os.system('clear')

ip  = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lightgreen+bold+"[~]"
        print(a, "D3m0ni4kTools",['GPS'])
        print(a, "Target:", data['query'])
        print(a, "ISP:", data['isp'])
        print(a, "Organisation:", data['org'])
        print(a, "City:", data['city'])
        print(a, "Region:", data['region'])
        print(a, "Region name:", data['regionName'])
        print(a, "Latitude:", data['lat'])
        print(a, "Longitude:", data['lon'])
        print(a, "Timezone:", data['timezone'])
        print(a, "Zip code:", data['zip'])
        print(" "+clear)

except KeyboardInterrupt:
        print('Exiting,See You Soon'+clear)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
    print(red+bold+"[!]"+" Need internet to use this Tools!"+clear)
    sys.exit(1)
