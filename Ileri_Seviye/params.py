def toplam(a,b):
    return a+b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b
def cikarma(a,b):
    return a-b

def islem(a,b,c,d,islem):
    if islem == "toplam":
        print(toplam(a,b))
    elif islem == "carpma":
        print(carpma(a,b))
    elif islem == "bolme":
        print(bolme(a,b))
    elif islem == "cikarma":
        print(cikarma(a,b))
    
islem(2,3,4,5,"toplam")
islem(2,3,4,5,"carpma")
islem(2,3,4,5,"bolme")
islem(2,3,4,5,"cikarma")