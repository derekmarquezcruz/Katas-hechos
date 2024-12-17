#El objetivo de este ejercicio es convertir una cadena en una nueva cadena en la que cada carácter de la nueva cadena es si ese carácter aparece solo una vez en la cadena original, o si ese carácter aparece más de una vez en la cadena original. 
#Ignore las mayúsculas y minúsculas al determinar si un carácter es un duplicado."("")"
def duplicate_encode(word):
    
    word_lower = word.lower()
    
    
    char_count = {}
    for char in word_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    
    encoded_string = ''.join('(' if char_count[char] == 1 else ')' for char in word_lower)
    
    return encoded_string
  
  test.assert_equals(duplicate_encode("din"),"(((")
        test.assert_equals(duplicate_encode("recede"),"()()()")
        test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
        test.assert_equals(duplicate_encode("(( @"),"))((")
