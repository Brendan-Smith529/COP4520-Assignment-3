# Part One 

## Proof of Correctness:
The solution properly solves the problem since the linked list
is designed to be concurrent and therefore thread-safe. Additionally,
the action the servants choose is randomized based on a RNG. Along with
that, the present chosen from the bag to removed and searched for are also
chosen by a randomly generated index based on how many presents are left
in the bag 

## Efficiency:
The brute force and initial way to complete the algorithm can be rather slow.
For example, if it was set up with only a list that removed elements and if
the linked list was singly-linked instead of doubly-linked.

I drastically increased runtime by creating a list and shuffling it, like
the slower version, but then turned the bag with presents into a queue for
faster removal times; from O(n) to O(1) for all 500,000 removals. Another
efficiency change is making the concurrent linked list doubly-linked to achieve
O(1) operations.

## Experimental Evaluation:
The number of servants and presents was pre-determined so there was not much
experimentation to do in that regard. What was done, however, was testing
the different data structures and looking into how to optimize. For exampe,
from singly-linked to doubly-linked lists and lists to queues for faster popping.
The runtime for the final version was much faster than the fully unoptimized version.

14 minutes -> 2-3 seconds

## To run the file (no output):
Disclaimer: This will take a long time to run
```
python3 presents.py
```
