import socket
import threading


def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if message:
                print(f"Server: {message}")
            else:
                print("Connection closed by server.")
                break
        except ConnectionResetError:
            print("Connection reset by server.")
            break


def send_messages(sock):
    while True:
        message = input("Client: ")
        sock.sendall(message.encode())


def start_client(host='127.0.0.1', port=65432):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    send_thread = threading.Thread(target=send_messages, args=(client,))

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()


if __name__ == "__main__":
    start_client()
