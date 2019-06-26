import os
import sys
import getpass

"""Adds passed arg directory to PATH"""

def find_dir(var, item, levels=0):
    if item.name.lower() == var:
        return item.path
    elif item.is_dir() and levels <= 3:
        for subItem in os.scandir(item.path):
            # Search recursively 3 levels deep
            found = find_dir(var, subItem, levels + 1)
            if found:
                return found


def repository(var):
    var, directory = var.lower(), os.getcwd().lower()
    if directory.split(os.path.sep)[-1] == var:
        return directory
    else:
        # Search directory for matching repository name
        for item in os.scandir(directory):
            found = find_dir(var, item)
            if found:
                return found


def set_filename():
    for filename in (os.path.expanduser('~/.bashrc'), os.path.expanduser('~/.bash_profile')):
        if os.path.exists(filename):
            return filename
    else:
        return os.path.expanduser('~/.bash_profile')


def update_path(var, directory):
    capitalized, filename = var.upper(), set_filename()
    try:
        exists = os.environ[capitalized]
    except KeyError:
        exists = False
    with open(filename, 'a' if os.path.exists(filename) else 'w') as writer:
        if not exists:
            writer.write('\nexport {}={}\n'.format(capitalized, directory))
        if directory not in os.environ['PATH']:
            writer.write('export PATH=\$PATH:\${}\n'.format(capitalized))


def save_pypi_info(savePassword=False):
    username = input('Enter PyPI username: ')
    if savePassword:
        password = getpass.getpass('Enter password for {}: '.format(username))
    else:
        password = None
    try:
        filepath = os.path.expanduser('~/.pypirc')
        if not os.path.exists(filepath):
            with open(filepath, 'w') as info:
                info.write('\n'.join((
                        '[distutils]',
                        'index-servers=pypi',
                        '[pypi]',
                        'repository = https://pypi.python.org/pypi'
                        'username = {}'.format(username),
                        '' if not savePassword else 'password = {}'.format(password)
                    )))
    finally:
        del username, password


def add_alias(alias):
    filename = set_filename()
    with open(filename, 'r') as reader:
        for line in filename:
            if alias in line:
                return
    with open(filename, 'a' if os.path.exists(filename) else 'w') as writer:
        writer.write(f'alias \n{alias}\n')


def main():
    var = sys.argv[1]
    directory = repository(var)
    if directory:
        update_path(var, directory)
    else:
        raise FileNotFoundError('{} repository could not be located'.format(var))


if __name__ == '__main__':
    main()
