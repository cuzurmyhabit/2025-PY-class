for a in range (1, 400):                #a는 1이상이고 합이 400이니까 399까지
    for b in range (a + 1, 400 - a):    #b는 무조건 a보다 크고 a와 더해서 400
        c = 400 - a - b                 #그럼 c는 나머지 값
        if a < b < c and a*a + b*b == c*c:
            print("a = " + str(a) + " b = " + str(b) + " c = " + str(c))