import turingarena as ta
import random

for _ in range(10):

    n = random.randint(0, 100)
    s_evaluator = 0

    try:
        print(f"Testing {n} ...", end="")
        with ta.run_algorithm(ta.submission.source) as p:
            s = p.functions.sum_mult(n)
        print(f" answer: {s}", end="")

        for i in range (0, 100):
            s_evaluator = s_evaluator + (n * i)

        if s == s_evaluator:
            print(" (correct)", end="")
        else:
            print("  (WRONG!)", end="")
            ta.goals["correct"] = False
        print(f"(time: {int(p.time_usage * 1000000)} us)")

    except ta.AlgorithmError as e:
        print(f" error: {e}")
        ta.goals["correct"] = False

ta.goals.setdefault("correct", True)
