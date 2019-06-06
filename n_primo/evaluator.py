import random

import turingarena as ta

for _ in range(10):
    prim = 1
    i = 2
    a = int(random.random()*100)

    with ta.run_algorithm(ta.submission.source) as process:
        n = process.functions.primo(a)


    try:

        while i < a/2+1:
            if a % i == 0:
                prim = 0

            i += 1

        if n == prim:
            if n == 0:
                print(str(a) + " non primo")
            else:
                print(str(a) + " primo")
            print(" correct \n")

        else:
            ta.goals["correct"] = False
            print("WRONG!")

    except ta.AlgorithmError as e:
        ta.goals["correct"] = False
        print(e)

ta.goals.setdefault("correct", True)
