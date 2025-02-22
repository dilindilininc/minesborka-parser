# -*- coding: utf-8 -*-

import random
import requests
import sys
from lxml.html import fromstring

print("""
 ████     ██                                 ███████                                         
░██░██   ░██                                ░██░░░░██                                        
░██░░██  ░██  █████   █████  ██████  ██████ ░██   ░██  ██████   ██████  ██████  █████  ██████
░██ ░░██ ░██ ██░░░██ ██░░░██░░██░░█ ██░░░░██░███████  ░░░░░░██ ░░██░░█ ██░░░░  ██░░░██░░██░░█
░██  ░░██░██░███████░██  ░░  ░██ ░ ░██   ░██░██░░░░    ███████  ░██ ░ ░░█████ ░███████ ░██ ░ 
░██   ░░████░██░░░░ ░██   ██ ░██   ░██   ░██░██       ██░░░░██  ░██    ░░░░░██░██░░░░  ░██   
░██    ░░███░░██████░░█████ ░███   ░░██████ ░██      ░░████████░███    ██████ ░░██████░███   
░░      ░░░  ░░░░░░  ░░░░░  ░░░     ░░░░░░  ░░        ░░░░░░░░ ░░░    ░░░░░░   ░░░░░░ ░░░      
""")


url1 = "https://minesborka.com/index.php?do=download&id="
range1 = 3000
range2 = 3500
name = "1.18.1 | SkyBlock for Minecraft 1.18.1"

def parse():
	while True:
		for rand in range(range1, range2):
			url = f"{url1}{rand}"
			r = requests.get(url)
			if r.status_code == 200:
				tree = fromstring(r.content)
				title = tree.find(".//title").text
				print(f"{rand} Valid")
				if name in title:
					print(url + " Found!")
					sys.exit()
			else:
				print(f"{rand} Not Valid")
print('Подождите... Это займёт некоторое время!')
parse()

print('Not Found!')