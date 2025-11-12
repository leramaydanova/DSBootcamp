def data_types():
    a = 2
    b = "hello"
    c = 2.2
    d = True
    e = ["i", "love", 7, True]
    f = {"apple": 7,
            "banana": 3,
            "oranges": 10}
    g = ("i", "love", 7, True) 
    h = {1, 2, 3, 4, 5}

    vars = [a, b, c, d, e, f, g, h]

    res = [type(var).__name__ for var in vars]

    print('[' + ", ".join(res) + ']')

if __name__ == '__main__':
    data_types()