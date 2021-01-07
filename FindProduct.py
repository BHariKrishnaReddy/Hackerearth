    n = int(input())

    a = list(map(int, input().split()))

     

    ini = 1

    for i in range(len(a)):

            ini = (ini * a[i]) % (10**9 + 7)
     

    print(ini)
