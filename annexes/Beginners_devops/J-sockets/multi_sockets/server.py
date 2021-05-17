import socket as s
import select

host = ""
port = 12800

main_conn = s.socket(s.AF_INET, s.SOCK_STREAM)
main_conn.bind((host, port))
main_conn.listen(5)
print(f"Server is now listening on port: {port}!")

server_is_running = True
connected_clients = []
# list of sockets from clients
while server_is_running:
    (asked_connections, wlist, xlist) = select.select([main_conn], [], [], 0.05)
    # asked_connections is a list of sockect objects that has been catched by select

    for conn in asked_connections:
        (conn_client, conn_info) = conn.accept()    # method to catch a message (non really block here, because somethins has been catched by select)
        print(f"DEBUG: conn_client type is: {type(conn_client)}")
        connected_clients.append(conn_client)       # add socket to the list

    clients_buffer = []
    try:
        # same treatment with select but with a buffer, in this way asked_connections strean is not interrupted
        (clients_buffer, wlist, xlist) = select.select(connected_clients, [], [], 0.05)
    except select.error:
        print("Exception : an error occurred!")
    else:
        if clients_buffer != []:
            print(f"DEBUG: client into the buffer : {clients_buffer}")
        for client in clients_buffer:
            # client's type is a socket
            msg_recv = client.recv(1024)  # record the message for one client into 1024 bits 
            msg_recv = msg_recv.decode()  # convert bytes into str
            print(f"Recept {msg_recv}")   # print message
            client.send(b"5/5")           # make a response
            if msg_recv == "end":
                server_is_running = False # asks to close connection

print("Connexion is closing…")
for client in connected_clients:          # loop into connection list to close all socket
    client.close

main_conn.close()                         # close socket object
print("connections has been closed")
