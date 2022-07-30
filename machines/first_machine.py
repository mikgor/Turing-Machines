from consts import *
from custom_types import TransitionFunction
from turing_machine import TuringMachine


class FirstMachine(TuringMachine):
    """
    A machine to compute the sequence 0 1 0 1 0 1... (0 <blank> 1 <blank> 0...)
    It never reaches the final state.
    https://en.wikipedia.org/wiki/Turing_machine_examples
    """
    def __init__(self,
                 tape_string: str = "",
                 transition_function: TransitionFunction = None,
                 *args,
                 **kwargs):

        if transition_function is None:
            transition_function = {
                (STATE_0, SYMBOL_BLANK): (STATE_1, SYMBOL_0, MOVE_HEAD_RIGHT),
                (STATE_1, SYMBOL_BLANK): (STATE_3, SYMBOL_BLANK, MOVE_HEAD_RIGHT),
                (STATE_3, SYMBOL_BLANK): (STATE_4, SYMBOL_1, MOVE_HEAD_RIGHT),
                (STATE_4, SYMBOL_BLANK): (STATE_0, SYMBOL_BLANK, MOVE_HEAD_RIGHT),
            }

        super().__init__(tape_string=tape_string,
                         transition_function=transition_function,
                         initial_state=STATE_0,
                         final_states=set(),
                         tape_alphabet={SYMBOL_BLANK, SYMBOL_0, SYMBOL_1},
                         input_symbols={SYMBOL_BLANK, SYMBOL_0, SYMBOL_1},
                         *args,
                         **kwargs)
