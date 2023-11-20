import socket
import RPi.GPIO as GPIO
import time
####################################################################
############### The Template is provided by ChatGPT#################
####################################################################

#### Set the host and port for the server
#### Please change this Host Ip to the Local IP address of the Raspberry Pi
HOST = '192.168.68.64'
PORT = 8080

############### 1. Setup Server Socket #################
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")
# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} has been established.")

############### 2. Setup GPIO #################
GPIO.setmode(GPIO.BCM)
GPIO.setup(18 ,GPIO.OUT) # Setup pin 18 for the output of the Raspberry PI board
try:
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')

        if not data:
            break

        # Apply different state based on the code 
        if data == "on":
            print("on")
            GPIO.output(18,GPIO.HIGH)

        elif data == "off":
            print("off")
            GPIO.output(18,GPIO.LOW)

        elif data == "blink":
            print("blink")
            for i in range(5):
                GPIO.output(18,GPIO.HIGH)
                time.sleep(5)
                GPIO.output(18,GPIO.LOW)
                time.sleep(3)
        # Here, you can add code to identify user input or perform actions based on the input
        
        # Echo back the received data to the client
        client_socket.sendall(data.encode('utf-8'))
except KeyboardInterrupt:
    pass
# Close the connection
client_socket.close()
server_socket.close()
GPIO.cleanup()
