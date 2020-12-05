#Developed by PythonCoder8
#Get system info for Windows
#Windows alternative for my Github "Sysinfo" repo

import socket
from getpass import getuser
from platform import uname
from time import time
import psutil as ps
from datetime import datetime

start = time()
def get_size(bytesize, suffix="B"):
    #Scale bytes to its proper format
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytesize < factor:
            return f"{bytesize:.2f}{unit}{suffix}"
        bytesize /= factor

width = 60
titletxt = 'Windows System Info'
title = titletxt.center(width, '-')
print(title + "\n")

del width
del titletxt
del title

raminfo = ps.virtual_memory()
print('Available RAM: %s' %(get_size(raminfo.available)))
bt_timestamp = ps.boot_time()
bt = datetime.fromtimestamp(bt_timestamp)
print(f'Computer boot time: {bt.year}/{bt.month}/{bt.day} at {bt.hour}:{bt.minute}')
del timestamp
del bt
print('Computer hostname: %s'%(socket.gethostname()))
print('CPU cores: %s'%(ps.cpu_count(logical=False)))
print('CPU information: %s'%(uname().processor))
print('CPU logical processors: %s'%(ps.cpu_count(logical=True)))
print('Currently logged on user: %s'%(getuser()))
print('IPv4 address: %s'%(socket.gethostbyname(socket.gethostname())))
print('OS: %s'%(uname().system))
print('OS Version: %s'%(uname().version))
print('Total RAM: %s' %(get_size(raminfo.total)))
print('Used RAM: %s' %(get_size(raminfo.used)))
end = time()

print('\nProgram runtime: %f sec'%(end - start))
