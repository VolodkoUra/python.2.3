"""Создайте список [ 18, 14, 10, 6, 2 ]  с помощью функции range()"""


def power():
    #Способ 1
    l = list(range(18, 0, -4))
    print(l)

    #Способ 2
    l1 = []
    for item in range(18,0,-4):
        l1.append(item)
    print(l1)


if __name__ == '__main__':
    power()


