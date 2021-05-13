import socket as s

host = "localhost"
port = 12800

client_conn = s.socket(s.AF_INET, s.SOCK_STREAM)        # build connection object.
client_conn.connect((host, port))                       # open a socket
print(f"Connextion established with server on port: {port} ")

msg_send = b""
while msg_send != b"end":
    msg_send = input("> ")
    msg_send = msg_send.encode()                        # sting method str -> bytes
    client_conn.send(msg_send)                          # send an encoded message
    msg_recept = client_conn.recv(1024)                 # buffered a recept connetion to 1024 bits
    print(msg_recept.decode())                          # string method bytes -> str

print("Connection has benn ended!")
client_conn.close()