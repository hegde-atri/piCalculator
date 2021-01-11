import random


def calculate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2

        if distance <= 1:
            num_point_circle += 1

        num_point_total += 1

    return 4 * (num_point_circle / num_point_total)


print(calculate_pi(10_000))
#run calculate_pi(n) where n is the number of iterations; the more the number of iterations, the closer to the value of pi