
def data_input(cls, filename="input.txt") -> str:
    with open(filename, 'r') as file:
        s = file.read()
        return s


def data_output(cls,  chain_detected: bool, filename="output.txt") -> None:
    with open(filename, "w") as file:
        if chain_detected:
            file.write('ACCEPT')
        else:
            file.write('REJECT')

