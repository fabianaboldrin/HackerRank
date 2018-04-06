import statistics as st

raw = input()
y = sorted([int(x) for x in input().split(' ')])
x = len(y)//2
z = (len(y)//2) + 1

if len(y) % 2 == 0:
    Q2 = st.median(y)
    Q1 = st.median(y[:x])
    Q3 = st.median(y[x:])
else:
    Q2 = st.median(y)
    Q1 = st.median(y[:x])
    Q3 = st.median(y[z:])

print('{0}\n{1}\n{2}'.format(int(Q1), int(Q2), int(Q3)))
