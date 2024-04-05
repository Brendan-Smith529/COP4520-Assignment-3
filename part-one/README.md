# Part One 

## Proof of Correctness:
The solution properly solves the problem since the linked list
is designed to be concurrent and therefore thread-safe. Additionally,
the action the servants choose is randomized based on a RNG. Along with
that, the present chosen from the bag to removed and searched for are also
chosen by a randomly generated index based on how many presents are left
in the bag 

## Efficiency:
Python is inherently slow due to its nature, but this version is
faster than a sequential version since multiple 'servants' are working
on the process at one time 

## Experimental Evaluation:
The number of servants and presents was pre-determined so there was not much
experimentation. What was done, however, was giving the options to easily change
the present count or number of servants. Along with this, a version was tested with
only a single thread running and multiple ways with a multi-threaded approach to ensure
the completion of the tasks 

## To run the file (no output):
Disclaimer: This will take a long time to run
```
python3 presents.py
```
