import random
import math


def estimate_pi(samples):
    n_pnts_in_circle = 0
    for _ in range(samples):
        # Generate random point in unit square
        x = random.random()
        y = random.random()

        # Distance to origin again radius of unit circle
        # No need to sqrt() bcus we only need to know if the distance is less than or equal to 1
        # If you sqrt() some value that is below 1 it'll still be below 1, same for above 1
        distance = x**2 + y**2

        # distance < radius unit circle -> point is inside the unit circle
        if distance <= 1:
            n_pnts_in_circle += 1

    # 4x ratio of points in the circle (comes from (pi*r^2/(2r)^2) where r = 1)
    pi = 4 * n_pnts_in_circle / samples

    # Print results
    print("Estimated value of pi taking %d samples: %s" % (samples, pi))
    print("Off by %s" % abs(math.pi - pi))


if __name__ == '__main__':
    estimate_pi(5000)
