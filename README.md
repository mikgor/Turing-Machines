# Turing Machines
A simple implementation of Turing Machine and its variations in Python.
## Turing machine
It's a model of computation originally invented by Alan Turing, that operates on an infinite memory tape divided into discrete cells.

> Each cell holds a single symbol from a finite set of symbols called the alphabet of the machine. It has a "head" that, at any point in the machine's operation, is positioned over one of these cells, and a "state" selected from a finite set of states. At each step of its operation, the head reads the symbol in its cell. Then, based on the symbol and the machine's own present state, the machine writes a symbol into the same cell, and moves the head one step to the left or the right, or stops the computation. The choice of which replacement symbol to write and which direction to move is based on a finite table that specifies what to do for each combination of the current state and the symbol that is read.

More: [Turing Machine - Wikipedia](https://en.wikipedia.org/wiki/Turing_machine).

## Implemented machines
### Turing Machine
Base class for each of machines.

### First Turing Machine
A machine to compute the sequence 0 1 0 1 0 1... (0 <blank> 1 <blank> 0...). It never reaches the final state.

### Binary Complement Machine
A machine that swaps all 0s and 1s.

### Binary Counter Machine
Increments the input number by 1.

### Palindrome Detector Machine
A machine that returns 1 if  an input id s palindrome, or 0 otherwise.

## Examples
Examples available in: _examples.py_ and _/tests_.

## Installing requirements.txt
   ```
   pip3 install -r requirements.txt
   ```

## Sources
* https://en.wikipedia.org/wiki/Turing_machine
* https://en.wikipedia.org/wiki/Turing_machine_examples
* https://python-course.eu/applications-python/turing-machine.php
* https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/turing-machine/four.html
