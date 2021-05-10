class Caeser:
    def __init__(self, key):
        self.key = key

    def encrypt(self, msg):
        new_msg = ''
        for char in msg:
            if char == ' ':
                new_msg += ' '
            elif char.isupper():
                new_msg += self._encryptUpper(char)
            elif char.islower():
                new_msg += self._encryptLower(char)
            else:
                new_msg += char
        return new_msg

    def _encryptLower(self, char):
        # a - a = 0
        # z - a = 25
        return chr(((ord(char) - 97 + self.key) % 26) + 97)

    def _decryptLower(self, char):
        return chr(((ord(char) - 97 - self.key) % 26) + 97)

    def _encryptUpper(self, char):
        # ord('A') = 65
        return chr(((ord(char) - 65 + self.key) % 26) + 65)

    def _decryptUpper(self, char):
        return chr(((ord(char) - 65 - self.key) % 26) + 65)

    def encryptManyMsgs(self, msgs):
        newmsgs = []
        for msg in msgs:
            newmsgs.append(self.encrypt(msg))
        return newmsgs

    def decryptManyMsgs(self, msgs):
        newmsgs = []
        for msg in msgs:
            newmsgs.append(self.decrypt(msg))
        return newmsgs

    def decrypt(self, msg):
        new_msg = ''
        for char in msg:
            if char == ' ':
                new_msg += ' '
            elif char.isupper():
                new_msg += self._decryptUpper(char)
            elif char.islower():
                new_msg += self._decryptLower(char)
            else:
                new_msg += char
        return new_msg


'''
C = Caeser(key=25)
D = Caeser(key=26)
E = Caeser(key=27)
R = Caeser(key=1)

msg = 'Hello Sasuke'

print(C.encrypt(msg))
print(D.encrypt(msg))
print(E.encrypt(msg))
print(R.encrypt(msg))
input()
'''
