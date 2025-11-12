import os

def f():
    virtual_env = os.environ.get('VIRTUAL_ENV')
    print(f"Your current virtual env is {virtual_env}")

if __name__ == '__main__':
    f()