import socket

target_host = "0.0.0.0"
target_port = 9999

#build an object of socket.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect server
client.connect((target_host,target_port))

#send data
client.send('111')

#receive data
response = client.recv(4096)

print response