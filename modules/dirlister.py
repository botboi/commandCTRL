import os

def run(**args):
    print "[*] In dirList module."
    files = os.listdir(".")

    return str(files)
