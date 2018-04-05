from itertools import groupby
result = []
for k,g in groupby((input()), int):
    a = '({0}, {1})'.format(len(list(g)),k)
    result.append(a)
    
print(*result)
