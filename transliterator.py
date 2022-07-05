from typing import List
from collections import namedtuple


lexem_classes = {" ": "space", "*": "arithmet_sign", "div": "arithmet_sign",
                 "mod": "arithmet_sign", "<": "compar_sign", ">": "compar_sign",
                 "<=": "compar_sign", ">=": "compar_sign", "<>": "compar_sign",
                 ";": "smcolon", "[": "sqrbrkt1", "]": "sqrbrkt2",
                 "(": "brkt1", ")": "brkt2", "+": "dig_sign", "-": "dig_sign"}

error_message = "ERROR"

TRANSLIATERATOR_LEXEM: namedtuple = namedtuple('Lexem', ['symbol', 'cls'])


def transliteration(data: str) -> List[namedtuple]:
    symbols = []
    i = 0
    while i < len(data):
        symbol = data[i]
        if data[i].isalpha():
            if data[i] == "d" and data[i + 1] == "i" and data[i + 2] == "v":
                i += 3
                symbol = "div"
                symbols.append(TRANSLIATERATOR_LEXEM(symbol, lexem_classes.get(symbol, error_message)))
                continue
            elif data[i] == "m" and data[i + 1] == "o" and data[i + 2] == "d":
                i += 3
                symbol = "mod"
                symbols.append(TRANSLIATERATOR_LEXEM(symbol, lexem_classes.get(symbol, error_message)))
                continue
            else:
                i += 1
                symbols.append(TRANSLIATERATOR_LEXEM(symbol, "letter"))
                continue
        elif symbol.isdigit():
            i += 1
            symbols.append(TRANSLIATERATOR_LEXEM(symbol, "digit"))
            continue
        elif symbol == "<":
            if data[i + 1] == "=" or data[i + 1] == ">":
                symbol = data[i:i + 2]
                symbols.append(TRANSLIATERATOR_LEXEM(symbol, lexem_classes.get(symbol, error_message)))
                i += 2
                continue
        elif symbol == ">":
            if data[i + 1] == "=":
                symbol = data[i:i + 2]
                symbols.append(TRANSLIATERATOR_LEXEM(symbol, lexem_classes.get(symbol, error_message)))
                i += 2
                continue
        symbols.append(TRANSLIATERATOR_LEXEM(symbol, lexem_classes.get(symbol, error_message)))
        i += 1
    return symbols


input = ["repeat f(1) until A[i+j]+B[i+j]>Max;",
         "repeat func(12) until Arr[Min+Max] div Arr[Top+Bot]<Zero;",
         "repeat func(-12) until Arr[Min+Max] div Arr[Top+Bot]<>Zero;",
         "repeat abs(-5) until myarray[I + j] * myarray[I - j] < MIN ;"]


