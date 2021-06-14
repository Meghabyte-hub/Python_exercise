n = int(input("Type a number: "))
square_dict = {}
i=1
while i<=n:
    square_dict[i] = i*i
    i+=1
print(square_dict)