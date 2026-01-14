__author__ = 'U(196P8V' #this is my username ('F-162A7V') encrypted in vigenere. try making a code to find the key!



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
        stddisp = 49
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
    offset = 0
    for i in range(len(word)):
        if word[i] != ' ':

            stddisp, mod = find_stdispNmod(word,i)
            row = ord(word[i]) - stddisp
            col = ord(key[(i+offset) % len(key)]) - find_stdispNmod(key,i)[0]
            new_word += chr(stddisp + (row + col) % mod)
        else:
            offset -= 1;
            new_word += ' '
    return new_word


def decode(word, key):
    decoded_word = ""
    key = key.lower()
    offset = 0
    for i in range(len(word)):
        if word[i] != ' ':

            stddisp, mod = find_stdispNmod(word,i)
            row = ord(word[i]) - stddisp
            col = ord(key[(i+offset) % len(key)]) - find_stdispNmod(key,i)[0]
            decoded_word += chr(stddisp + ((row - col) % mod))
        else:
            offset -= 1;
            decoded_word += ' '
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
