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

    hostname = "192.168.1."
    #   For DETER need to change to local address!!!!
    #   Change range to (255)
    for i in range(10):
        res = pinger(hostname + str(i))
        if res == 1:
            myList.append(hostname + str(i))
    return str(myList)
'''
test = run()
print test
'''
