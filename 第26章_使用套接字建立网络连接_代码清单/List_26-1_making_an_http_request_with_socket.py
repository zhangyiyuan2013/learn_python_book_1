import socket

connection = socket.create_connection(('helloworldbook3.com',80))  # Open the socket
# Asd the server to send us the secret message
connection.sendall('GET /data/message.txt HTTP/1.0\r\n'.encode('utf-8'))
connection.sendall(b'Host: helloworldbook3.con\r\n\r\n')

# Receive the message the server sends back
response = bytes()
while True:
    new_data = connection.recv(4096)
    if not new_data:
        break  # Stop when there's nothing left to download
    response += new_data

print(response.decode('utf-8'))  # Display the message on the screen

connection.close()   # Close the socket connection
