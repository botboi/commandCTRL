import socket
target_host = "0.0.0.0"
target_port = 9999

#create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

#send data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive data

responce = client.recv(4096)

print responce
