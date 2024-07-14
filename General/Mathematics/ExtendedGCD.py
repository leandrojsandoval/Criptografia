def extendedGCD(p, q):
    u1, u2 = 1, 0
    v1, v2 = 0, 1
    while q != 0:
        r = p % q
        quotient = p // q
        p, q = q, r
        u = u1 - quotient * u2
        v = v1 - quotient * v2
        u1, u2 = u2, u
        v1, v2 = v2, v
    return u1, v1

# Given primes
p = 26513;
q = 32321;

# Calculate u, v
u, v = extendedGCD(p, q);

# Print the lower number between u and v as the flag
flag = min(u, v);
print("=================== Flag ===================");
print(flag);
