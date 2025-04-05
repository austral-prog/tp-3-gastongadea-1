def slice_simple():
    texto = "Awesome"
    texto=texto.lower()
    print (texto[:3])
    mid=int(len(texto)/2)
    print (texto[mid-1:mid+2])
    print(texto[:4]+texto[-2:])
