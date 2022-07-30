from consts import MOVE_HEAD_LEFT, MOVE_HEAD_RIGHT
from tests.utils.cases.base_case import BaseTestCase
from turing_machine import TuringMachine


class TuringMachineTestCase(BaseTestCase):
    machine: TuringMachine = TuringMachine

    def setUp(self) -> None:
        tape_string = self.fake.tape_str()
        turing_machine = self._create_turing_machine(tape_string=tape_string)

        states = turing_machine.get_states()
        initial_state = turing_machine.initial_state()
        final_states = turing_machine.final_states()

        self.assertEqual(turing_machine.tape_str(), tape_string)
        self.assertEqual(turing_machine.current_state(), initial_state)
        self.assertEqual(turing_machine.current_head_position_index(), 0)
        self.assertIn(initial_state, states)

        if final_states is not None:
            for final_state in final_states:
                self.assertIn(final_state, states)

        self.assertTrue(turing_machine.current_state() == turing_machine.is_in_final_state()
                        if final_states is not None and initial_state in final_states
                        else turing_machine.current_state() != turing_machine.is_in_final_state())

        self.turing_machine = turing_machine

    def _create_turing_machine(self, *args, **kwargs) -> TuringMachine:
        turing_machine = self.machine(*args, **kwargs)

        return turing_machine

    def test_reset_machine(self) -> None:
        _ = self.turing_machine.step()
        self.turing_machine.reset_machine()

        self.assertEqual(self.turing_machine.current_state(), self.turing_machine.initial_state())
        self.assertEqual(self.turing_machine.current_head_position_index(), 0)

    def test_step(self) -> None:
        current_head_position_index = self.turing_machine.current_head_position_index()
        current_symbol = self.turing_machine.current_symbol()
        transition = (self.turing_machine.current_state(), current_symbol)

        transition_function = self.turing_machine.transition_function()

        if transition in transition_function:
            to_state, to_symbol, to_move_direction = transition_function[transition]
            previous_head_position_index = current_head_position_index
            move_value = 0

            if to_move_direction == MOVE_HEAD_LEFT:
                move_value = -1
            elif to_move_direction == MOVE_HEAD_RIGHT:
                move_value = 1

            step = self.turing_machine.step()
            to_symbol = to_symbol \
                if 0 <= previous_head_position_index < len(self.turing_machine.tape_str()) \
                else self.turing_machine.blank_symbol()

            self.assertEqual(self.turing_machine.current_state(), to_state)
            self.assertEqual(self.turing_machine.current_head_position_index(), previous_head_position_index+move_value)
            self.assertEqual(self.turing_machine.tape_str(), step)
            self.assertEqual(self.turing_machine.symbol_at_index(previous_head_position_index), to_symbol)

    def test_compute(self,
                     tape_string=None,
                     step_limit=1_000) -> None:
        if tape_string is None:
            tape_string = self.fake.tape_str(input_symbols=self.turing_machine.input_symbols(),
                                             blank_symbol=self.turing_machine.blank_symbol())

        self.turing_machine = self._create_turing_machine(tape_string=tape_string)
        step_counter: int = 0

        while not self.turing_machine.is_in_final_state():
            _ = self.turing_machine.step()
            step_counter += 1

            if step_counter >= step_limit:
                break

        result = self.turing_machine.tape_str()
        self.turing_machine.reset_machine()

        compute_result = self.turing_machine.compute(tape_string=tape_string,
                                                     step_limit=step_limit,
                                                     print_step=False,
                                                     reset_machine_at_final=True)

        self.assertEqual(compute_result, result)
