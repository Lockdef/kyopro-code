x = int(input())

while True:
    for i in range(2, x):
        if x % i == 0:
            x += 1
            break
    else:
        print(x)
        break
