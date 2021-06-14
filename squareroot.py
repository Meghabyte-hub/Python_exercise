import math
C=50
H=30
D = list(map(int, input("Enter comma separated values: ").split(",")))
for i in D:
    P=((2 * C * i)/H)
    Q=math.sqrt(P)
    print(Q,end=",")