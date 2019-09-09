# Not Yet Solved Properly

numlist = list(range(1,20))

num = 1

while True:
    TF=True
    for i in numlist:
        if num%i != 0:
            TF=False
            num+=1
            print(num)
            break
    if TF:
        print("끝!",num)
        break