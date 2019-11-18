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

def A000079(start=0, limit=20, plot=False):
    seq = []
    for n in range(start, limit):
        seq.append(2**n)

    if plot:
        plt.plot(seq, 'r-o', label='power')
        plt.title = "Power"
        plt.show()
        return seq
    else:
        return seq

def main():
    args = parse_args()

    if args.sequence == "A181391":
        return A181391(args.start, args.limit, args.plot)
    elif args.sequence == "A115020":
        return A115020()[args.start : args.start + args.limit]
    elif args.sequence == "A000010":
        return [A000010(x) for x in range(1, args.limit)]
    elif args.sequence == "A000079":
        return A000079(args.start, args.limit, args.plot)


if __name__ == "__main__":
    print(main())

