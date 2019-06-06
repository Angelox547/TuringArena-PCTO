def primo(a):
    i = 2
    while i < a/2+1:
        if a % i == 0:
            return 0
        i += 1
    return 1
