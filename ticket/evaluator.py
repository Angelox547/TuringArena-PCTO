import turingarena as ta
import random

for _ in range(10):

    n = random.randint(0, 100)
    b = random.randint(0, 100)
    k = random.randint(0, 100)
    m = random.randint(0, 100)

    c_eval = 0

    with ta.run_algorithm(ta.submission.source) as process:
            c_tot = int(process.functions.cost(n, b, k, m))

    try:
        print(f"Viaggi {n} ...", end="")
        print(f" spesa {c_tot}", end="")
        while n >= 0:
            if (k * b) >= m and n >= k:
                c_eval += m
                n = n - k
            else:
                c_eval += b
                n = n - 1

        if c_tot == c_eval:
            print(" (correct)", end="")
        else:
            print("  (WRONG!)", end="")
            ta.goals["correct"] = False

        print(f"(time: {int(process.time_usage * 1000000)} us)")

    except ta.AlgorithmError as e:
        print(f" error: {e}")
        ta.goals["correct"] = False

ta.goals.setdefault("correct", True)
