import sys
import subprocess
import os
from decouple import config
import nmap


IP_NETWORK = '192.168.1.4' 
IP_DEVICE = '192.168.1.4'

proc = subprocess.Popen(['ping', IP_NETWORK], stdout=subprocess.PIPE)
proc.wait()
print(proc)
while True:
    line = proc.stdout.read()
    if not line:
        break

    print('This is line....')
    print(line.decode('utf-8'))
    connected_ip = line.decode('utf-8').split()[1]

    print(connected_ip)

    if connected_ip == IP_DEVICE:
        print('Device found!!!')
        subprocess.Popen(['say', 'A new device connected to the network!'])
    else:
        print('Device not found!!!')
        