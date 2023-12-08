#!/usr/bin/python3

scores = [2, 3, 8, 32, 86, 99]

for score in scores:
    print(f"Before: {score}")
    if score < 90:
        score += 10
    else:
        pass
    print(f"After: {score}")
