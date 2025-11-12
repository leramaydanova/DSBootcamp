import timeit, sys

def cycle(emails):
    gmails = []
    for email in emails:
        if '@gmail' in email:
            gmails.append(email)
    return gmails

def list_comprehension(emails):
    gmails = [email for email in emails if '@gmail' in email]
    return gmails

def list_map(emails):     
    gmails = list(map(lambda x: x if '@gmail' in x else None, emails))
    return gmails

def list_filter(emails):
    gmails = list(filter(lambda x: '@gmail' in x, emails))
    return gmails

if __name__ == '__main__':
    try:
        func = sys.argv[1]
        number = int(sys.argv[2])
        res = 0

        data = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
        'anna@live.com', 'philipp@gmail.com'] * 5

        match func:
            case 'loop':
                res = timeit.timeit(lambda: cycle(data), number=number)
            case 'list_comprehension':
                res = timeit.timeit(lambda: list_comprehension(data), number=number)
            case 'map':
                res = timeit.timeit(lambda: list_map(data), number=number)
            case 'filter':
                res = timeit.timeit(lambda: list_filter(data), number=number)
            case _:
                raise Exception('Not valid function name')
        
        print(res)
        # print(f"{cycle(data)}\n{list_comprehension(data)}\n{list_map(data)}\n{list_filter(data)}")
    except Exception as e:
        print(e)
