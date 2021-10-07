def open_read_file(filepath):
    with open(filepath, 'r') as file:
        read_file = "".join(file.readlines())
    return read_file