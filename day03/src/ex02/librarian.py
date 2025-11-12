import subprocess, os

def librarian():
    if os.environ.get('VIRTUAL_ENV_PROMPT') != 'youngtar':
            raise EnvironmentError('Wrong environment')
    subprocess.call("pip3 install -r _requirements.txt".split(' '))
    subprocess.call("pip3 freeze > requirements.txt", shell=True)
    subprocess.call("pip3 freeze".split(' '))


if __name__ == '__main__':
    try:
        librarian()
    except EnvironmentError as e:
        print(e)