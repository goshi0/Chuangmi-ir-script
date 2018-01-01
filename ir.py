
#!/usr/bin/python3
import sys
import ipaddress
from typing import Any
from miio import ChuangmiIr,DeviceException
import time
import json
import os
import os.path
fichero ='./codes.txt'
ip= 'Device ip'
token = 'Device token'
try:
    os.stat("codes.txt")
    print ('Existe el fichero codes.txt')
except:
	print ('No existe codes txt vamos a crearlo')
	file = open("codes.txt", "w")

num_lines = sum(1 for line in open('codes.txt'))
print ('Stored Ir Keys  ->'+ str(num_lines) )
id = num_lines + 1
ir =  ChuangmiIr(ip,token)

ir.learn(key=1)
time.sleep(10)
print (ir.read(key=1).get("code"))


with open('codes.txt', 'a') as file:
	try:
		file.write(ir.read(key=1).get("code")+ '\n')
	except:
		print('cant save the Ir code readin error')
