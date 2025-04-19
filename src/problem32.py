r = []
for i in range(1000,10000):
        a = i // 100
        b = i %100
        c = a+b
        if i == c *c:
                r.append(str(i))
print(' '.join(r))