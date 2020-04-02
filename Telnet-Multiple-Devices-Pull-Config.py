import getpass
import telnetlib

#enter username and password
user = raw_input("Enter your Telnet Username: ")
password = getpass.getpass()

#opens a file with the IP addresses of the Cisco devices
file = open("Switch_IP_Address.txt")

for line in file:
    print "Getting Running config from" + (line)
    HOST = line
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
#sets terminal length to 0 so that all the config can be displayed
    tn.write("terminal length 0\n")
    tn.write("enable\n")
    tn.write("cisco\n")
    tn.write("sh run\n")
    tn.write("exit\n")
#save the output to a file for each devices
    readoutput = tn.read_all()
    saveoutput = open("switch" + HOST, "w")#open a file for the config
    saveoutput.write(readoutput)#write the config to the new file
    saveoutput.close# close the file
