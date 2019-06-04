import random
import turingarena as ta

for i in range(10):
    ta.evallib.evaluation.send_data(dict(type="value", key=f"field_{i}", value=i**2))

for _ in range(50):

    side_range = range(0, 6)
    side1, side2, side3 = random.choices(side_range, k=3)
    answer = ["scalene", "not", "isoscele", "equilateral"]

    with ta.run_algorithm(ta.submission.source) as process:
        index = process.functions.type(side1, side2, side3)

    solution = answer[index]

    try:
        print(f"Sides: {side1}, {side2}, {side3} ...", end="")
        print(f"answer: {solution}", end="")

        if a + b > c and a + c > b and b + c > a and a > 0 and b >0 and c > 0:
            if a != b and b != c and c != a:
                if index == 0:
                    print(" (correct)", end="")
                else:
                    print(" (WRONG!)", end="")
                    ta.goals["correct"] = False
                               
            elif (a == b and a != c) or (a == c and b != c) or (c == b and a != b):
                if index == 2:
                    print(" (correct)", end="")
                else:
                    print(" (WRONG!)", end="")
                    ta.goals["correct"] = False
                    
            elif a == b and b == c:
                if index == 3:
                    print(" (correct)", end="")
                else:
                    print(" (WRONG!)", end="")
                    ta.goals["correct"] = False
            
        else:
            if index == 1:
                print(" (correct)", end="")
            else:
                print(" (WRONG!)", end="")
                ta.goals["correct"] = False
        print(f"{int(process.time_usage * 1000000)} us)")
        
