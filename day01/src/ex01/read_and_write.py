def readf():
    data_rows = []
    with open('ds.csv', 'r', encoding='utf-8') as file:
        for line in file:
            cleaned_line = line.strip()
            columns = cleaned_line.split(',')
            right_columns = [*columns[0:2], ",".join(columns[2:-3]), *columns[-3:-1], columns[-1]]
            data_rows.append(right_columns)

    return data_rows


def writef():
    data = readf()
    with open('ds.tsv', 'w') as file:
        for line in data:
            file.write("\t".join(line) + '\n')


if __name__ == '__main__':
    writef()