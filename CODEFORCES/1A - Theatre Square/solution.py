import math
 
n, m, a = [int(i) for i in input().split(" ")]
 
fh = math.ceil(n / a)
fv = math.ceil(m / a)
 
print(fh * fv)
    