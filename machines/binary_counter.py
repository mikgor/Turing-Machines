from consts import *
from turing_machine import TuringMachine


class BinaryCounterMachine(TuringMachine):
    """
    Increments the input number by 1.
    """
    def __init__(self, tape_string="") -> None:
        transition_function = {
            (STATE_0, SYMBOL_BLANK): (STATE_1, SYMBOL_BLANK, MOVE_HEAD_RIGHT),
            (STATE_0, SYMBOL_0): (STATE_0, SYMBOL_0, MOVE_HEAD_LEFT),
            (STATE_0, SYMBOL_1): (STATE_0, SYMBOL_1, MOVE_HEAD_LEFT),
            (STATE_1, SYMBOL_BLANK): (STATE_2, SYMBOL_1, MOVE_HEAD_LEFT),
            (STATE_1, SYMBOL_0): (STATE_2, SYMBOL_1, MOVE_HEAD_RIGHT),
            (STATE_1, SYMBOL_1): (STATE_1, SYMBOL_0, MOVE_HEAD_RIGHT),
            (STATE_2, SYMBOL_BLANK): (STATE_FINAL, SYMBOL_BLANK, MOVE_HEAD_RIGHT),
            (STATE_2, SYMBOL_0): (STATE_2, SYMBOL_0, MOVE_HEAD_LEFT),
            (STATE_2, SYMBOL_1): (STATE_2, SYMBOL_1, MOVE_HEAD_LEFT),
        }

        super().__init__(tape_string=tape_string,
                         initial_state=STATE_0,
                         final_states={STATE_FINAL},
                         tape_alphabet={SYMBOL_BLANK, SYMBOL_0, SYMBOL_1},
                         input_symbols={SYMBOL_BLANK, SYMBOL_0, SYMBOL_1},
                         transition_function=transition_function)
