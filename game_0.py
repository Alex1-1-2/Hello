import numpy as np
def random_predict(number):
    c=0
    while True:
        c+=1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    return c
#print(random_predict(25))