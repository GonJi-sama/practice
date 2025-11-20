def block(x):
    x = int(x)

    for i in range(1, x+1, 1):
        for j in range(x, 0, -1):
            if j > i:
                print(" ", end = "")
            else:
                print("x", end = "")
        print("")

