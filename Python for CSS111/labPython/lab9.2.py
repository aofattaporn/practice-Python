import math
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
C = int(sys.argv[3])*math.pi/180
c = math.sqrt((a**2)+(b**2)-(2*a*b*math.cos(C)))
print(c)