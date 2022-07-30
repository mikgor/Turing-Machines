from consts import SYMBOL_0, SYMBOL_1, SYMBOL_BLANK
from machines.palindrome_detector import PalindromeDetectorMachine
from tests.utils.cases.turing_machine_case import TuringMachineTestCase
from turing_machine import TuringMachine


class TestPalindromeDetectorMachine(TuringMachineTestCase):
    machine: TuringMachine = PalindromeDetectorMachine

    def setUp(self) -> None:
        super().setUp()

    def test_compute(self, *args, **kwargs) -> None:
        super().test_compute(*args, **kwargs)

        self.assertEqual(self.turing_machine.compute(
            tape_string=f"{SYMBOL_1}{SYMBOL_0}{SYMBOL_0}{SYMBOL_0}{SYMBOL_BLANK}"),
            f"{SYMBOL_BLANK}{SYMBOL_BLANK}{SYMBOL_BLANK}{SYMBOL_0}{SYMBOL_BLANK}")
