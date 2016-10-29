from sys import argv

# assumes an integer argument
for n in range(2, int(argv[1])):
    for i in range(2, n):
        if n % i == 0:
            # print(n, 'equals', i, '*', n//i)
            break
    else:
        print(n, 'is prime')
