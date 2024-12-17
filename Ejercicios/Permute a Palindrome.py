#Escriba una función que compruebe si CUALQUIER permutación de los caracteres de la cadena de entrada es un palíndromo.
#Puntos de bonificación para una solución que es eficiente y/o que utiliza solo funciones de lenguaje integradas. 
#Considérate brillante si puedes llegar a una versión que no use ninguna función en absoluto.

def permute_a_palindrome(s):
    from collections import Counter
    
    char_count = Counter(s)
    
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    
    return odd_count <= 1
  
  def sample_tests():
    
    @test.it('input = a')
    def sample_test1():
        test.assert_equals(permute_a_palindrome("a"), True)
    
    @test.it('input = aa')
    def sample_test2():
        test.assert_equals(permute_a_palindrome("aa"), True)
        
    @test.it('input = aaa')
    def sample_test3():
        test.assert_equals(permute_a_palindrome("aaa"), True)
        
  
