#!/usr/bin/python3
import subprocess
import os
nome_file = "nmap-scan-herno-lan.txt"
ip = "192.1."
l=""
m=""
output_file="Open_ports/open_port.txt"
subprocess.call(["mkdir","Open_ports"])

for i in range(0,256,+1):
        l=str(i)
        for a in range(0,4,+1):
                m=str(a)
                if subprocess.run(['grep','-w', ip + m + '.' + l ,nome_file], 
		   capture_output=True).returncode == 0:
                   with open(output_file + ip + m + '.' + l, 'w') as f:
                       o = subprocess.run(['cat', 'nmap-scan-herno-lan.txt'], text=True, capture_output=True)
                       p = subprocess.run(['grep','-w',ip + m + '.' + l ,nome_file], 
                       stdout=f, text=True, input=o.stdout)
                       print(ip + m + '.' + l)


