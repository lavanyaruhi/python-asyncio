import random

def random_number_generator():
    while True:
        yield random.randint(1, 100)
        
rand_gen = random_number_generator()

for _ in range(5):
    print(next(rand_gen))
