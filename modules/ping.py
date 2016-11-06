import os
def run(**args):
    myList = []
    #   Will need to change this for DETER
    #   Maybe automate to run through range -
    #   Have to figure out how to have that run without threads
    #   Because I get too many errors that way - maybe sleep(1)?
    hostname = "192.168.1.120"
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
        myList.append(hostname)
    else:
        pingstatus = "Network Error"
    return myList

test = run()

print test
