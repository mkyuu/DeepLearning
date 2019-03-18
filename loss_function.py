import numpy as np

def square_sum(y,t):
    '''y = 出力値
    　 t = 正解値
    '''
    return 1.0/2.0 * np.sum(np.square(y-t)) #二乗和誤差

y = np.array([2,2,2,2])
t = np.array([1,1,1,1])
print(square_sum(y,t))

def cross_entropy(y,t):
    '''y = 出力値
    　 t = 正解値
    '''
    return -np.sum(t * np.log(y + 1e-7)) #交差エントロピー誤差