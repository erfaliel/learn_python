import socket as s

host = ''
port = 12800

main_connexion = s.socket(s.AF_INET, s.SOCK_STREAM) # build connexion object
main_connexion.bind((host, port))                    # update parameter for listening port
main_connexion.listen(5)                            # If noone connection is accepted, max conn is 5
print(f"Server is listening on port {port}.")

(conn_client, conn_info) = main_connexion.accept()  # Method that block the programm untill to recept a connection

msg_recept = b""
while msg_recept != b"end":
    msg_recept = conn_client.recv(1024)             #catch msg from socket with 1024 bits max
    print(msg_recept.decode())
    conn_client.send(b"5/5")

print("Connection has been closed!")
conn_client.close()                                 #to close the scocket
main_connexion.close()                              #to close main connection object     
