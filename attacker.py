import caeser as cr
import os

print('This program is for attacking encrypted messages by Caeser Cipher algorithm\n')
fileName = 'Decrypted messages.txt'
fileExists = False

if os.path.exists(fileName):
    #already exists w by3ml append
    fileExists = True
    file = open(fileName, "a")
    file.write("\n\n")
    file.close()
else:
    file = open(fileName, "x")
    #create
    file.close()

while True:
    inp = input('Enter the message you want to decrypt\n')
    start = 1
    end = 25
    # start = int(input('Enter the start of the key range you want to start attacking from (if you don\'t know enter 1)'))
    # end = int(input('Enter the end of the key range you want to end attacking at (if you don\'t know enter 25)'))
    file = open(fileName, "a")
    file.write(inp + '\n\n')
    for i in range(start, end + 1):
        c = cr.Caeser(key=i)
        msg = c.decrypt(msg=inp)
        file.write(msg + f'  at key = {i}\n')
    file.write('\n\n')
    file.close()
    print('Decryption completed')

