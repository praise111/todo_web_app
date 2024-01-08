FILEPATH = 'todo.txt'
def to_read(filepath=FILEPATH):
    with open(filepath, 'r') as file_locale:
        todos_locale = file_locale.readlines()
    return todos_locale


def to_write(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_locale:
        file_locale.writelines(todos_arg)


