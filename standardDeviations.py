import math
import statistics
a=[60, 61, 65, 63 ,98, 99 ,90, 95,91, 96]
n=len(a)
s=0
for i in a:
  s+=i
m=s/n
print("THIS IS THE MEAN" ,m)
x=[]
for i in a:
   b=i-m
   sq=b**2
   x.append(sq)
Sum=0
for i in x:
   Sum+=i
re=Sum/(n-1)
sd=math.sqrt(re)
print(sd)
test=statistics.stdev(a)
print(test)
