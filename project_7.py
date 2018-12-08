from random import randint

list_ = [randint(-100, 100) for num in range(25)]
print(list_)

i = s = 0
i0 = i1 = i2 = i3 = i4 = 0
while i < 25:
    if list_[i] > 0:
        if s == 0:
            i0 = i
        elif s == 1:
            i1 = i
        elif s == 2:
            i2 = i
        elif s == 3:
            i3 = i
        elif s == 4:
            i4 = i
            break
        s += 1
    i += 1

multiply = list_[i0] * list_[i1] * list_[i2] * list_[i3] * list_[i4]
print('Индексы элементов:', i0, i1, i2, i3, i4)
print('Произведение первых пяти положительных элементов:')
print('{} * {} * {} * {} * {} = {}'.format(list_[i0], list_[i1], list_[i2], list_[i3], list_[i4], multiply))
