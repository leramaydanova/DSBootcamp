def sorter():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
        ]
    
    list_of_tuples.sort(key=lambda x: (-keyNum(x), keyCountry(x)))
    for country, num in list_of_tuples:
        print(country)

def keyNum(e):
    return int(e[1])

def keyCountry(e):
    return e[0]

if __name__ == '__main__':
    sorter()