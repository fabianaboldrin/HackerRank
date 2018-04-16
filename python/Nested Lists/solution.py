if __name__ == '__main__':
    d = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[name] = score

lista = sorted(d.values())
s = []
for i in lista:
       if i not in s:
          s.append(i)

segMenor = s[1]

lista2 = []
for k, v in d.items():
    if v == segMenor:
        lista2.append(k)
        
print("\n".join(map(str, sorted(lista2))))

