#!/usr/bin/python3
import sys
import ipaddress
from typing import Any
from miio import ChuangmiIr,DeviceException
import time
############################################
##
## Config
##############################################
ip = 'device ip'
token = 'device token'


####################NO MODIFICAR NADA MAS A PARTIR DE AQUI######
f=open('codes.txt')
codeline=f.readlines()
id = codeline[int(sys.argv[1])-1]
print('vamos a enviar el codigo numero'+  id)
try:
	ir =  ChuangmiIr(ip,token)
except:
	print ('esto ha petado sin decir nada flipa!')
print('conexion con el ir Ok procedemos a enviar el codigo  ->'  )
ir.play(id,frequency='')
print ('todo ha ido bien creo!')
