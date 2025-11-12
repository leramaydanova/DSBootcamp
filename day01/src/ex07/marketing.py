import sys

def call_center():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    res = clients

    for mail in recipients:
        res.remove(mail)

    print(res)

def potential_clients():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
        'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
        'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    
    set_clients = set(clients)
    set_participants = set(participants)

    diff = set_participants - set_clients

    res = [mail for mail in participants if mail in diff]

    print(res)

def loyalty_program():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
        'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
        'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    
    res = clients

    set_clients = set(clients)
    set_participants = set(participants)

    diff = set_clients - set_participants

    res = [mail for mail in clients if mail in diff]

    print(res)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'call_center':
            call_center()
        elif sys.argv[1] == 'potential_clients':
            potential_clients()
        elif sys.argv[1] == 'loyalty_program':
            loyalty_program()
        else:
            raise ValueError('Unknown command')