from tests.utils.cases.turing_machine_case import TuringMachineTestCase
from turing_machine import TuringMachine


class TestTuringMachine(TuringMachineTestCase):
    machine: TuringMachine = TuringMachine

    def setUp(self) -> None:
        super().setUp()

    def test_compute(self, *args, **kwargs) -> None:
        super().test_compute(*args, **kwargs)
