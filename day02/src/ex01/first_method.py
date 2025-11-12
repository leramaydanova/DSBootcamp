class Research:
    def file_reader(self):   
        data = ''
        with open('data.csv', 'r') as file:
            for line in file:
                data = ''.join([data, line])
        return data

if __name__ == '__main__':
    example = Research().file_reader()
    print(example)