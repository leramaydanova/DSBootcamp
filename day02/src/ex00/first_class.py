class Must_Read:
    with open('data.csv', 'r') as file:
        for line in file:
            print(line, end='')

if __name__ == '__main__':
    example = Must_Read()