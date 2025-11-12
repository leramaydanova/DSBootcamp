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
        
        def counts_any(self, data):
            heads = 0
            tails = 0

            for h, t in data:
                heads += h
                tails += t
            
            return heads, tails
        
        def save_file(self, data, file_name, ext):
            with open(f"{file_name}.{ext}", 'w') as file:
                count_of_observations = len(data[0])
                heads, tails = data[1]
                frac_heads, frac_tails = data[2]
                number_of_obs = len(data[3])
                predict_heads, predict_tails = self.counts_any(data[3])
                
                file.write(f"We made {count_of_observations} observations by tossing a coin: {tails} were tails and {heads} were heads. " \
                f"The probabilities are {round(frac_tails, 2)}% and {round(frac_heads, 2)}%, respectively. " \
                f"Our forecast is that the next {number_of_obs} observations will be: {predict_tails} tail and {predict_heads} heads.")


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

        

