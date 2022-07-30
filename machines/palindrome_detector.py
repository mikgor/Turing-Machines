from consts import *
from custom_types import TransitionFunction
from turing_machine import TuringMachine


class PalindromeDetectorMachine(TuringMachine):
    """
    A machine that returns 1 if  an input id s palindrome, or 0 otherwise.
    """
    def __init__(self,
                 tape_string: str = "",
                 transition_function: TransitionFunction = None,
                 *args,
                 **kwargs):

        if transition_function is None:
            transition_function = {
                (STATE_0, SYMBOL_BLANK): (STATE_1, SYMBOL_BLANK, MOVE_HEAD_LEFT),
                (STATE_0, SYMBOL_0): (STATE_0, SYMBOL_0, MOVE_HEAD_RIGHT),
                (STATE_0, SYMBOL_1): (STATE_0, SYMBOL_1, MOVE_HEAD_RIGHT),
                (STATE_1, SYMBOL_BLANK): (STATE_FINAL, SYMBOL_1, MOVE_HEAD_NONE),
                (STATE_1, SYMBOL_0): (STATE_2, SYMBOL_BLANK, MOVE_HEAD_LEFT),
                (STATE_1, SYMBOL_1): (STATE_4, SYMBOL_BLANK, MOVE_HEAD_LEFT),
                (STATE_2, SYMBOL_BLANK): (STATE_3, SYMBOL_BLANK, MOVE_HEAD_RIGHT),
                (STATE_2, SYMBOL_0): (STATE_2, SYMBOL_0, MOVE_HEAD_LEFT),
                (STATE_2, SYMBOL_1): (STATE_2, SYMBOL_1, MOVE_HEAD_LEFT),
                (STATE_3, SYMBOL_BLANK): (STATE_0, SYMBOL_BLANK, MOVE_HEAD_NONE),
                (STATE_3, SYMBOL_0): (STATE_0, SYMBOL_BLANK, MOVE_HEAD_RIGHT),
                (STATE_3, SYMBOL_1): (STATE_6, SYMBOL_1, MOVE_HEAD_NONE),
                (STATE_4, SYMBOL_BLANK): (STATE_5, SYMBOL_BLANK, MOVE_HEAD_RIGHT),
                (STATE_4, SYMBOL_0): (STATE_4, SYMBOL_0, MOVE_HEAD_LEFT),
                (STATE_4, SYMBOL_1): (STATE_4, SYMBOL_1, MOVE_HEAD_LEFT),
                (STATE_5, SYMBOL_BLANK): (STATE_0, SYMBOL_BLANK, MOVE_HEAD_NONE),
                (STATE_5, SYMBOL_0): (STATE_6, SYMBOL_0, MOVE_HEAD_NONE),
                (STATE_5, SYMBOL_1): (STATE_0, SYMBOL_BLANK, MOVE_HEAD_RIGHT),
                (STATE_6, SYMBOL_BLANK): (STATE_FINAL, SYMBOL_0, MOVE_HEAD_NONE),
                (STATE_6, SYMBOL_0): (STATE_6, SYMBOL_BLANK, MOVE_HEAD_RIGHT),
                (STATE_6, SYMBOL_1): (STATE_6, SYMBOL_BLANK, MOVE_HEAD_RIGHT),
            }

        super().__init__(tape_string=tape_string,
                         initial_state=STATE_0,
                         final_states={STATE_FINAL},
                         tape_alphabet={SYMBOL_BLANK, SYMBOL_0, SYMBOL_1},
                         input_symbols={SYMBOL_BLANK, SYMBOL_0, SYMBOL_1},
                         transition_function=transition_function,
                         *args,
                         **kwargs)
