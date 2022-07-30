import itertools
from custom_types import TransitionFunction, TransitionFunctionKey

from consts import STATE_INITIAL, SYMBOL_BLANK, MOVE_HEAD_LEFT, MOVE_HEAD_RIGHT, MOVE_HEAD_DIRECTIONS

"""
Turing Machine is a model of computation originally invented by Alan Turing.
It operates on an infinite memory tape divided into discrete cells.

More: https://en.wikipedia.org/wiki/Turing_machine
"""


class Tape(object):
    def __init__(self,
                 tape_string: str = "",
                 blank_symbol: str = SYMBOL_BLANK) -> None:
        self.__initial_tape: str = tape_string
        self.__tape: list[str] = [cell for cell in tape_string]
        self.__blank_symbol: str = blank_symbol

    def tape_str(self) -> str:
        return str.join('', self.__tape)

    def get_tape_alphabet(self) -> set[str]:
        return set(self.tape_str())

    def get_initial_tape_str(self) -> str:
        return self.__initial_tape

    def get_blank_symbol(self) -> str:
        return self.__blank_symbol

    def get_initial_tape_alphabet(self) -> set[str]:
        return set(self.__initial_tape)

    def read_cell(self, index) -> str:
        if 0 <= index < len(self.__tape):
            return self.__tape[index]
        return self.__blank_symbol

    def set_cell(self, index, symbol) -> None:
        if 0 <= index < len(self.__tape):
            self.__tape[index] = symbol


class TuringMachine(object):
    def __init__(self,
                 tape_string: str = "",
                 blank_symbol: str = SYMBOL_BLANK,
                 initial_state: str = STATE_INITIAL,
                 final_states: set[str] = None,
                 tape_alphabet: set[str] = None,
                 input_symbols: set[str] = None,
                 transition_function: TransitionFunction = None) -> None:
        self.__tape: Tape = Tape(tape_string, blank_symbol)
        self.__blank_symbol: str = blank_symbol
        self.__initial_state: str = initial_state
        self.__head_position_index: int = 0
        self.__current_state: str = self.__initial_state
        self.__final_states: set[str] = set() if final_states is None else final_states
        self.__tape_alphabet: set[str] = set() if tape_alphabet is None else tape_alphabet
        self.__input_symbols: set[str] = set() if input_symbols is None else input_symbols
        self.__transition_function: TransitionFunction = \
            dict() if transition_function is None else transition_function

    def tape_str(self) -> str:
        return self.__tape.tape_str()

    def step(self) -> str:
        current_symbol: str = self.__tape.read_cell(self.__head_position_index)
        transition: TransitionFunctionKey = (self.__current_state, current_symbol)

        if transition in self.__transition_function:
            to_state, to_symbol, to_move_direction = self.__transition_function[transition]

            self.__tape.set_cell(self.__head_position_index, to_symbol)
            self.__current_state = to_state

            if to_move_direction == MOVE_HEAD_LEFT:
                self.__head_position_index -= 1
            elif to_move_direction == MOVE_HEAD_RIGHT:
                self.__head_position_index += 1

        return self.__tape.tape_str()

    def blank_symbol(self) -> str:
        return self.__blank_symbol

    def input_symbols(self) -> set[str]:
        return self.__input_symbols

    def final_states(self) -> set[str]:
        return self.__final_states

    def initial_state(self) -> str:
        return self.__initial_state

    def current_state(self) -> str:
        return self.__current_state

    def symbol_at_index(self, index) -> str:
        return self.__tape.read_cell(index)

    def current_symbol(self) -> str:
        return self.symbol_at_index(self.current_head_position_index())

    def current_head_position_index(self) -> int:
        return self.__head_position_index

    def transition_function(self) -> TransitionFunction:
        return self.__transition_function

    def reset_machine(self) -> None:
        self.__head_position_index: int = 0
        self.__current_state: str = self.__initial_state

    def compute(self,
                tape_string="",
                step_limit=1_000,
                print_step=False,
                reset_machine_at_final=True) -> str:
        self.__tape: Tape = Tape(tape_string, self.__blank_symbol)
        step_counter: int = 0

        while not self.is_in_final_state():
            step = self.step()
            step_counter += 1

            if print_step:
                print(f"Step {step_counter}: {step}")

            if step_counter >= step_limit:
                print(f"Step limit reached: {step_limit}")
                break

        if reset_machine_at_final:
            self.reset_machine()

        return self.__tape.tape_str()

    def is_in_final_state(self) -> bool:
        return self.__current_state in self.__final_states

    def get_states(self) -> set[str]:
        states: set[str] = set(itertools.chain(*[([transition[0], self.__transition_function[transition][0]])
                                                 for transition in self.__transition_function]))

        return {*states, self.__initial_state, *self.__final_states}

    def print_machine_details(self) -> None:
        print('--------------- Machine details ---------------')
        print(type(self).__name__)
        print('Q - set of states: ', self.get_states())
        print('Γ - set of the tape alphabet: ', self.__tape_alphabet)
        print('Σ - set of input symbols: ', self.__input_symbols)
        print('q0 - initial state: ', self.__initial_state)
        print('qf - final states: ', self.__final_states)
        print('b - blank symbol: ', self.__blank_symbol)
        print('δ - transition function:')
        print(f'|\tFrom state\t\t|\tFrom symbol\t|\t\t->\t\t|\t\tTo state\t\t\t|\tTo symbol\t|\tMove direction\t|')
        for transition in self.__transition_function:
            from_state, from_symbol = transition
            to_state, to_symbol, to_move_direction = self.__transition_function[transition]
            print(f'|\t{from_state}\t\t|\t{from_symbol}\t\t\t|\t\t->\t\t|\t\t{to_state}\t\t\t|\t{to_symbol}'
                  f'\t\t\t|\t{MOVE_HEAD_DIRECTIONS[to_move_direction]}\t\t\t|')
        print('---------------------------------------------\n')
