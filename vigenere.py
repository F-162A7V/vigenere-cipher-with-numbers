__author__ = 'yoav'



def find_stdispNmod(word,i):
    idx = i%len(word)
    l1 = list('!"#$%&()\'*+,-./')
    l2 = list(':;<=>?@')
    l3 = list('[\\]^_`')
    if word[idx].isupper():
        stddisp = 65
        mod = 26
    elif word[idx].islower():
        stddisp = 97
        mod = 26
    elif word[idx].isdigit():
        stddisp = 48
        mod = 10
    elif word[idx] in l1:
        stddisp = 33
        mod = 16
    elif word[idx] in l2:
        stddisp = 58
        mod = 7
    elif word[idx] in l3:
        stddisp = 32
        mod = 6
    return stddisp, mod

def encode(word, key):
    new_word = ""
    key = key.lower()
    for i in range(len(word)):
        stddisp, mod = find_stdispNmod(word,i)
        row = ord(word[i]) - stddisp
        col = ord(key[i % len(key)]) - find_stdispNmod(key,i)[0]
        new_word += chr(stddisp + (row + col) % mod)
    return new_word


def decode(word, key):
    decoded_word = ""
    key = key.lower()
    for i in range(len(word)):
        stddisp, mod = find_stdispNmod(word,i)
        row = ord(word[i]) - stddisp
        col = ord(key[i % len(key)]) - find_stdispNmod(key,i)[0]
        decoded_word += chr(stddisp + ((row - col) % mod))
    return decoded_word


def main():
    while True:
        print("----------------------")
        print("1: Encode plain text\n")
        print("2: Decode encrypted text\n")
        inpt = input("Enter choice: ")
        if (inpt.isdigit()):
            text = input("Enter text: ")
            keyword = input("Enter keyword: ")
            if inpt == "1":
                print("Encoded text: " + encode(text, keyword))
            elif inpt == "2":
                print("Decoded text: " + decode(text, keyword))
            else:
                print("Invalid input")
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
