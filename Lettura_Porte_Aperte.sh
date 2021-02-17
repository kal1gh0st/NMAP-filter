#!/bin/bash

nome_file=Herno_Lesa_Masscan.txt
ip=192.1.

mkdir Open_ports
for ((i=0; i<=256; i++ ))
do
    for ((a=0; a<=3; a++ ))
    do
        if grep -w -q "$ip""$a"."$i" $nome_file
	then
            cat $nome_file | grep -w $ip"$a"."$i" > Open_ports/open_port_$ip"$a"."$i".txt
	fi
    done
done
echo "Done!!"
