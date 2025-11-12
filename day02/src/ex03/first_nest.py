import sys, os

class Research:

    class Calculations:

        def counts(self, data):
            heads = 0
            tails = 0

            for h, t in data:
                heads += h
                tails += t

            return heads, tails
        
        def fractions(self, heads, tails):
            all = heads + tails
            return heads / all * 100, tails / all * 100




    def __init__(self, path):
        if not os.path.exists(path):
            raise ValueError("File does not exist")
        self.path = path

    def file_reader(self, has_header = False):   
        data = []
        with open(self.path, 'r') as file:
            if has_header:
                line1 = file.readline()
                header = line1.strip().split(',')

                if len(header) != 2 or not header[0].isalpha() or not header[1].isalpha():
                    raise ValueError("Not valid file")

            
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line != '0,1' and cleaned_line != '1,0':
                    raise ValueError("Not valid file")
                
                list = cleaned_line.split(',')
                a, b = map(int, list)
                data.append([a, b])

        return data

if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            list = Research(sys.argv[1]).file_reader()
            calc = Research.Calculations().counts(list)
            frac = Research.Calculations().fractions(calc[0], calc[1])
            print(list)
            print(*calc)
            print(*frac)
        except ValueError as e:
            print(e)
        

