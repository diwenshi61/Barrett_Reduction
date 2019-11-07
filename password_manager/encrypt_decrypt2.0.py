GLOBAL_LENGTH = 4200
LOOPS = 1 # number of hashes between writes

import hashlib
import getpass
import destroy
import sys

def encrypt():
    print ("")
    print ("passwords.txt example")
    print ("['email','computer']")
    print ("MyEmailPassword")
    print ("MyComputerPassword")
    print ("Keep passwords/descriptors 94 characters or less")
    print ("Only accepts ASCII characters 32-126")
    print ("")
    password = ""
    y = " "
    while password != y:
        print ("Create a master password.")
        password = hashlib.sha256(getpass.getpass()).hexdigest()
        print ("Reenter to confirm")
        y = hashlib.sha256(getpass.getpass()).hexdigest()
        if password != y:
            print ("Try again")
            print ("")
    try:
        file = open("passwords.txt","r")
    except IOError:
        print ("Error: no passwords.txt file found")
        quit()
    f = open("encrypted.txt","w")
    line_count = 0
    a = []
    enc_msg = ""
    for line in file:
        if line_count == 0:
            a = eval(line) # dangerous if using externally sourced files
            line_count = 1
        else:
            enc_msg = ""
            if len(a[line_count - 1]) > 94:
                print ("Descriptor over 94 characters")
                quit()
            if len(line) > 94:
                print ("Password over 94 characters")
                quit()
            temp = 0
            if "\n" in line:
                temp = 1
            enc_msg += chr(len(a[line_count - 1]) + 32)
            enc_msg += chr(len(line) + 32 - temp)
            for char in a[line_count - 1]:
                if (ord(char) > 126 or ord(char) < 32) and char != "\n":
                    print ("Invalid character")
                    quit()
            for char in line:
                if (ord(char) > 126 or ord(char) < 32) and char != "\n":
                    print ("Invalid character")
                    quit()
            enc_msg += a[line_count - 1]
            enc_msg += line
            line_count += 1
            pos = []
            temp = 0
            hashbase = password + chr(line_count - 1 + 32)
            for char in enc_msg:
                if char != "\n":
                    while True:
                        for i in range(LOOPS):
                            temp = hashlib.sha256(hashbase).hexdigest()
                            hashbase = temp
                        if int(temp, 16) % GLOBAL_LENGTH not in pos:
                            pos += [int(temp, 16) % GLOBAL_LENGTH]
                            break
            for i in range(GLOBAL_LENGTH):
                if i in pos:
                    f.write(enc_msg[pos.index(i)])
                else:
                    for i in range(LOOPS):
                        temp = hashlib.sha256(hashbase).hexdigest()
                        hashbase = temp
                    f.write(chr(int(temp, 16) % 95 + 32))
            f.write("\n")
    f.close()
    file.close()
    destroy.destroy("passwords.txt")
    print ("finished encryption")


def decrypt():
    f = open("encrypted.txt","r")
    password = hashlib.sha256(getpass.getpass()).hexdigest()
    line_count = 0
    words = []
    pwds = []
    for line in f:
        line_count += 1
        pos = []
        pos1 = []
        temp = 0
        hashbase = password + chr(line_count + 32)
        for i in range(2):
            while True:
                for i in range(LOOPS):
                    temp = hashlib.sha256(hashbase).hexdigest()
                    hashbase = temp
                if int(temp, 16) % GLOBAL_LENGTH not in pos:
                    pos += [int(temp, 16) % GLOBAL_LENGTH]
                    pos1 += [line[int(temp, 16) % GLOBAL_LENGTH]]
                    break
        word = ""
        for i in range(ord(pos1[0]) - 32):
            while True:
                for i in range(LOOPS):
                    temp = hashlib.sha256(hashbase).hexdigest()
                    hashbase = temp
                if int(temp, 16) % GLOBAL_LENGTH not in pos:
                    pos += [int(temp, 16) % GLOBAL_LENGTH]
                    word += line[int(temp, 16) % GLOBAL_LENGTH]
                    break
        words += [word]
        pwd = ""
        for i in range(ord(pos1[1]) - 32):
            while True:
                for i in range(LOOPS):
                    temp = hashlib.sha256(hashbase).hexdigest()
                    hashbase = temp
                if int(temp, 16) % GLOBAL_LENGTH not in pos:
                    pos += [int(temp, 16) % GLOBAL_LENGTH]
                    pwd += line[int(temp, 16) % GLOBAL_LENGTH]
                    break
        pwds += [pwd]
    f.close()
    file = open("passwords.txt","w")
    file.write(str(words))
    for pwd in pwds:
        file.write("\n" + pwd)
    file.close()

if __name__ == "__main__":
    while True:
        choice = raw_input("Type 1 for encryption, 2 for decryption, 3 to remove passwords.txt, quit to quit\n")
        if choice == "1":
            encrypt()
        elif choice == "2":
            decrypt()
        elif choice == "3":
            destroy.destroy("passwords.txt")
        elif choice.lower() == "quit":
            quit()
