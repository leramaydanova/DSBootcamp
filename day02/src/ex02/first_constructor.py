import sys, os

class Research:
    def __init__(self, path):
        if not os.path.exists(path):
            raise ValueError("File does not exist")
        self.path = path

    def file_reader(self):   
        data = ''
        with open(self.path, 'r') as file:
            line1 = file.readline()
            header = line1.strip().split(',')

            if len(header) != 2 or not header[0].isalpha() or not header[1].isalpha():
                raise ValueError("Not valid file")
            
            data = ''.join(line1)
            
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line != '0,1' and cleaned_line != '1,0':
                    raise ValueError("Not valid file")
                data = ''.join([data, line])
        return data

if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            example = Research(sys.argv[1]).file_reader()
            print(example)
        except ValueError as e:
            print(e)
        

