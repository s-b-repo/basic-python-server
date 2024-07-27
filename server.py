import socket

def start_server(host='localhost', port=12345):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    
    # Enable the server to accept connections (max 5 clients in the waiting queue)
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    while True:
        # Accept a new connection
        client_socket, address = server_socket.accept()
        print(f"Connected to {address}")
        
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        print(f"Received message: {data}")
        
        # Send a response to the client
        response = "Message received"
        client_socket.send(response.encode())
        
        # Close the client socket
        client_socket.close()

if __name__ == "__main__":
    start_server()
