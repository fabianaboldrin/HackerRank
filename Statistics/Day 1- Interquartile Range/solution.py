import statistics as st

x = int(input())
y = [int(x) for x in input().split(' ')]
z = [int(x) for x in input().split(' ')]

lista = []

for i in range(x):
    count = 0
    while(count < z[i]):
        count = count+1
        lista.append(y[i])
        
lista = sorted(lista)
med = len(lista)//2

Q1 = st.median(lista[:med])
Q3 = st.median(lista[med+1:])

print('{0}'.format(float(Q3-Q1)))


    
