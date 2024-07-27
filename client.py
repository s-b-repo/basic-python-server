import socket

def start_client(host='localhost', port=12345, message="Hello, Server!"):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Send a message to the server
    client_socket.send(message.encode())
    
    # Receive a response from the server
    response = client_socket.recv(1024).decode()
    print(f"Received from server: {response}")
    
    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    start_client()
