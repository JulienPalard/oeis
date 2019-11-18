import argparse
import matplotlib.pyplot as plt
import math

parser = argparse.ArgumentParser(description='')

parser.add_argument('sequence')
parser.add_argument('--start', type= int, default=0)
parser.add_argument('--limit', type= int, default=17)

args = parser.parse_args()

def countdown():
    result = []
    for n in range(100,0,-7):
        if n >= 0:
            result.append(n)
    
    return result

def phi(n):
    numbers = []
    i = 0
    for i in range(n):
        if math.gcd(i, n) == 1:
            numbers.append(i)
    return len(numbers)

def primeNumber(start, end, plot=False):
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

def main():
    if args.sequence == "A000010":
        return [phi(x) for x in range (1, args.limit)]
    if args.sequence == "A000040":
        return primeNumber(args.start,args.limit,args.plot)
            
print(countdown()[args.start:args.start + args.limit])


def parse_args():
    parser = argparse.ArgumentParser(description="Get all primes number.")
    parser.add_argument("--plot", help="Display graph.",action="store_true")
    parser.add_argument("--start", default=0, help="Begining value.",type=int)
    parser.add_argument("--limit", default=9999, help="Character to use as a replacement.",type=int)

    return parser.parse_args()

