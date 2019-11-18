"""
Tool that return a given sequence
"""
import argparse
import numpy as np
import matplotlib.pyplot as plt
import math

__version__ = "0.0.1"


def parse_args():
    parser = argparse.ArgumentParser(description="Print a sweet sequence")
    parser.add_argument(
        "sequence",
        metavar="S",
        type=str,
        help="Define the sequence to run (e.g.: A181391)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=20,
        help="Define the limit of the sequence, (default: 20)",
    )
    parser.add_argument(
        "--plot", action="store_true", help="Print a sweet sweet sweet graph"
    )
    parser.add_argument(
        "--start",
        type=int,
        default=0,
        help="Define the starting point of the sequence (default: 0)",
    )

    return parser.parse_args()


def A181391(start=0, limit=20, plot=False):
    sequence = [0]
    last_pos = {}

    for i in range(start + limit):
        new_value = i - last_pos.get(sequence[i], i)
        sequence.append(new_value)
        last_pos[sequence[i]] = i

    if plot:
        colors = []
        for i in range(start, start + limit):
            colors.append(np.random.rand())

        plt.scatter(
            range(start, start + limit),
            sequence[start : start + limit],
            s=50,
            c=colors,
            alpha=0.5,
        )
        plt.show()

    return sequence[start : start + limit]


def A115020():
    result = []
    for n in range(100, 0, -7):
        if n >= 0:
            result.append(n)

    return result


def A000010(n):
    numbers = []
    i = 0
    for i in range(n):
        if math.gcd(i, n) == 1:
            numbers.append(i)
    return len(numbers)

def A000040(start=0, end=999, plot=False):
    result = []
    resultIndex = []
    i=0
    for val in range(start, end + 1): 
        if val > 1: 
            for n in range(2, val): 
                if (val % n) == 0: 
                    break
            else: 
                result.append(val)
                resultIndex.append(i)
                i=i+1
    if plot:
        plt.plot(resultIndex,result)
        plt.ylabel('some numbers')
        plt.show()
    else:
        return result

def A008592(start, limit):
    nterms = limit + 1
    end = limit + start
    my_list = []
    i = 0
    print("A008592 sequence:")
    while i < end:
        my_list.append(i*10)
        i += 1
    return my_list[start:end]

def _partitions(n):
	
    if n == 0:
        return []
    if n==1:
        return [[1]]
    liste=[[n]]  
    for i in range(1,n):

        for p in _partitions(n-i):
            if [i]+p==sorted([i]+p):
                liste.append([i]+p)       
    return liste
def partitions(n):
    return len(_partitions(n))
def affiche(n):
    listes=_partitions(n)
    for i in range(0,len(listes)):
        print(listes[i])

def main():

    args = parse_args()
   
    if args.sequence == "A008592":
        return A008592(args.start, args.limit)
    if args.sequence == "A181391":
        return A181391(args.start, args.limit, args.plot)
    elif args.sequence == "A115020":
        return A115020()[args.start : args.start + args.limit]
    elif args.sequence == "A000040":
        return A000040(args.start, args.limit, args.plot)
    elif args.sequence == "A000010":
        return [A000010(x) for x in range(1, args.limit)]
    if args.sequence == "A000041":
        print(affiche(args.start))
        print(partitions(args.start))
        

    
if __name__=="__main__":
    print(main())
