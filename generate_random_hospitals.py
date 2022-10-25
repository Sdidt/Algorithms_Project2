import random
import sys


def gen_random_hospitals(nodes):
    h = random.randint(1, 15)
    hospitals = random.sample(nodes, h)
    print(h, hospitals)
    f = open("hospitals.txt", 'w')
    original_stdout = sys.stdout
    sys.stdout = f
    print('#' + str(h))
    for hosp in hospitals:
        print(hosp)
    sys.stdout = original_stdout