from consts import STATE_INITIAL, STATE_FINAL, MOVE_HEAD_RIGHT, MOVE_HEAD_NONE, SYMBOL_0, SYMBOL_1, SYMBOL_BLANK
from turing_machine import TuringMachine
from custom_types import TransitionFunction


class BinaryComplementMachine(TuringMachine):
    """
    A machine that swaps all 0s and 1s.
    """
    def __init__(self,
                 tape_string: str = "",
                 transition_function: TransitionFunction = None,
                 *args,
                 **kwargs) -> None:

        if transition_function is None:
            transition_function = {
                (STATE_INITIAL, SYMBOL_0): (STATE_INITIAL, SYMBOL_1, MOVE_HEAD_RIGHT),
                (STATE_INITIAL, SYMBOL_1): (STATE_INITIAL, SYMBOL_0, MOVE_HEAD_RIGHT),
                (STATE_INITIAL, SYMBOL_BLANK): (STATE_FINAL, SYMBOL_BLANK, MOVE_HEAD_NONE),
            }

        super().__init__(tape_string=tape_string,
                         transition_function=transition_function,
                         final_states={STATE_FINAL},
                         tape_alphabet={SYMBOL_BLANK, SYMBOL_0, SYMBOL_1},
                         input_symbols={SYMBOL_BLANK, SYMBOL_0, SYMBOL_1},
                         *args,
                         **kwargs)
