import timeit, sys
from functools import reduce

def loop(r):
    sum = 0
    for i in range(r + 1):
        sum += i*i
    return sum

def _reduce(r):
    sum = int(reduce(lambda x, y: x + y*y, range(r + 1)))
    return sum

if __name__ == '__main__':
    try:
        func = sys.argv[1]
        number = int(sys.argv[2])
        r = int(sys.argv[3])
        res = 0

        match func:
            case 'loop':
                res = timeit.timeit(lambda: loop(r), number=number)
            case 'reduce':
                res = timeit.timeit(lambda: _reduce(r), number=number)
            case _:
                raise Exception('Not valid function name')
        
        print(res)
        print(f"{loop(r)}\n{_reduce(r)}")
    except Exception as e:
        print(e)
    
