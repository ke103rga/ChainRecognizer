from typing import List
from collections import namedtuple


def syntax(words):
    state = "start"
    for s in words:
        if s.cls == "identifier":
            if state == "start":
                state = "name"
            else:
                return 0
        elif s.cls == "col":
            if state == "name":
                state = "equal"
            else:
                return 0
        elif s.cls == "equal sign":
            if state == "equal":
                state = "array"
            else:
                return 0
        elif s.cls == "identifier2":
            if state == "array":
                state = "arrayparam"
            else:
                return 0
        elif s.cls == "sqrbrkt1":  # ----------------------
            if state == "arrayparam":
                state = "arrayparam"
            elif state == "funcarr":
                state = "funcarrparam"
            else:
                return 0
        elif s.cls == "letter" or s.cls == "digit":
            if state == "arrayparam":
                state = "arrayparam"
            elif state == "funcarrparam":
                state = "funcarrparam"
            else:
                return 0
        elif s.cls == "sqrbrkt2":  # -------------------------
            if state == "arrayparam":
                state = "sign"
            elif state == "funcarrparam":
                state = "semicolon"
            else:
                return 0
        elif s.cls == "arithmetic sign":
            if state == "sign":
                state = "func"
            else:
                return 0
        elif s.cls == "identifier3":
            if state == "func":
                state = "funcarr"
            else:
                return 0
        elif s.cls == "brkt1":
            if state == "funcarr":
                state = "funcarr"
            else:
                return 0
        elif s.cls == "identifier4":
            if state == "funcarr":
                state = "funcarr"
            else:
                return 0
        # elif s.cls == "letter" or s.cls == "digit":
        #     if state == "funcarrparam":
        #         state = "funcarrparam"
        #     else:
        #         return 0
        elif s.cls == "brkt2":
            if state == "semicolon":
                state = "semicolon"
            else:
                return 0
    if state == "semicolon":
        return 1
    return 0
