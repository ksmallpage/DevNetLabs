import getpass
import sys
import telnetlib

HOST = "localhost"#add IP address of the switch in place of localhost
user = raw_input("Enter your Telnet Username: ")
password = getpass.getpass()

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
tn.write("exit\n")
