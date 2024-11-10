import socket as s
import select

host = ""
port = 12800

def launch_server(host, port):
    main_conn = s.socket(s.AF_INET, s.SOCK_STREAM)
    main_conn.bind((host, port))
    main_conn.listen(5)
    print(f"Server is now listening on port: {port}")
    return main_conn

def main_loop(main_conn):
    server_is_running = True
    connected_clients = []
    # list of sockets from clients
    while server_is_running:
        (asked_connections, wlist, xlist) = select.select([main_conn], [], [], 0.05)
        connected_clients = handler(main_conn, connected_clients, asked_connections)
        server_is_running = read_messages(connected_clients)
        

def handler(main_conn, connected_clients, asked_connections):
    print(f"DEBUG: main_conn: {main_conn}")
    print(f"DEBUG : connected_clients : {connected_clients}")
    # (asked_connections, wlist, xlist) = select.select([main_conn], [], [], 0.05)
    # asked_connections is a list of sockect objects that has been catched by select
    for conn in asked_connections:
        (conn_client, conn_info) = conn.accept()     # method to catch a message (non really block here, because somethins has been catched by select)
        print(f"DEBUG: conn_client type is : {type(conn_client)}")
        connected_clients.append(conn_client)
        return connected_clients

def read_messages(connected_clients):
    clients_buffer = []
    print(f"DEBUG: connected_clientes : {connected_clients}")
    (asked_connections, wlist, xlist) = select.select([main_conn], [], [], 0.05) 
    try:
        # same treatment than handler with select but with a buffer, in this way asked_connections strean is not interrupted
        (clients_buffer, wlist, xlist) = select.select(connected_clients, [], [], 0.05)
    except select.error:
        print("Exception: an error occured with the buffer!")
    else:
        if clients_buffer != []:
            print(f"DEBUG: message from client into the buffer : {clients_buffer}")
        for client in clients_buffer:
            # client's type is a socket
            msg_recv = read_one_message(client)
            # check if One client wants to leave
            if msg_recv == "end":
                return False
            else:
                return True


def read_one_message(client):
    msg_recv = client.recv(1024)  # record the message for one client into 1024 bits
    msg_recv = msg_recv.decode()  # convert bytes into str
    print(f"Recept {msg_recv}")   # print message
    client.send(b"message acked") # make a response for acknowledgement
    return msg_recv

if __name__ == '__main__':
    main_conn = launch_server(host, port)
    main_loop(main_conn)