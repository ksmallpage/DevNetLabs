import getpass
import sys
import telnetlib

HOST = "localhost"#enter the IP address of the router management interface
user = raw_input("Enter your Telnet Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")#enter enable password
tn.write("conf t\n")
tn.write("int loopback 0\n")#creates loopback interface
tn.write("ip add 1.1.1.1 255.255.255.255\n")
tn.write("end\n")
tn.write("exit\n")
tn.write("copy run start\n")
