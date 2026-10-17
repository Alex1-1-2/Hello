import numpy as np
def game_2(number):
    c=0
    predict=np.random.randint(1,101)
    while number != predict:
        c+=1
        if number < predict:
            predict /= 2
        elif number > predict:
            predict += 1
    return c
