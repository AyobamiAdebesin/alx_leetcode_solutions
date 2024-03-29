#!/usr/bin/python3

""" Suppose there is a circle. There are petrol pumps on
that circle. Petrol pumps are numbered 0 to N - 1(both inclusive).
You have two pieces of information corresponding to each of the petrol pump:
(1) the amount of petrol that particular petrol pump will give, and
(2) the distance from that petrol pump to the next petrol pump.

Initially, you have a tank of infinite capacity carrying no petrol.
You can start the tour at any of the petrol pumps. Calculate the first point
from where the truck will be able to complete the circle. Consider that the
truck will stop at each of the petrol pumps. The truck will move one kilometer
for each litre of the petrol
"""


def truckTour(petrolpumps):
    # Write your code here
    i = 0
    while i < len(petrolpumps):
        amt = petrolpumps[i][0]
        dist = petrolpumps[i][1]
        j = 1
        while amt - dist >= 0:
            if j == len(petrolpumps):
                return i
            else:
                amt_rem = amt - dist
                amt_rem += petrolpumps[(i+j) % len(petrolpumps)][0]
                dist = petrolpumps[(i+j) % len(petrolpumps)][1]
                amt = amt_rem
                j += 1
        i += 1
