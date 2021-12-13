import matplotlib.pyplot as plt
data = [
    [200, 500-42],#0 0 1
    [208, 500-34],#1 2 3
    [196, 500-37],#2 45
    [225, 500-48],#3 67
    [195, 500-45],#4 89     // 얼굴

    [240, 500-79],#5 10 11  //left 어꺠
    [190, 500-79],#6 12 13 //right 어꺠
    [293, 500-88],#7 14 15 left 팔꿈치
    [135, 500-84],#8 16 17 right 팔꿈치
    [342, 500-85],#9 18 19 left 손목
    [93, 500-79],#10  20 21 right  손목
    [238, 500-192],#11 22 23  left 힙
    [202, 500-198],#12 24 25 right  힙
    [302, 500-260],#13 26 27 left 무릎
    [142, 500-211],#14 28 29 right  무릎
    [352, 500-308],#15 30 31 left 발목
    [141, 500-308],#16 32 33 right  발목

]

x, y = zip(*data)
plt.scatter(x, y)
plt.show()