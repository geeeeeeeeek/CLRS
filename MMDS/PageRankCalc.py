from pip.backwardcompat import raw_input

__author__ = 'Tong'


def page_rank(e=0.0001, depth=99999, scale=3):
    beta = float(raw_input("Beta: "))
    number = int(raw_input("Number of nodes: "))

    formula = []

    for count in range(number * number):
        temp = float(raw_input(">> "))
        formula.append(beta * temp + (1 - beta) / number)

    p = [1 / number] * number
    while True and depth >= 0:
        q = [0] * number
        for i in range(number):
            for j in range(number):
                q[i] += p[j] * formula[i * number + j]
        flag = True
        for count in range(number):
            if abs(p[count] - q[count]) >= e:
                flag = False
                break
        p = q
        depth -= 1
        if flag:
            break
    for i in range(number):
        print(p[i] * scale)


page_rank()