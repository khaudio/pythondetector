import os
import sys
import getpass

"""Adds passed arg as alias"""

def find_dir(var, item, levels=0):
    if item.name.lower() == var:
        return item.path
    elif item.is_dir() and levels <= 3:
        for subItem in os.scandir(item.path):
            # Search recursively 3 levels deep
            found = find_dir(var, subItem, levels + 1)
            if found:
                return found


def set_filename():
    for filename in (os.path.expanduser('~/.bashrc'), os.path.expanduser('~/.bash_profile')):
        if os.path.exists(filename):
            return filename
    else:
        return os.path.expanduser('~/.bash_profile')


def add_alias(arg):
    alias, delimiter, command = arg.partition('=')
    string = f"{alias}{delimiter}'{command}'"
    filename = set_filename()
    with open(filename, 'r') as reader:
        for line in filename:
            if string in line or alias in line.partition('=')[0]:
                return
            last = line
    print(f'last is {last}')
    with open(filename, 'a' if os.path.exists(filename) else 'w') as writer:
        writer.write('\n' if last else '' + f'alias {alias}\n')


def main():
    aliases = sys.argv[1:]
    for string in aliases:
        add_alias(string)


if __name__ == '__main__':
    main()
