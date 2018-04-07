x = int(input())
y = [int(x) for x in input().split(' ')]

mean = sum(y)/x
variance = sum([(p - mean)**2 for p in y])
print('{0}'.format(round((variance/x) ** 0.5, 1)))

