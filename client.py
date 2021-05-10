import socket
import threading
import caeser as encryption

# client side choosing their names
name = input("Enter ur Name PLease: ")
# connecting to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))



enc = 0


def sendSingleMessage(message):
    client.send((enc.encrypt(message)).encode())

def recieveKey(key=1):
    return int((pow(int(key) - 22, 1/2) - 4) / 8)

def recieveSingleMessage():
    return enc.decrypt(msg=client.recv(1024).decode())


def listen():
    client.send(name.encode())
    global enc
    k = recieveKey(client.recv(1024).decode())
    # print(k)
    enc = encryption.Caeser(key=k)
    write_thread = threading.Thread(target=write)
    write_thread.start()
    #actual listening
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            # message = client.recv(1024).decode()
            # if message == 'NICK':
            #
            # else:
                message = recieveSingleMessage()
                print('\n' + message)
        except:
            # Close Connection When Error
            print("\nAn error occured!")
            client.close()
            break


# Sending Messages To Server
def write():
    print('Connected to chat.')
    while True:
        inp = input('You: ')
        message = f'{name}: {inp}'
        # message = '{}: {}'.format(name, input(''))
        sendSingleMessage(message)


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=listen)
receive_thread.start()


