from typing import List
from collections import namedtuple


fsm = {"start": {"key_repeat": "keyword_repeat"},
       "keyword_repeat": {"ident": "func"},
       "func": {"brkt1": "funcparam"},
       "funcparam": {"int": "endparam"},
       "endparam": {"brkt2": "keyword_untill"},
       "keyword_untill": {"key_untill": "arr"},
       "arr": {"ident": "arr_start_param"},
       "arr_start_param": {"sqrbrkt1": "arr_first_summand"},
       "arr_first_summand": {"ident": "arr_sign"},
       "arr_sign": {"arithmet_sign": "arr_second_summand"},
       "arr_second_summand": {"ident": "arr_param_end"},
       "arr_param_end": {"sqrbrkt2": "ar_sign"},
       "ar_sign": {"arithmet_sign": "arr2"},
       "arr2": {"ident": "arr_start_param2"},
       "arr_start_param2": {"sqrbrkt1": "arr_first_summand2"},
       "arr_first_summand2": {"ident": "arr_sign2"},
       "arr_sign2": {"arithmet_sign": "arr_second_summand2"},
       "arr_second_summand2": {"ident": "arr_param_end2"},
       "arr_param_end2": {"sqrbrkt2": "comp_sign"},
       "comp_sign": {"compar_sign": "identifier"},
       "identifier": {"smcolon": "semicolon"},
       "semicolon": {}}

initial_state = "start"

admitting_states = ["semicolon"]


def syntax(words: List[namedtuple], initial_state: str = initial_state) -> bool:
    state = initial_state
    for word in words:
        transitions = fsm.get(state)
        if word.cls in transitions.keys():
            state = transitions.get(word.cls)
        else:
            print("REJECTED")
            return False
    print("ACCEPTED")
    return True
