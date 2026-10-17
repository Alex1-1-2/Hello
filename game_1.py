import numpy as np
def game_1(number):
    c=0
    predict_number=np.random.randint(1,101)
    while predict_number != number:
        c+=1
        if predict_number < number:
            predict_number += 1
        elif predict_number > number:
            predict_number -= 1
    return c
#print(game_1(66))