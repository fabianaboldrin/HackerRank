
size = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

soma = []
for i in range(size):
    soma.append(x[i]*w[i])

print(round(sum(soma)/sum(w), 1))
