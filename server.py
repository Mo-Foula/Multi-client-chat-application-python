import socket
import threading
import caeser as encryption
import random

# connecting data
host = '127.0.0.1'
port = 12345
# starting server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(2)
# lists for clients and their names
clients = []


# names = [] y)


class Client:
    def __init__(self, name, connection, encKey):
        self.name = name
        self.connection = connection
        self.enc = encryption.Caeser(key=encKey)  # OBJECT MN CEASER


# sending messages to all connected clients
def broadcast(sender="", message=""):
    for client in clients:
        if client.connection != sender:
            #     client.send(message.encode())
            sendSingleMessage(client, message)


def prepareToSendKey(key=1):
    return pow(8 * key + 4, 2) + 22


def recieveSingleMessage(client):
    print(client.connection.recv(1024).decode())
    return client.enc.decrypt(msg=client.connection.recv(1024).decode())

# 1) recieve then decode then decrypt
# 2) 3aksaha, encrypt, encode, send
def sendSingleMessage(client, msg):
    client.connection.send(client.enc.encrypt(msg=msg).encode())


# Handling messages from clients
def handle(client):
    while True:
        try:
            # broadcasting messages
            message = recieveSingleMessage(client)
            broadcast(client.connection, '\n' + message)
        except:
            # removing and closing clients
            name = client.name
            clients.remove(client)
            client.connection.close()
            print(f'\n{name} left !')
            broadcast(message=f'\n{name} left !')
            break


# receving /listing
def receive():
    while True:
        # accepting connection
        client, address = server.accept()# lama yla2i new connection
        print(f"Connected with {str(address)}")
        # input('aaaaaaa')

        # request and store names
        # client.send('NICK'.encode())
        name = client.recv(1024).decode()

        # send encryption key
        encKey = random.randint(1, 25)
        # client.send('encryptionKeyIs'.encode())
        client.send(str(prepareToSendKey(key=encKey)).encode())
        # yo7ot el key fl mo3adla then y7wlo string then encode then send
        clientObj = Client(name=name, encKey=encKey, connection=client)
        clients.append(clientObj)
        # input('OKOKOKOOK')
        # names.append(name)
        # clients.append(client)
        # print broadcast nickname
        print(f"Name is {name}")
        broadcast(client, f"\n{name} joined!")
        # starting handling threads for client
        thread = threading.Thread(target=handle, args=(clientObj,))
        thread.start()

        # print('ALL CONNECTIONS')
        # for c in names:
        #     print('client', c)


receive()
