import timeit

def cycle(emails):
    gmails = []
    for email in emails:
        if '@gmail' in email:
            gmails.append(email)
    return gmails

def list_comprehension(emails):
    gmails = [email for email in emails if '@gmail' in email]
    return gmails

if __name__ == '__main__':
    number = 90000
    data = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
    'anna@live.com', 'philipp@gmail.com'] * 5
    cycle_time = timeit.timeit(lambda: cycle(data), number=number)
    list_comp_time = timeit.timeit(lambda: list_comprehension(data), number=number)
    res_str = ""
    values = sorted([cycle_time, list_comp_time])
    if list_comp_time <= cycle_time:
        res_str = "It is better to use a list comprehension"
    else:
        res_str = "It is better to use a loop"
    print(res_str)
    print(f"{values[0]} vs {values[1]}")
    # print(f"{cycle(data)}\n{list_comprehension(data)}")
