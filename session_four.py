# min number
import random
random_list = [random.choice(list(range(1, 100))) for _ in range(10)]
def get_min(random_list):
    min(random_list)
    print(min(random_list))
    pass
get_min(random_list)
