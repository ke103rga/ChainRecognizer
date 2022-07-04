from typing import List
from collections import namedtuple
from transliterator import Transliterator

fsm = {"start": {"letter": "key-word_repeat", "space": "start"},
       "key-word_repeat": {"letter": "key-word_repeat", "space": "space1"},
       "space1": {"letter": "func", "space": "space1"},
       "func": {"letter": "func", "digit": "func", "brkt1": "funcparam_sing"},
       "funcparam_sing": {"digit": "funcparam", "dig_sign": "funcparam_firstdigit"},
       "funcparam_firstdigit": {"digit": "funcparam"},
       "funcparam": {"digit": "funcparam", "brkt2": "first_space2"},
       "first_space2": {"space": "space2"},
       "space2": {"letter": "keyword_untill", "space": "space2"},
       "keyword_untill": {"letter": "keyword_untill", "space": "space3"},
       "space3": {"letter": "arr1", "space": "space3"},
       "arr1": {"letter": "arr1", "digit": "arr1", "sqrbrkt1": "first_summand_ident1"},
       "first_summand_ident1": {"letter": "first_summand1", "space": "first_summand_ident1"},
       "first_summand1": {"letter": "first_summand1", "digit": "first_summand1",
                          "space": "in-dex_space1", "arithmet_sign": "index_space2", "dig_sign": "index_space2"},
       "index_space1": {"space": "index_space1", "arithmet_sign": "index_space2", "dig_sign": "index_space2"},
       "index_space2": {"space": "index_space2", "letter": "second_summand1"},
       "second_summand1": {"letter": "second_summand1", "digit": "second_summand1", "sqrbrkt2": "space4"},
       "space4": {"space": "space4", "arithmet_sign": "space5", "dig_sign": "space5"},
       "space5": {"letter": "arr2", "space": "space5"},
       "arr2": {"letter": "arr2", "digit": "arr2", "sqrbrkt1": "first_summand_ident2"},
       "first_summand_ident2": {"space": "first_summand_ident2", "letter": "first_summand2"},
       "first_summand2": {"letter": "first_summand2", "digit": "first_summand2",
                          "space": "index_space3", "arithmet_sign": "index_space4", "dig_sign": "index_space4"},
       "idex_space3": {"space": "idex_space3", "arithmet_sign": "index_space4", "dig_sign": "index_space4"},
       "index_space4": {"space": "index_space4", "letter": "second_summand2"},
       "second_summand2": {"letter": "second_summand2", "digit": "second_summand2", "sqrbrkt2": "space6"},
       "space6": {"space": "space6", "compar_sign": "space7"},
       "space7": {"space": "space7", "letter": "ident"},
       "ident": {"letter": "ident", "digit": "ident", "space": "space8"},
       "space8": {"space": "space8", "smcolon": "space9"},
       "space9": {"space": "space9"}}

initial_state = "start"

admitting_states = ["space9"]

LEXER_LEXEM: namedtuple = namedtuple('Lexem', ['symbol', 'cls'])


def lexical(symbols: List[namedtuple]) -> List[namedtuple]:
    words = []
    state = initial_state
    word = ""
    for symbol in symbols:
        transition = fsm.get(state)
        if symbol.cls in transition.keys():
            if symbol.cls != "space":
                word += symbol.symbol
            if transition.get(symbol.cls) == "space1" and word != "":
                words.append(LEXER_LEXEM(word, "ident"))
                word = ""
            elif transition.get(symbol.cls) == "funcparam_sign" and word != "":
                words.append(LEXER_LEXEM(word[:-1], "ident"))
                words.append(LEXER_LEXEM(symbol.symbol, symbol.cls))
                print(symbol.symbol)
                word = ""
            elif transition.get(symbol.cls) == "first_space2":
                words.append(LEXER_LEXEM(word[:-1], "int"))
                words.append(LEXER_LEXEM(symbol.symbol, symbol.cls))
                word = ""
            elif transition.get(symbol.cls) == "space3" and word != "":
                words.append(LEXER_LEXEM(word, "ident"))
                word = ""
            elif transition.get(symbol.cls) == "first_summand_ident1" and word != "":
                words.append(LEXER_LEXEM(word[:-1], "ident"))
                words.append(LEXER_LEXEM(symbol.symbol, symbol.cls))
                word = ""
            elif transition.get(symbol.cls) == "index_space2" and word != "":
                words.append(LEXER_LEXEM(word[:-1], "ident"))
                words.append(LEXER_LEXEM(symbol.symbol, "arithmet_sign"))
                word = ""
            elif transition.get(symbol.cls) == "space4":
                words.append(LEXER_LEXEM(word[:-1], "ident"))
                words.append(LEXER_LEXEM(symbol.symbol, symbol.cls))
                word = ""
            elif transition.get(symbol.cls) == "space5" and word != "":
                words.append(LEXER_LEXEM(symbol.symbol, symbol.cls))
                word = ""
            elif transition.get(symbol.cls) == "first_summand_ident2" and word != "":
                words.append(LEXER_LEXEM(word[:-1], "ident"))
                words.append(LEXER_LEXEM(symbol.symbol, symbol.cls))
                word = ""
            elif transition.get(symbol.cls) == "index_space4" and word != "":
                words.append(LEXER_LEXEM(word[:-1], "ident"))
                words.append(LEXER_LEXEM(symbol.symbol, "arithmet_sign"))
                word = ""
            elif transition.get(symbol.cls) == "space6":
                words.append(LEXER_LEXEM(word[:-1], "ident"))
                words.append(LEXER_LEXEM(symbol.symbol, symbol.cls))
                word = ""
            elif transition.get(symbol.cls) == "space7" and word != "":
                words.append(LEXER_LEXEM(symbol.symbol, symbol.cls))
                word = ""
            elif transition.get(symbol.cls) == "space8":
                words.append(LEXER_LEXEM(word, "ident"))
                word = ""
            elif transition.get(symbol.cls) == "space9":
                words.append(LEXER_LEXEM(word, symbol.cls))
                word = ""
            state = transition.get(symbol.cls)

        else:
            print("пизда", symbol.symbol)
            break
    return words


symbols = Transliterator.transliteration("repeat f(1) until A[i+j]modB[i+j]<>Max;")
for symbol in symbols:
    print(f"{symbol.symbol}: {symbol.cls}")
words = lexical(symbols)
for symbol in words:
    print(f"{symbol.symbol}: {symbol.cls}")
