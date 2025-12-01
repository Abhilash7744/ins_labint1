#after entering into Internal2 Folder , use these commands

#sudo apt install openssl -y
'''openssl req -newkey rsa:2048 -nodes -keyout server_key.pem -x509 -days 365 -out server_cert.pem \
  -subj "/C=IN/ST=Telangana/L=Hyderabad/O=CBIT/OU=CSE/CN=localhost"'''




# ssl_client.py
import socket
import ssl

HOST = '127.0.0.1'
PORT = 8443

# NOTE: For demo only, we disable verification for a self-signed cert.
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        print("[*] TLS connection established. Cipher:", ssock.cipher())
        print("Type messages to send. Type 'exit' or 'quit' to close.\n")

        while True:
            msg = input("You: ").strip()
            if msg.lower() in ("exit", "quit"):
                print("[*] Closing client connection.")
                break

            if not msg:
                continue  # ignore empty lines

            ssock.sendall(msg.encode())

            # wait for server reply
            data = ssock.recv(4096)
            if not data:
                print("[!] Server closed the connection.")
                break

            print("Server:", data.decode(errors="ignore"))


