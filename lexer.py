from typing import List
from collections import namedtuple
from file_manager import FileManager
from keywords import PASCAL_KEYWORDS


class Lexer:
    LEXER_LEXEM: namedtuple = namedtuple('Lexem', ['symbol', 'cls'])

    @classmethod
    def lexical(cls, symbols:List[namedtuple]) -> List[namedtuple]:
        pass

    @classmethod
    def process_chain_to_lexems(cls, chain_of_lexems: List[namedtuple]) -> List[namedtuple]:
        lexer_chain = []
        now = [' ', 'None']
        state = "start"

        for s in chain_of_lexems:
            if s.cls == "letter":  # РІСЃС‚СЂРµС‡Р°РµРј Р‘СѓРєРІС‹
                if state == "start":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "identifier"
                    state = "name"
                elif state == "name":
                    now[0] += s.symbol
                elif state == "equ":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "identifier2"
                    state = "array"
                elif state == "array":
                    now[0] += s.symbol
                elif state == "arrayparam":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "letter"
                    state = "arrayparam"
                elif state == "space2":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "identifier3"
                    state = "func"
                elif state == "func":
                    now[0] += s.symbol
                elif state == "funcarr":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "identifier4"
                    state = "funcparam"
                elif state == "funcparam":
                    now[0] += s.symbol
                elif state == "funcarrparam":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "letter"
                    state = "funcarrparam"
                else:
                    FileManager.return_output(chain_detected=False)

            elif s.cls == "col":  # РІСЃС‚СЂРµС‡Р°РµРј :
                if state == "name":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "col"
                    state = "tdots"
                else:
                    FileManager.return_output(chain_detected=False)

            elif s.cls == "equal sign":  # РІСЃС‚СЂРµС‡Р°РµРј =
                if state == "tdots":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "equal sign"
                    state = "equ"
                else:
                    # print('equal sign')
                    FileManager.return_output(chain_detected=False)

            elif s.cls == "space":  # РІСЃС‚СЂРµС‡Р°РµРј РџСЂРѕР±РµР»
                if state == "arrayparam":
                    state = "space1"
                elif state == "space1":
                    state = "space1"
                elif state == "sign":
                    state = "space2"
                elif state == "semicolon":
                    pass
                else:
                    # print(now)
                    # print(words)
                    # print(state)
                    # print("space")
                    FileManager.return_output(chain_detected=False)

            elif s.cls == "digit":  # РІСЃС‚СЂРµС‡Р°РµРј Р§РёСЃР»Рѕ
                if state == "name":
                    now[0] += s.symbol
                elif state == "array":
                    now[0] += s.symbol
                elif state == "arrayparam":
                    now[0] += s.symbol
                elif state == "arrayparam":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "digit"
                    state = "arrayparam"
                elif state == "func":
                    now[0] += s.symbol
                elif state == "funcarr":
                    now[0] += s.symbol
                elif state == "funcarrparam":
                    now[0] += s.symbol
                elif state == "funcarrparam":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "digit"
                    state = "funcarrparam"
                elif state == "funcparam":
                    now[0] += s.symbol
                else:
                    # print("Digit")
                    FileManager.return_output(chain_detected=False)

            elif s.cls == "arithmetic sign":  # РІСЃС‚СЂРµС‡Р°РµРј РђСЂРёС„РјРµС‚РёС‡РµСЃРєРёР№ Р·РЅР°Рє
                if state == "space1":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "arithmetic sign"
                    state = "sign"
                elif state == "arrayparam":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "digit"
                    state = "arrayparam"
                elif state == "funcarrparam":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "digit"
                    state = "funcarrparam"
                else:
                    # print(now)
                    # print(state)
                    # print("ArithSign")
                    # print(words)
                    FileManager.return_output(chain_detected=False)

            elif s.cls == "semicolon":  # РІСЃС‚СЂРµС‡Р°РµРј ;
                if state == "semicolon":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "semicolon"
                    state = "semicolon"
                else:
                    # print("semicol")
                    FileManager.return_output(chain_detected=False)

            elif s.cls == "sqrbrkt1":  # РІСЃС‚СЂРµС‡Р°РµРј [
                if state == "array":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "sqrbrkt1"
                    state = "arrayparam"
                elif state == "func":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "sqrbrkt1"
                    state = "funcarr"
                elif state == "funcparam":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "sqrbrkt1"
                    state = "funcarrparam"
                else:
                    # print("[")
                    # print(now)
                    # print(words)
                    # print(state)
                    FileManager.return_output(chain_detected=False)

            elif s.cls == "sqrbrkt2":  # РІСЃС‚СЂРµС‡Р°РµРј ]
                if state == "arrayparam":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "sqrbrkt2"
                    state = "space1"
                elif state == "funcarrparam":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "sqrbrkt2"
                    state = "semicolon"
                else:
                    FileManager.return_output(chain_detected=False)

            elif s.cls == "brkt1":
                if state == "func":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "brkt1"
                    state = "funcarr"
                else:
                    FileManager.return_output(chain_detected=False)

            elif s.cls == "brkt2":
                if state == "semicolon":
                    lexer_chain.append(cls.LEXER_LEXEM(*now))
                    now[0] = s.symbol
                    now[1] = "brkt2"
                    state = "semicolon"
                else:
                    FileManager.return_output(chain_detected=False)


        lexer_chain.append(cls.LEXER_LEXEM(*now))
        lexer_chain.pop(0)

        # Блок идентификации ключевых слов
        cls._check_keywords(chain_of_lexems=lexer_chain)

        return lexer_chain

    @classmethod
    def _check_keywords(self, chain_of_lexems: List[namedtuple]) -> None:
        for lexem in chain_of_lexems:
            if lexem.cls == "identifier":
                # index = binary_search(chain_of_lexems[i].symbol.lower(), 0, len(keywords_list))
                if lexem.symbol.lower() in PASCAL_KEYWORDS:
                    FileManager.return_output(chain_detected=False)
