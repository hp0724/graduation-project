import matplotlib.pyplot as plt
data = [
    [138, 500-199],#0 0 1 입
    [139, 500-176],#1 2 3 왼쪽눈
    [128, 500-184],#2 45  오른쪽눈
    [127, 500-196],#3 67  왼쪽 귀
    [129, 500-198],#4 89   오른쪼 귀   // 얼굴

    [153, 500-204],#5 10 11  //left 어꺠
    [177, 500-186],#6 12 13 //right 어꺠
    [303, 500-40],#7 14 15 left 팔꿈치
    [305, 500-50],#8 16 17 right 팔꿈치
    [110, 500-298],#9 18 19 left 손목
    [117, 500-296],#10  20 21 right  손목
    [268, 500-84],#11 22 23  left 힙
    [322, 500-100],#12 24 25 right  힙
    [310, 500-52],#13 26 27 left 무릎
    [371, 500-165],#14 28 29 right  무릎
    [420, 500-265],#15 30 31 left 발목
    [409, 500-249],#16 32 33 right  발목

]

x, y = zip(*data)
plt.scatter(x, y)
plt.show()