import sys
from random import randint

class Research:

    class Calculations:

        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = 0
            tails = 0

            for h, t in self.data:
                heads += h
                tails += t

            return heads, tails
        
        def fractions(self, heads, tails):
            all = heads + tails
            return heads / all * 100, tails / all * 100

    class Analytics(Calculations):

        def predict_random(self, number):
            predict = []
            for n in range(number):
                heads = randint(0, 1)
                tails = 1 if heads == 0 else 0
                predict.append([heads, tails])

            return predict

        def predict_last(self):
            return self.data[len(self.data) - 1]


    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header = True):   
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
            calc = Research.Calculations(list).counts()
            frac = Research.Calculations(list).fractions(calc[0], calc[1])
            rand = Research.Analytics(list).predict_random(3)
            last = Research.Analytics(list).predict_last()
            print(list)
            print(*calc)
            print(*frac)
            print(rand)
            print(last)
        except ValueError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        

