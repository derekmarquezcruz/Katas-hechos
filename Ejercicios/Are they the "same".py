#Dados dos arrays y escriba una función (o) que compruebe si los dos arrays tienen los "mismos" elementos, con las mismas multiplicidades 
# (la multiplicidad de un miembro es el número de veces que aparece). 
# "Igual" significa, aquí, que los elementos en son los elementos en al cuadrado, independientemente del orden.abcomp(a, b)compSame(a, b)ba

def comp(array1, array2):
    
    if array1 is None or array2 is None:
        return False
    
    
    if len(array1) != len(array2):
        return False
    
    
    return sorted([x * x for x in array1]) == sorted(array2)
