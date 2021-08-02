from random import randint

N = [randint(0, 3) for _ in range(randint(10, 20))]
print(N)
count = 0
for num in N:
    if num == 0:
        N.append(N.pop(N.index(num)))
        count += 1
print(N)
print(N[:N.index(0)])

