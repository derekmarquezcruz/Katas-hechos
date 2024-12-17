#Su tarea es escribir una función que haga exactamente lo que sugiere el título (por lo tanto, advertencia justa, tenga en cuenta que no está saliendo de ella simplemente lanzando un método de clasificación básico poco convincente allí) 
#con una lista de números enteros y el número esperado de elementos más pequeños para devolver "n"
def first_n_smallest(arr, n):
    if n == 0: return []
    reversed_array = arr[::-1]
    
    while len(reversed_array) != n:
        reversed_array.pop(reversed_array.index(max(reversed_array)))
    return reversed_array[::-1]

test.assert_equals(first_n_smallest([1,2,3,4,5],3), [1,2,3])
        test.assert_equals(first_n_smallest([5,4,3,2,1],3), [3,2,1])
        test.assert_equals(first_n_smallest([1,2,3,1,2],3), [1,2,1])
        test.assert_equals(first_n_smallest([1,2,3,-4,0],3), [1,-4,0])
        test.assert_equals(first_n_smallest([1,2,3,4,5],0), [])
        test.assert_equals(first_n_smallest([1,2,3,4,5],5), [1,2,3,4,5])
        test.assert_equals(first_n_smallest([1,2,3,4,2],4), [1,2,3,2])
        test.assert_equals(first_n_smallest([2,1,2,3,4,2],2), [2,1])
        test.assert_equals(first_n_smallest([2,1,2,3,4,2],3), [2,1,2])
        test.assert_equals(first_n_smallest([2,1,2,3,4,2],4), [2,1,2,2])
