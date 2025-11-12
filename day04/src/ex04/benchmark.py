import timeit, random
from collections import Counter

def counts(list):
    return Counter(list)

def top(list):
    c = counts(list)
    return c.most_common(10)

def no_counter_counts(list: list):
    res = dict()
    for i in set(list):
        res[i] = list.count(i)
    return res

def no_counter_top(l: list):
    items = list(no_counter_counts(l).items())
    items.sort(key=lambda i: i[1], reverse=True)
    return items[0:10]

if __name__ == '__main__':
    random_list = [random.randint(0, 100) for _ in range(1000000)]

    my_func = timeit.timeit(lambda: no_counter_counts(random_list), number=1)
    counter = timeit.timeit(lambda: counts(random_list), number=1)
    my_top = timeit.timeit(lambda: no_counter_top(random_list), number=1)
    counter_top = timeit.timeit(lambda: top(random_list), number=1)

    print(f"my function: {my_func}\nCounter: {counter}\nmy top: {my_top}\nCounter's top: {counter_top}")
