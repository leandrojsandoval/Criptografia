def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Calculate gcd for a = 66528, b = 52920
a = 66528
b = 52920
print("=================== Flag ===================");
print(gcd(a, b));
