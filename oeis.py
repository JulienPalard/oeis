import argparse
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

def main():
    if args.sequence == "A000010":
        return [phi(x) for x in range (1, args.limit)]
            
print(main())
