def cost(n, b, k, m):
    c = 0
    while n >= 0:
        if (k * b) >= m and n >= k:
            c += m
            n = n - k
        else:
            c += b
            n = n - 1
    return c

