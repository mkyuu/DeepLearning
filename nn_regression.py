import numpy as np
import matplotlib.pyplot as plt


#ｘ、ｙ座標
X = np.arange(-1.0,1.0,0.2) #要素数は１０
Y = np.arange(-1.0,1.0,0.2)

# 出力を格納する10x10のグリッド
Z = np.zeros((10,10))

# 重み
w_im = np.array([[4.0,4.0],
                 [4.0,4.0]]) # 中間層 2x2の行列

w_mo = np.array([[1.0],
                [-1.0]]) # 出力層 2x1の行列

# バイアス
b_im = np.array([3.0,-3.0]) # 中間層
b_mo = np.array([0.1]) # 出力層

# 中間層
def middle_layer(x,w,b):
    u = np.dot(x,w) + b
    return 1/(1+np.exp(-u)) # シグモイド関数

# 出力層
def output_layer(x,w,b):
    u = np.dot(x,w) + b
    return u # 恒等関数

# グリッドの各マスでニューラルネットワークの演算
for i in range(10):
    for j in range(10):

        # 順伝播
        inp = np.array([X[i],Y[j]]) # 入力層
        mid = middle_layer(inp,w_im,b_im) # 中間層
        out = output_layer(mid,w_mo,b_mo) # 出力層

        # グリッドにNNの出力を格納
        Z[j][i] = out[0]

# グリッドの表示
plt.imshow(Z,"gray",vmin = 0.0, vmax = 1.0)
plt.colorbar()
plt.show()