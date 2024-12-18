#En este Kata, se le dará una matriz de números en la que dos números aparecen una vez y el resto aparecen solo dos veces. 
#Su tarea será devolver la suma de los números que aparecen solo una vez. 
#Por ejemplo, repeats([4,5,7,5,4,8]) = 15 porque solo los números 7 y 8 aparecen una vez y su suma es 15. Todos los demás números aparecen dos veces.
def repeats(arr):

    contador = {}
    for num in arr:
        if num in contador:
            contador[num] += 1
        else:
            contador[num] = 1
          
    suma = 0
    for num, count in contador.items():
        if count == 1:
            suma += num
    
    return suma
        test.assert_equals(repeats([4,5,7,5,4,8]),15)
        test.assert_equals(repeats([9, 10, 19, 13, 19, 13]),19)
        test.assert_equals(repeats([16, 0, 11, 4, 8, 16, 0, 11]),12)
        test.assert_equals(repeats([5, 17, 18, 11, 13, 18, 11, 13]),22)
        test.assert_equals(repeats([5, 10, 19, 13, 10, 13]),24)
