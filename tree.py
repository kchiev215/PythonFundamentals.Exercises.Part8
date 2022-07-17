import os

def walk(dirname):
    """Prints the names of all files in dirname and its subdirectories.
    This is the version in the book.
    dirname: string name of directory
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        return path

def writing_to_file(message):
    with open('directory.txt', 'w') as f:
        f.write(message)


if __name__ == '__main__':
    writing_to_file(walk('.'))