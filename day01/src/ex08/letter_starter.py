import sys

def letter_starter():
    if len(sys.argv) != 2:
        raise ValueError('Incorrect number of argument')
    
    with open('employees.tsv', 'r') as employees:
        next(employees)
        for line in employees:
            
            split_row = line.strip().split('\t')

            if (split_row[2] == sys.argv[1]):
                print(f"Dear {split_row[0]}, welcome to our team! " \
                "We are sure that it will be a pleasure to work with you. " \
                "That’s a precondition for the professionals that our company hires.")

                break
            


if __name__ == '__main__':
    try:
        letter_starter()
    except ValueError as e:
        print(e)