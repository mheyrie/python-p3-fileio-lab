def write_file(file_name , file_content):
    with open(f"{file_name}.txt, {file_content}, 'w'") as text_file:
        return text_file.write

def append_file(file_name, append_content):
    with open(f"{file_name}.txt, {append_content}, 'a'") as f:
        return f.a
        pass

    pass

def read_file(file_name):
    with open (f"{file_name}.txt", "r") as f:
        return f.read


# print(write_file(file_name="logfile", file_content="Log 1: 5 bananas added" ))