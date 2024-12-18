#Dada una cadena que incluye caracteres alfanuméricos ("3a4B2d"), se devuelve la expansión de esa cadena
#los valores numéricos representan la ocurrencia de cada letra que precede a ese valor numérico. 
#No debe haber caracteres numéricos en la cadena final.
def string_expansion(s):
    result = []
    repeat_count = 1

    for char in s:
        if char.isdigit():
            repeat_count = int(char) 
        else:
            result.append(char * repeat_count) 

    return ''.join(result)

test.assert_equals(string_expansion('3D2a5d2f'), 'DDDaadddddff')
test.assert_equals(string_expansion('4D1a8d4j3k'), 'DDDDaddddddddjjjjkkk')
test.assert_equals(string_expansion('4D2a8d4j2f'), 'DDDDaaddddddddjjjjff')
test.assert_equals(string_expansion('3n6s7f3n'), 'nnnssssssfffffffnnn')
test.assert_equals(string_expansion('0d4n8d2b'), 'nnnnddddddddbb')
test.assert_equals(string_expansion('0c3b1n7m'), 'bbbnmmmmmmm')
test.assert_equals(string_expansion('7m3j4ik2a'), 'mmmmmmmjjjiiiikkkkaa')
test.assert_equals(string_expansion('3A5m3B3Y'), 'AAAmmmmmBBBYYY')
test.assert_equals(string_expansion('5M0L8P1'), 'MMMMMPPPPPPPP')
test.assert_equals(string_expansion('2B'), 'BB')
test.assert_equals(string_expansion('7M1n3K'), 'MMMMMMMnKKK')
test.assert_equals(string_expansion('A4g1b4d'), 'Aggggbdddd')
