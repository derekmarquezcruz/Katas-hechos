#Complete el método/función para que convierta las palabras delimitadas por guiones/guiones bajos en mayúsculas y minúsculas. 
#La primera palabra dentro de la salida debe escribirse en mayúscula solo si la palabra original estaba en mayúscula (conocida como mayúscula y minúscula mayúscula, también conocida como mayúscula y minúscula de Pascal). 
#Las siguientes palabras siempre deben ir en mayúsculas.

def to_camel_case(s):
    if not s:
        return ""
    
    
    palabras = s.replace('-', ' ').replace('_', ' ').split()
    
    
    if s[0].isupper():
        palabras[0] = palabras[0].capitalize()
    
    
    palabras[1:] = [palabra.capitalize() for palabra in palabras[1:]]
    return ''.join(palabras)
  
test.assert_equals(to_camel_case(""), "", "An empty string was provided but not returned")
test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")
