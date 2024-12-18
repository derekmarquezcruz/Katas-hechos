#Escriba una función que tome una cadena de una o más palabras y devuelva la misma cadena. 
#pero con todas las palabras que tengan cinco o más letras invertidas (como el nombre de este Kata). 
#Las cadenas que se pasen constarán únicamente de letras y espacios. Los espacios se incluirán solo cuando haya más de una palabra.
def spin_words(sentence):
    listed_sentence = sentence.split(" ")
    final_list = []
    for word in listed_sentence:
        if len(word) >= 5:
            word = list(word)
            final = "".join(word[::-1])
            final_list.append(final)
        else:
            final_list.append(word)
    return " ".join(final_list)

test.assert_equals(spin_words("Welcome"), "emocleW")
test.assert_equals(spin_words("to"), "to")
test.assert_equals(spin_words("CodeWars"), "sraWedoC")
