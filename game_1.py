import numpy as np
def game_1(number):
    c=0
    predict_number=np.random.randint(1,101)
    while True:
        c+=1
        if number > predict_number:
            number-=1
        elif number < predict_number:
            number+=1
        elif number == predict_number:
            break
    return c
print(game_1(66))