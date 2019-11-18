import argparse

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
