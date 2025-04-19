def tax(m):
    if m <= 1000:
        tax = 0
    elif m <= 3000:
        tax = m * 0.03
    elif m <= 5000:
        tax = m * 0.04
    else:
        tax = m * 0.06
    return tax
 
m = float(input())
tax = tax(m)
tax_str = f"{tax:.2f}".rstrip('0').rstrip('.') if '.' in f"{tax:.2f}" else f"{int(tax)}"
print(tax_str)