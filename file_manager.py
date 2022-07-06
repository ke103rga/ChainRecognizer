def data_input(filename: str = "input.txt"):
    with open(filename, "r") as file:
        s = file.read()
    return s


def data_output(result: bool, filename: str = "output.txt"):
    with open(filename, "w") as file:
        if result:
            print("ACCEPT", file=file)
        else:
            print("REJECT", file=file)
