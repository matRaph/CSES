from posixpath import split


def func():
    n = int(input())
    n2 = list(map(int, input().split(" ")))
    n2.sort()
    for x in range(len(n2)):
        if x+1 != n2[x]:
            return print(x+1)
    return print(n)

func()