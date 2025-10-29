# ssl_server.py
import socket
import ssl

HOST = '127.0.0.1'   # or '0.0.0.0' to accept external connections
PORT = 8443

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='server_cert.pem', keyfile='server_key.pem')

# Create plain socket, then accept and wrap accepted sockets (NOT wrapping the listening socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(5)
    print(f"[*] Listening on {HOST}:{PORT} (TLS) ...")

    while True:
        newsock, addr = sock.accept()
        print(f"[+] Connection from {addr}")
        # Wrap the accepted socket with SSL for this session
        try:
            with context.wrap_socket(newsock, server_side=True) as ssock:
                data = ssock.recv(4096)
                if not data:
                    print("[-] No data received")
                    continue
                print(f"[<] Received: {data.decode(errors='ignore')}")
                ssock.sendall(b"Hello from SSL server!")
        except ssl.SSLError as e:
            print(f"[!] SSL error: {e}")
        except Exception as e:
            print(f"[!] Connection error: {e}")
        finally:
            newsock.close()
