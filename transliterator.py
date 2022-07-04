from typing import List
from collections import namedtuple


lexem_classes = {" ": "space", "*": "arithmet_sign", "div": "arithmet_sign",
                 "mod": "arithmet_sign", "<": "compar_sign", ">": "compar_sign",
                 "<=": "compar_sign", ">=": "compar_sign", "<>": "compar_sign",
                 ";": "smcolon", "[": "sqrbrkt1", "]": "sqrbrkt2",
                 "(": "brkt1", ")": "brkt2", "+": "dig_sign", "-": "dig_sign"}
error_message = "ERROR"


class Transliterator:

    TRANSLIATERATOR_LEXEM: namedtuple = namedtuple('Lexem', ['symbol', 'cls'])

    @classmethod
    def transliteration(cls, data: str) -> List[namedtuple]:
        symbols = []
        i = 0
        while i < len(data):
            symbol = data[i]
            if data[i].isalpha():
                if data[i] == "d" and data[i + 1] == "i" and data[i + 2] == "v":
                    i += 3
                    symbol = "div"
                    symbols.append(cls.TRANSLIATERATOR_LEXEM(symbol, lexem_classes.get(symbol, error_message)))
                    continue
                elif data[i] == "m" and data[i + 1] == "o" and data[i + 2] == "d":
                    i += 3
                    symbol = "mod"
                    symbols.append(cls.TRANSLIATERATOR_LEXEM(symbol, lexem_classes.get(symbol, error_message)))
                    continue
                else:
                    i += 1
                    symbols.append(cls.TRANSLIATERATOR_LEXEM(symbol, "letter"))
                    continue
            elif symbol.isdigit():
                i += 1
                symbols.append(cls.TRANSLIATERATOR_LEXEM(symbol, "digit"))
                continue
            elif symbol == "<":
                if data[i+1] == "=" or data[i+1] == ">":
                    symbol = data[i:i+2]
                    symbols.append(cls.TRANSLIATERATOR_LEXEM(symbol, lexem_classes.get(symbol, error_message)))
                    i += 2
                    continue
            elif symbol == ">":
                if data[i+1] == "=":
                    symbol = data[i:i+2]
                    symbols.append(cls.TRANSLIATERATOR_LEXEM(symbol, lexem_classes.get(symbol, error_message)))
                    i += 2
                    continue
            symbols.append(cls.TRANSLIATERATOR_LEXEM(symbol, lexem_classes.get(symbol, error_message)))
            i += 1
        return symbols


    @classmethod
    def process_chain_to_lexems(cls, chain: str) -> List[namedtuple]:
        translyator_chain = []
        i = 0
        while i < len(chain):
            if chain[i].isalpha():
                if chain[i] == "d" and chain[i + 1] == "i" and chain[i + 2] == "v":
                    i += 3
                    p = "div"
                    translyator_chain.append(cls.TRANSLIATERATOR_LEXEM(p, "arithmetic sign"))
                    continue
                elif chain[i] == "m" and chain[i + 1] == "o" and chain[i + 2] == "d":
                    i += 3
                    p = "mod"
                    translyator_chain.append(cls.TRANSLIATERATOR_LEXEM(p, "arithmetic sign"))
                    continue
                else:
                    translyator_chain.append(cls.TRANSLIATERATOR_LEXEM(chain[i], "letter"))
            elif chain[i].isdigit():
                translyator_chain.append(cls.TRANSLIATERATOR_LEXEM(chain[i], "digit"))
            elif chain[i] == " ":
                translyator_chain.append(cls.TRANSLIATERATOR_LEXEM(chain[i], "space"))
            elif chain[i] == ":":
                translyator_chain.append(cls.TRANSLIATERATOR_LEXEM(chain[i], "col"))
            elif chain[i] == "=":
                translyator_chain.append(cls.TRANSLIATERATOR_LEXEM(chain[i], "equal sign"))
            elif chain[i] == "+" or chain[i] == "-" or chain[i] == "*":
                translyator_chain.append(cls.TRANSLIATERATOR_LEXEM(chain[i], "arithmetic sign"))
            elif chain[i] == ";":
                translyator_chain.append(cls.TRANSLIATERATOR_LEXEM(chain[i], "semicolon"))
            elif chain[i] == "[":
                translyator_chain.append(cls.TRANSLIATERATOR_LEXEM(chain[i], "sqrbrkt1"))
            elif chain[i] == "]":
                translyator_chain.append(cls.TRANSLIATERATOR_LEXEM(chain[i], "sqrbrkt2"))
            elif chain[i] == "(":
                translyator_chain.append(cls.TRANSLIATERATOR_LEXEM(chain[i], "brkt1"))
            elif chain[i] == ")":
                translyator_chain.append(cls.TRANSLIATERATOR_LEXEM(chain[i], "brkt2"))
            else:
                translyator_chain.append(cls.TRANSLIATERATOR_LEXEM(chain[i], "error"))
            i += 1
        return translyator_chain


#symbols = Transliterator.transliteration("repeat f(1) until A[i+j]modB[i+j]<>Max;")
#for symbol in symbols:
#    print(f"{symbol.symbol}: {symbol.cls}")