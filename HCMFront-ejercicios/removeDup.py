def removeDup(a):
    test = list(a)
    out = []
    out=out + [test[0]]
    for indice in range(1,len(test)):
        if(test[indice]!=test[indice-1]):
            out = out + [test[indice]]
    print ''.join(out)

removeDup('aaaaaaabbbbbbbbbcb')
