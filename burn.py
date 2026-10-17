import numpy as np
import game_0, game_1
def score_game(f):
    count_ls=[]
    random_array = np.random.randint(1,101,size=(100))
    for i in random_array:
        count_ls.append(f(i))
    score=int(np.mean(count_ls))
    #print(count_ls)
    print(score)
score_game(game_0.random_predict)