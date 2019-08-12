import socket

target_host = "192.168.7.11"
target_port = 9999

# create a socket object
# socket.socket([family[, type[, proto]]])


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
client.send(b'Hello')

# receive some data
response = client.recv(4096)

print (response)
