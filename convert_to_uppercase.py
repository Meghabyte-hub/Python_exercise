line = []
while True:
    x = input()
    if len(x)==0:
        break
    line.append(x.upper())

for i in line:
    print(i)