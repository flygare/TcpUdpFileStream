# fileClientTCP.py
__author__ = 'William'

from socket import *

# Set server ip and port
serverName = '192.168.43.28'
serverPort = 12000

# Create socket
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect to socket
clientSocket.connect((serverName, serverPort))

# Set file to request (choose from: 100, 1000, 10000, 100000, 1000000, 10000000, 100000000)
fileToRequest = "1000000"

# Send file request to server
clientSocket.send(str.encode(fileToRequest))
# Recieve requested file from server
recievedFile = clientSocket.recv(int(fileToRequest))

# Print results
print(recievedFile)
print("Length (B): "+str(len(recievedFile)))

# Save file to disk
open(fileToRequest+".txt", "wb").write(recievedFile)


# Close socket
clientSocket.close()
