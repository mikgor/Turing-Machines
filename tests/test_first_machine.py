import random

from consts import SYMBOL_BLANK, SYMBOL_0, SYMBOL_1
from machines.first_machine import FirstMachine
from tests.utils.cases.turing_machine_case import TuringMachineTestCase
from turing_machine import TuringMachine


class TestFirstMachine(TuringMachineTestCase):
    machine: TuringMachine = FirstMachine

    def setUp(self) -> None:
        super().setUp()

    def test_compute(self, *args, **kwargs) -> None:
        super().test_compute(*args, **kwargs)

        tape_string: str = f"{SYMBOL_BLANK}{SYMBOL_BLANK}{SYMBOL_BLANK}{SYMBOL_BLANK}" \
                           f"{SYMBOL_BLANK}{SYMBOL_BLANK}{SYMBOL_BLANK}{SYMBOL_BLANK}"

        self.assertEqual(self.turing_machine.compute(tape_string=tape_string),
                         f"{SYMBOL_0}{SYMBOL_BLANK}{SYMBOL_1}{SYMBOL_BLANK}"
                         f"{SYMBOL_0}{SYMBOL_BLANK}{SYMBOL_1}{SYMBOL_BLANK}")

        tape_length = random.randint(1, 100)
        tape_string: str = str.join('', [SYMBOL_BLANK]*tape_length)

        self.assertEqual(self.turing_machine.compute(
            tape_string=tape_string), self.fake.first_machine_tape_str(tape_length=tape_length))
