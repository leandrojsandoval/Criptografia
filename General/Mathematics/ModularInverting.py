p = 13
g = 3

# Compute the inverse using Fermat's little theorem
flag = pow(g, p-2, p);
print("=================== Flag ===================");
print(flag);
