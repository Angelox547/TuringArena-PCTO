def type(side1, side2, side3):
    if a + b > c and a + c > b and b + c > a and a > 0 and b >0 and c > 0:
        if a != b and b != c and c =! a:
            return 0
        elif (a == b and a != c) or (a == c and b != c) or (c == b and a != b):
            return 2
        elif a == b and b == c:
            return 3
    else:
        return 1
