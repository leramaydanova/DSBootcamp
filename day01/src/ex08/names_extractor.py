import sys

def names_extractor():
    if len(sys.argv) != 2:
        raise ValueError('Incorrect number of argument')

    with open('employees.tsv', 'w') as employees:
        employees.write("Name\tSurname\tE-mail\n")
        with open(sys.argv[1], 'r', encoding='utf-8') as emails:
            for line in emails:
                name = line.split(".")[0]
                surname = line.split("@")[0].split(".")[1]
                name = name.capitalize()
                surname = surname.capitalize()
                row = '\t'.join([name, surname, line])
                employees.write(row)


if __name__ == '__main__':
    try:
        names_extractor()
    except ValueError as e:
        print(e)