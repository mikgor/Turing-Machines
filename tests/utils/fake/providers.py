import random

from faker.providers import BaseProvider

from consts import SYMBOLS, SYMBOL_BLANK, SYMBOL_0, SYMBOL_1


class TapeProvider(BaseProvider):
    def tape_str(self,
                 input_symbols: set = None,
                 blank_symbol: str = None,
                 exclude_blank_symbol: bool = False,
                 blank_symbol_prefix: bool = False,
                 blank_symbol_suffix: bool = False,
                 min_length: int = 1,
                 max_length: int = 12) -> str:
        if input_symbols is None:
            input_symbols = SYMBOLS

        if blank_symbol is None:
            blank_symbol = SYMBOL_BLANK

        if exclude_blank_symbol:
            input_symbols.discard(blank_symbol)

        tape_str = blank_symbol if blank_symbol_prefix else ""
        input_symbols_tuple = tuple(input_symbols)

        if len(input_symbols_tuple) > 0:
            tape_str = tape_str.join(
                random.choices(
                    input_symbols_tuple,
                    k=random.randint(min_length, max_length)
                ))

        return tape_str + (blank_symbol if blank_symbol_suffix else "")

    def first_machine_tape_str(self,
                               tape_length: int = None,
                               blank_symbol: str = None) -> str:

        if blank_symbol is None:
            blank_symbol = SYMBOL_BLANK

        return (f"{SYMBOL_0}{blank_symbol}{SYMBOL_1}{blank_symbol}" * ((tape_length // 4) + 1))[:tape_length]
