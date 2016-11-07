import os
import paramiko
import sys
import time
def run(**args):
    fileName = "seed.sh"
    myList = ['localhost']
    # Function to ping and find all hosts on a network
    def pinger(hostname):
        response = os.system("ping -c 1 " + hostname)
        # and then check the response...
        if response == 0:
            pingstatus = 1
        else:
            pingstatus = 0
        return pingstatus

    hostname = "192.168.1."
    #   For DETER need to change to local address!!!!
    #   Change range to (255)
    for i in range(1,254,1):
        res = pinger(hostname + str(i)) #+ str(i))
        if res == 1:
            myList.append(hostname + str(i))
    return myList

x = run()

print str(x)
