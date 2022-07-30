from consts import SYMBOL_BLANK
from tests.utils.cases.base_case import BaseTestCase
from turing_machine import Tape


class TestTape(BaseTestCase):
    def setUp(self) -> None:
        tape_string = self.fake.tape_str()
        tape = self._create_tape_test_helper(tape_string=tape_string)

        self.assertEqual(tape.tape_str(), tape_string)
        self.assertEqual(tape.get_tape_alphabet(), set(tape_string))
        self.assertEqual(tape.get_initial_tape_alphabet(), set(tape_string))

        self.tape = tape

    def _create_tape_test_helper(self,
                                 tape_string="",
                                 blank_symbol=SYMBOL_BLANK) -> Tape:
        tape = Tape(tape_string=tape_string, blank_symbol=blank_symbol)

        return tape

    def test_read_cell(self) -> None:
        tape_string = self.tape.get_initial_tape_str()
        index = 0

        for symbol in tape_string:
            self.assertEqual(symbol, self.tape.read_cell(index))
            index += 1

        self.assertEqual(SYMBOL_BLANK, self.tape.read_cell(-1))
        self.assertEqual(SYMBOL_BLANK, self.tape.read_cell(index+1))

    def test_set_cell(self) -> None:
        tape_length = len(self.tape.tape_str())
        tape_string = self.fake.tape_str(min_length=tape_length, max_length=tape_length)

        index = 0
        for symbol in tape_string:
            self.tape.set_cell(index, symbol)
            self.assertEqual(symbol, self.tape.read_cell(index))
            index += 1

        self.assertEqual(tape_string, self.tape.tape_str())
