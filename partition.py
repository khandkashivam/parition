def parition(pArr, x, y):
    a, temp, sub, xDiff = 0, 0, 0, 0
    b, count, yDiff = 1, 1, 1

    while count > 0:
        if a == 4:
            a = -1
        else:
            count = (len(pArr)-1) - sub
            if count >= 0:
                if a < 2:
                    temp += pArr[count]
                else:
                    temp = temp - pArr[count]

                if b % 2 == 0:
                    sub += y[yDiff]
                    yDiff += 1
                else:
                    sub += x[xDiff]
                    xDiff += 1
                b += 1
        a += 1

    return temp

def main():
    p = [1, 1]
    n = int(input("enter n: "))

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    while len(p) < n+1:
        x.append(x[-1]+1)
        y.append(y[-1]+2)

        val = parition(p, x, y)

        p.append(val)

    print("p(" + str(n) + ") = " + str(p[n]))

main()
