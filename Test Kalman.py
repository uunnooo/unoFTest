import numpy as np


measurements = [[7., 15.],
                [8., 14.],
                [9., 13.],
                [10., 12.],
                [11., 11.],
                [12., 10.]] # 위치[x,y]의 측정 결과

initial_xy = [6., 17.] #초기위치
dt = 0.1 #측정간격
x = np.array([[initial_xy[0]], [initial_xy[1]],
              [0.], [0.]]) #초기 위치와 초기 속도를 대입 한 '4 차원 상태 "

print(x)
print(x.shape)

u = np.array([[0.], [0.], [0.], [0.]]) # 외부요소
P = np.array([[0., 0., 0., 0.],
              [0., 0., 0., 0.],
              [0., 0., 100., 0.],
              [0., 0., 0., 100.]]) #공분산 행렬
F = np.array([[1., 0., dt, 0.],
              [0., 1., 0., dt],
              [0., 0., 1., 0.],
              [0., 0., 0., 1.]]) # 상태 전이 행렬
H = np.array([[1., 0., 0, 0],
              [0., 1., 0., 0.]]) # 관측행렬
R = np.array([[0.1, 0],
              [0, 0.1]]) # 노이즈

I = np.identity((len(x))) #4차원 단위 행렬

def kalman_filter(x, P) :

     for n in range(len(measurements)) :
          # 예측
          x = np.dot(F, x) + u
          P = np.dot(np.dot(F, P), F.T)

          #계측 업데이트
          Z = np.array([measurements[n]])
          y = Z.T - np.dot(H, x)
          S = np.dot(np.dot(H, P), H.T) + R
          K = np.dot(np.dot(P, H.T), np.linalg.inv(S))
          x = x + np.dot(K, y)
          P = np.dot((I - np.dot(K, H)), P)

     x = x.tolist()
     P = P.tolist()

     return x,P

print("6회 측정후 위치와 속도의 예측값：",kalman_filter(x, P)[0])