import socket
taget_host = "0.0.0.0"
target_port = 9999

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send
client.sendto("AABBCC", (taget_host, target_port))

# receive

data, addr = client.recvfrom(4096)

print data
