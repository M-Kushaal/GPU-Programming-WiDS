import random
import time

N = 5_000_000
count = 0

start = time.perf_counter()

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y <= 1:
        count += 1

pi_est = 4 * count / N

end = time.perf_counter()

print("Estimated Pi:", pi_est)
print("CPU runtime:", end - start)