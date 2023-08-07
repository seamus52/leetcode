S = (range(1, 10))
A = S
B = S
cart = ((x,y) for x in A for y in B)

for e in cart:
    print(e)