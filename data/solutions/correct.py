def data(d, m, y):
    day30 = [4, 6, 9, 11]
    day31 = [1, 3, 5, 7, 8, 10, 12]

    if m != 2:
        for i in range(4):
            if day30[i] == m:
                if d > 0 and d < 31 and y > 0:
                    return 1

        for i in range(7):
            if day31[i] == m:
                if d > 0 and d < 32 and y > 0:
                    return 1
    elif m == 2:
        if y > 0 and y % 4 == 0:
            if d > 0 and d < 30:
                return 1

        elif y > 0 and y % 4 != 0:
            if d > 0 and d < 29:
                return 1
    else:
        return 0

    return 0
