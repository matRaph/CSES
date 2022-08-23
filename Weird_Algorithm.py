def func(num):
    lista = [num]
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = (num * 3) + 1
        lista.append(num)
    print(*lista)

n = int(input())
func(n)