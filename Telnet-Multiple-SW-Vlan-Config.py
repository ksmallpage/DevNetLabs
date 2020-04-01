import getpass
import sys
import telnetlib

user = raw_input("Enter your Telnet Username: ")
password = getpass.getpass()

for n in (12,16):#fourth octet of IP addresses of the Cisco devices
    HOST = "192.1.1." + str(n)#IP address of the Switch or Router
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    tn.write("enable\n")
    tn.write("cisco\n")#this will be your enable password
    tn.write("conf t\n")

    for n in (2, 10):#creates Vlan 2 -9
        tn.write("vlan " + str(n) + "\n")
        tn.write("name vlan_" + str(n) + "\n")

    tn.write("end\n")
    tn.write("copy run start")
    tn.write("exit\n")
