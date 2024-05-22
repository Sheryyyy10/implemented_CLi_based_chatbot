import socket
import threading


def handle_client(conn, addr):
    print(f"New connection from {addr}")
    while True:
        try:
            message = conn.recv(1024).decode()
            if message:
                print(f"Client {addr}: {message}")
                response = input("Server: ")
                conn.sendall(response.encode())
            else:
                print(f"Connection closed by {addr}")
                break
        except ConnectionResetError:
            print(f"Connection reset by {addr}")
            break
    conn.close()


def start_server(host='127.0.0.1', port=65432):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()


if __name__ == "__main__":
    start_server()
