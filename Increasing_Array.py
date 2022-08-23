def fn():
    n = int(input())
    n2 = list(map(int, input().split(" ")))
    movimentos = 0
    for x in range(1, len(n2)):
        diferenca = n2[x-1] - n[x]
        if  diferenca >= 0:
            n2[x] += diferenca
            movimentos += diferenca
        
    print(movimentos)

fn()