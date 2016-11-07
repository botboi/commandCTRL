import os
def run(**args):
    myList = []
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

    for i in range(254):
        res = pinger(hostname + str(i))
        if res == 1:
            myList.append(hostname + str(i))
    return str(myList)
'''
test = run()
print test
'''
