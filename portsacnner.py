#!/bin/env python3
# import Libraries to the program.

import nmap # nmap
import ipaddress # ipaddress
import re # regular expression
import datetime # date & time
import pyTextColor # text decorations

# pyTextColor Variables
pytext = pyTextColor.pyTextColor() # assign a variable for pyTextColor Library 
color = pytext.color # assign a variable for color
reset = pytext.reset # assign a variable for reset
style = pytext.style # assign a variable for style

# banner
print(r""" ____           _             
|  _ \ __ _ ___(_)_   _  __ _ 
| |_) / _` / __| | | | |/ _` |
|  __/ (_| \__ \ | |_| | (_| |
|_|   \__,_|___/_|\__, |\__,_|
                  |___/       
 ____                                                _             
|  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___  _ __ ___ (_)_ __   __ _ 
| |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \| '_ ` _ \| | '_ \ / _` |
|  __/| | | (_) | (_| | | | (_| | | | | | | | | | | | | | | | (_| |
|_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|_| |_| |_|_|_| |_|\__, |
                 |___/                                       |___/ """)
print("\n")
print("#" * 58)
print("\n* Copyright of Pasiya Programming, 2022")
print("\n* https://www.pasiyaprogramming.com")
print("\n* https://www.youtube.com/pasiyaprogramming")
print("\n")
print("Before you begin you need to install requirements. If you already install skip this process.")
print(f'Run {color("red")}{style("bold")}pip install -r requirements.txt{reset()} to install requirements.') 
print("\n")
print("#"* 58)

time = datetime.datetime.now() # assign a variable for datetime Library 
# Initialising the port numbers, will be using the variables later on.
port_min = 0  # minimum port number
port_max = 65535 # maximum port number
# Regular Expression Pattern to extract the number of ports you want to scan.
# You have to specify <lowest_port_number>-<highest_port_number> (ex 10-100)
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

# Ask user to input the ip address the want to scan.
while True:
	set_target = input("Enter ip address: ")
	# if we enter an invalid ip address the try except block will go to the exept block and say Incorrect ip address try again!!!
	try:
		ip_address = ipaddress.ip_address(set_target)
		# The following line will only execute if the ip is valid.
		break
	except:
		print(f'{color("red")}Incorrect ip address try again!!!{reset()}')

while True:
# You can scan 0-65535 ports. This scanner is basic and doesn`t use multithreading so scanning all the ports in not advised.
	print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 21-80)")
	port_range = input("Enter begin-end port: ")
	# We pass the port numbers in by removing extra spaces that people sometimes enter. So if you enter 80 - 90 instead of 80-90 the program will still work.
	port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
	if port_range_valid:
	# We're extracting the low end of the port scanner range the user want to scan.
		port_min = int(port_range_valid.group(1))
		# We're extracting the upper end of the port scanner range the user want to scan.
		port_max = int(port_range_valid.group(2))
		break
print("\n")
print("#" * 58)

# nmap scanning process
scanner = nmap.PortScanner() # assign a variable for nmap port scanner.

print(f'Scan starting now. {time}')
print("\n")
# We`re looping over all of the ports in the specified range.
for i in range(port_min,port_max+1):

	res = scanner.scan(set_target,str(i)) # assign a variable for scan
	res = res['scan'][set_target]['tcp'][i]['state']
	if 'open' in res: # check state in res variable
		print(f'port {style("bold")}{i}{reset()} is {style("bold")}{color("cyan")}{res}{reset()}.') # print open ports.
	else:
		print(f'port {style("bold")}{i}{reset()} is {style("bold")}{color("red")}{res}{reset()}.') # print close ports.

# program ending
print("\n")
print(f'Scan completed successfully. {time}')
print("#" * 58)	
