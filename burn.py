import numpy as np
import game_0
import game_1
import game_2


def score_game(f):
    count_ls = []
    random_array = np.random.randint(1, 101, size=(100))
    for i in random_array:
        count_ls.append(f(i))
    score = int(np.mean(count_ls))
    # print(count_ls)
    print(f'алгоритм угадывает за {score} попыт.')


print('проверка game_0: ', end='')
{score_game(game_0.random_predict)}
print('проверка game_1: ', end='')
score_game(game_1.game_1)
print('проверка game_2: ', end='')
score_game(game_2.game_2)
