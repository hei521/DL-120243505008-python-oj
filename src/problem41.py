from decimal import Decimal, getcontext
getcontext().prec = 20
 
data = list(map(str, input().split()))
repeat = int(data[0])
results = []
 
for i in range(repeat):
    x = Decimal(data[1 + 2*i])
    n = int(data[2 + 2*i])
    power = x ** n
     
    if power == power.to_integral_value():
        results.append(f"{power:.0f}")
    else:
        results.append(f"{power:.10f}".rstrip('0').rstrip('.') if '.' in f"{power:.10f}" else f"{power:.0f}")
 
print(' '.join(results))
 