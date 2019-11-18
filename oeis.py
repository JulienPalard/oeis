import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='')

parser.add_argument('--start', type= int, default=0)
parser.add_argument('--limit', type= int, default=17)

args = parser.parse_args()

def countdown():
    result = []
    for n in range(100,0,-7):
        if n >= 0:
            result.append(n)
    
    return result
            
print(countdown()[args.start:args.start + args.limit])


def parse_args():
    parser = argparse.ArgumentParser(description="Get all primes number.")
    parser.add_argument("--plot", help="Display graph.",action="store_true")
    parser.add_argument("--start", default=0, help="Begining value.",type=int)
    parser.add_argument("--limit", default=9999, help="Character to use as a replacement.",type=int)

    return parser.parse_args()

def A000040(start, end, plot=False):
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
    args = parse_args()
    prime_number(args.start,args.limit,args.plot)
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 