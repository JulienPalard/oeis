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
        "sequence", type=str, help="Define the sequence to run (e.g.: A181391)",
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
        default=1,
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


def A006577(n):

    if n == 1:
        return 0

    x = 0

    while True:

        if n % 2 == 0:
            n /= 2

        else:
            n = 3 * n + 1

        x += 1

        if n < 2:
            break

    return x


def A000142(start=0, limit=20, plot=False):
    sequence = []
    x = []
    for i in range(start, start + limit):
        sequence.append(math.factorial(i))
        x.append(i)

    if plot:
        plt.plot(x, sequence)
        plt.show()

    return sequence


def A000290(start=0, limit=20, plot=False):
    sequence = []
    x = []
    for i in range(start, start + limit):
        sequence.append(i * i)
        x.append(i)

    if plot:
        plt.plot(x, sequence)
        plt.show()

    return sequence


def A000079(start=0, limit=20, plot=False):
    sequence = []
    for i in range(start, start + limit):
        sequence.append(2 ** i)

    if plot:
        plt.plot(sequence)
        plt.show()

    return sequence


def A000045(start=0, limit=20, plot=False):
    sequence = []
    sequence.append(0)
    sequence.append(1)
    for i in range(2, limit):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    if plot:
        plt.plot(sequence)
        plt.show()

    return sequence


def A115020():
    result = []
    for n in range(100, 0, -7):
        if n >= 0:
            result.append(n)

    return result


def A000040(start, end, plot=False):
    result = []
    resultIndex = []
    i = 0
    for val in range(start, end + 1):
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                result.append(val)
                resultIndex.append(i)
                i = i + 1
    if plot:
        plt.plot(resultIndex, result)
        plt.ylabel("some numbers")
        plt.show()

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
    i = 0
    for val in range(start, end + 1):
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                result.append(val)
                resultIndex.append(i)
                i = i + 1
    if plot:
        plt.plot(resultIndex, result)
        plt.ylabel("some numbers")
        plt.show()
    else:
        return result


def partitions(n):

    if n == 0:
        return []
    if n == 1:
        return [[1]]

    partition = [[n]]

    for i in range(1, n):
        for p in partitions(n - i):
            if [i] + p == sorted([i] + p):
                partition.append([i] + p)

    return partition


def A000041(n):
    return len(partitions(n))


def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)

def A000045():
    args = parse_args()

    numbers = []
    y_label = []
    for i in range(int(args.start), int(args.limit)+1):
        numbers.append(Fibonacci(i))
        y_label.append(i)
        
    
    if args.plot:
        with plt.style.context('dark_background'):
            plt.plot(y_label, numbers, 'r-o')

        plt.xlabel('x label')
        plt.ylabel('y label')
        plt.title("A000045 - Fibonacci")
        plt.show()
    return numbers

def main():

    args = parse_args()

    if args.sequence == "A181391":
        return A181391(args.start, args.limit, args.plot)
    elif args.sequence == "A000142":
        return A000142(args.start, args.limit, args.plot)
    elif args.sequence == "A000290":
        return A000290(args.start, args.limit, args.plot)
    elif args.sequence == "A000079":
        return A000079(args.start, args.limit, args.plot)
    elif args.sequence == "A000045":
        return A000045(args.start, args.limit, args.plot)
    elif args.sequence == "A115020":
        return A115020()[args.start : args.start + args.limit]
    elif args.sequence == "A000040":
        return A000040(args.start, args.limit, args.plot)
    elif args.sequence == "A000010":
        return [A000010(x) for x in range(1, args.limit)]
    elif args.sequence == "A006577":
        return [A006577(n) for n in xrange(1, 101)]
    elif args.sequence == "A000041":
        return A000041(args.start)
    elif args.sequence == "A000045":
        return A000045() 


if __name__ == "__main__":
    print(main())
