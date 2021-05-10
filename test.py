# f(x) = (8x + 4)power 2 + 22

# x = (root((f(x) - 22) , 2) - 4 )/8
import math


def prepareToSendKey(key=1):
    return pow(8 * key + 4, 2) + 22


def recieveKey(key=1):
    return int((pow(key - 22, 1/2) - 4) / 8)

num = 23

print(prepareToSendKey(23))
print(recieveKey(prepareToSendKey(23)))
input()