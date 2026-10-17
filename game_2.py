import numpy as np
def game_2(number):
    c=0
    low, high = 1, 101
    while True:
        c+=1
        predict=np.random.randint(low, high)
        if number==predict:
            break
        elif number < predict:
            high=predict#-1
        elif number > predict:
            low=predict#+1
        #print(f'try {c}, res {predict}')
    return c
game_2(66)