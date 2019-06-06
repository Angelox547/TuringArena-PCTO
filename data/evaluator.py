import random

import turingarena as ta
for _ in range(10):

    d = int(random.random()*35)+1
    m = int(random.random()*15)+1
    y = int(random.random()*3000)+1

    day30 = [4, 6, 9, 11]
    day31 = [1, 3, 5, 7, 8, 10, 12]

    esiste = 0

    with ta.run_algorithm(ta.submission.source) as process:
        n = process.functions.data(d, m, y)

    try:

        if m != 2:
            for i in range(4):
                if day30[i] == m:
                    if d > 0 and d < 31 and y > 0:
                        esiste = 1

            for i in range(7):
                if day31[i] == m:
                    if d > 0 and d < 32 and y > 0:
                        esiste = 1


        elif m == 2:
            if y > 0 and y%4 == 0:
                if d > 0 and d < 30:
                    esiste = 1

            elif y > 0 and y%4 != 0:
                if d > 0 and d < 29:
                        esiste = 1

        else:
            esiste = 0

        if n == esiste:
            if n == 0:
                print(str(d) + " " + str(m) + " " + str(y) + " non esiste")
            else:
                print(str(d) + " " + str(m) + " " + str(y) + " esiste")
            print(" correct \n")

        else:
            ta.goals["correct"] = False
            print("WRONG! \n")

    except ta.AlgorithmError as e:
        ta.goals["correct"] = False
        print(e)

ta.goals.setdefault("correct", True)