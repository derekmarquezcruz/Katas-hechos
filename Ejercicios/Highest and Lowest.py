#En esta pequeña tarea, se le da una cadena de números separados por espacios y tiene que devolver el número más alto y el número más bajo.
  
def high_and_low(numbers): 
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))


  def fixed_tests():
    @test.it('Test Case 1')
    def basic_test_cases():
        test.assert_equals(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9");
    @test.it('Test Case 2')
    def basic_test_cases():
        test.assert_equals(high_and_low("1 2 3"), "3 1");
