import numpy as np


def game_2(number):
    c = 0
    low, high = 1, 101
    while True:
        c += 1
        predict = np.random.randint(low, high)
        if number == predict:
            # print(f'final try {c}, pred {predict}, low {low}, high {high}')
            break
        elif number < predict:
            high = predict
        elif number > predict:
            low = predict
        # print(f'try {c}, pred {predict}, low {low}, high {high}')
    return c
