import math

def dominoPiling(n):
    n = int(n.split(' ')[0]) * int(n.split(' ')[1])
    print(math.floor(n / 2))
    
dominoPiling(input())