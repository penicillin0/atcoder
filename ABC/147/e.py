for i in range(5):
    for j in range(5):
        for k in range(5):
            print(i, j, i ^ j, bin(i ^ j), bin(i ^ j).count(1))
            print(j, k, j ^ k, bin(j ^ k))
            
