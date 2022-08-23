def func():
    dna = list(map(str, input()))
    maior = 1
    atual = dna[0]
    count = 1
    for x in range(1, len(dna)):
        if (dna[x] == atual):
            count += 1
            
        else:
            atual = dna[x]
            if maior < count:
                maior = count
            count = 1
    
    if count == len(dna) or count > maior:
        print(count)
    else:
        print(maior)
        
func()