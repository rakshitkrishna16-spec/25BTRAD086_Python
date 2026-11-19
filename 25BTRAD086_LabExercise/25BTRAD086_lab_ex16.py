import random

def roll_dice(rolls):
    results = [random.randint(1, 6) for _ in range(rolls)]
    return results

print("Rolling dice 5 times:")
rolls = roll_dice(5)
print("Outcomes:", rolls)