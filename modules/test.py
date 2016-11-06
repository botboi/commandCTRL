import os
def run(**args):
    ip_list = ""
    try:
        ip = '192.168.1.120'
        ping.verbose_ping(ip, count=3)
        ip_list.append(ip)
    except socket.error, e:
        print "Ping Error:", e
    return str(ip_list)
