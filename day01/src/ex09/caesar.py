import sys

def encode():
    if len(sys.argv) != 4:
        raise ValueError('Incorrect number of argument')
    
    s = sys.argv[2]

    if (s.isascii() == False):
        raise ValueError('The script does not support your language yet.')
        
    caesar_str = []

    for letter in s:
        new_letter = chr((ord(letter) - ord('a') + int(sys.argv[3])) % 26 + ord('a')) if (letter >= 'a' and letter <= 'z') else letter
        caesar_str.append(new_letter)

    print(''.join(caesar_str))

def decode():
    if len(sys.argv) != 4:
        raise ValueError('Incorrect number of argument')
    
    s = sys.argv[2]

    if (s.isascii() == False):
        raise ValueError('The script does not support your language yet.')

    caesar_str = []
    for letter in s:
        new_letter = chr((ord(letter) - ord('a') - int(sys.argv[3])) % 26 + ord('a')) if (letter >= 'a' and letter <= 'z') else letter
        caesar_str.append(new_letter)

    print(''.join(caesar_str))


if __name__ == '__main__':
    if sys.argv[1] == 'encode':
        try:
            encode()
        except ValueError as e:
            print(e)
    elif sys.argv[1] == 'decode':
        try:
            decode()
        except ValueError as e:
            print(e)
    