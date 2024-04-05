# Part Two

## Proof of Correctness:
The solution properly solves the problem since eight threads
were concurrently collecting temperatures and storing them
into a shared memory state, in this case a list. 

The correctness of the differences and max/min temperatures
can also be observed based on the variations and probability.
The difference will never exceed 170 and the max and min change
based on randomness.


## Efficiency:
There is not much computational complexity, or computation in general,
but it is efficient since all eight threads only access the lock to
insert the number into the list and generate the random number before
trying to access the lock.

## Experimental Evaluation:
The experimental evaluation comes from testing a single-threaded version
to begin with. Afterwards, trying with multiple threads and different versions
of shared states such as lists, arrays, etc. To ensure randomness, the code
was tested multiple times and produced unique output most of them.


## To run the file
CL Output:
```
python3 temperature_module.py
```

File Output:
```
python3 temperature_module.py > output.txt
```
