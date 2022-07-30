from consts import SYMBOL_BLANK, SYMBOL_0, SYMBOL_1
from machines.binary_counter import BinaryCounterMachine
from tests.utils.cases.turing_machine_case import TuringMachineTestCase
from turing_machine import TuringMachine


class TestBinaryCounterMachine(TuringMachineTestCase):
    machine: TuringMachine = BinaryCounterMachine

    def setUp(self) -> None:
        super().setUp()

    def test_compute(self, *args, **kwargs) -> None:
        super().test_compute(*args, **kwargs)

        self.assertEqual(self.turing_machine.compute(
            tape_string=f"0{SYMBOL_1}{SYMBOL_0}{SYMBOL_0}{SYMBOL_1}{SYMBOL_1}"
                        f"{SYMBOL_0}{SYMBOL_0}{SYMBOL_1}{SYMBOL_BLANK}"),
                         f"{SYMBOL_1}{SYMBOL_1}{SYMBOL_0}{SYMBOL_0}{SYMBOL_1}"
                         f"{SYMBOL_1}{SYMBOL_0}{SYMBOL_0}{SYMBOL_1}{SYMBOL_BLANK}")

        self.assertEqual(self.turing_machine.compute(
            tape_string=f"{SYMBOL_1}{SYMBOL_1}{SYMBOL_1}{SYMBOL_1}{SYMBOL_BLANK}"),
            f"{SYMBOL_0}{SYMBOL_0}{SYMBOL_0}{SYMBOL_0}{SYMBOL_1}")
