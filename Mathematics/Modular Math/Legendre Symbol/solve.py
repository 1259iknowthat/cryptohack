from math import sqrt
from Crypto.Util.number import long_to_bytes
p = ...
ints= [..]
lengendre= lambda a: pow(a,(p-1)//2,p)
for _ in ints:
    if(lengendre(_)==1):
                t=pow(_,(p+1)//4,p)
                print(t)
