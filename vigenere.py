__author__ = 'yoav'



def encode(word,key):
    new_word = ""
    word = word.lower()
    key = key.lower()
    for i in range(len(word)):
        row = ord(word[i]) - 97
        col = ord(key[i%len(key)]) - 97
        new_word += chr(97 + (row+col) % 26)
    return new_word

def decode(word,key):
    decoded_word = ""
    word = word.lower()
    key = key.lower()
    for i in range(len(word)):
        row = ord(word[i]) - 97
        col = ord(key[i%len(key)]) - 97
        decoded_word += chr(97 + (row-col) % 26)
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
            while not keyword.isalpha():
                keyword = input("Invalid key, only enter letters: ")
            if inpt == "1":
                print(encode(text,keyword))
            elif inpt == "2":
                print(decode(text,keyword))
            else:
                print("Invalid input")


main()