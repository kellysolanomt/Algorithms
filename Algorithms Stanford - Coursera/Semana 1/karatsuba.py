def karatsuba(x,y):
    if len(str(x)) < 10 and len(str(y)) < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    mitad = n // 2
    a = x // (10**mitad)
    b = x % (10**mitad)
    c = y // (10**mitad)
    d = y % (10**mitad)
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_mas_bc = karatsuba(a+b, c+d) - ac - bd
    resultado = ac * (10 ** (2*(mitad))) + ad_mas_bc * (10 ** mitad) + bd
    return resultado

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

# x = 1234
# y = 5678

print(f"El resultado es: {karatsuba(x,y)}")