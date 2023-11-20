import socket
####################################################################
############### The Template is provided by ChatGPT#################
####################################################################

# Set the host and port where the server is running
# Please change this Host Ip to the Local IP address of the Raspberry Pi
HOST = '192.168.68.64'
PORT = 8080

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((HOST, PORT))
    print("Connected to the server.")

    while True:
        # Get user input
        message = input("Enter a value (on, off, blink) to publish (type 'exit' to quit): ")

        if message.lower() == 'exit':
            break

        # Send the data to the server
        client_socket.sendall(message.encode('utf-8'))

except ConnectionRefusedError:
    print("The server is not available. Please ensure the server is running.")
finally:
    # Close the connection
    client_socket.close()