from consts import SYMBOL_BLANK
from machines.binary_complement import BinaryComplementMachine
from machines.binary_counter import BinaryCounterMachine
from machines.first_machine import FirstMachine
from machines.palindrome_detector import PalindromeDetectorMachine

binary_complement_machine = BinaryComplementMachine()

print("Result:", binary_complement_machine.compute(f"010011001{SYMBOL_BLANK}"), "\n")
print("Result:", binary_complement_machine.compute(f"1100111{SYMBOL_BLANK}"), "\n")

binary_counter_machine = BinaryCounterMachine()
print("Result:", binary_counter_machine.compute(f"010011001{SYMBOL_BLANK}"), "\n")
print("Result:", binary_counter_machine.compute(f"1011{SYMBOL_BLANK}"), "\n")

tape_string: str = f"{SYMBOL_BLANK}{SYMBOL_BLANK}{SYMBOL_BLANK}{SYMBOL_BLANK}" \
                   f"{SYMBOL_BLANK}{SYMBOL_BLANK}{SYMBOL_BLANK}{SYMBOL_BLANK}"
first_machine = FirstMachine(tape_string)
step_counter: int = 0
for i in range(len(tape_string)):
    print(f"Step {i}: {first_machine.step()}")
print("Result:", first_machine.tape_str(), "\n")

first_machine.reset_machine()

print("Result:", first_machine.compute(str.join('', [SYMBOL_BLANK]*99)), "\n")

palindrome_detector_machine = PalindromeDetectorMachine()
print("Result:", palindrome_detector_machine.compute(f"1000{SYMBOL_BLANK}"), "\n")
