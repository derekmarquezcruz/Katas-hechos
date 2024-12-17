#En este Kata,debe crear una función que tome una cantidad de moneda estadounidense en y devuelva un diccionario/hash que muestre la menor cantidad de monedas utilizadas para completar esa cantidad. 
#Las únicas denominaciones de monedas consideradas en este ejercicio son:
#Por lo tanto, el diccionario devuelto debe contener exactamente 4 pares clave/valor.centsPennies (1¢), Nickels (5¢), Dimes (10¢) and Quarters (25¢)

def loose_change(cents):

    coinKeys = ['Nickels', 'Pennies', 'Dimes', 'Quarters']
    coinValues = [5, 1, 10, 25]

    wallet = dict(zip(coinKeys, coinValues))

    coins = list(sorted(wallet.values()))

    change = []
    i = len(coins) - 1
    while cents > 0 and i >= 0:
        if cents >= coins[i]:
            cents = cents - coins[i]
            change.append(coins[i])
        else:
            i -= 1

    change_dict = dict.fromkeys(coinKeys, 0)
    for coinKeys in wallet:
        for coin in change:
            if wallet[coinKeys] == coin:
                change_dict[coinKeys] += 1

    return change_dict

test.assert_equals(loose_change(29),  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1})
test.assert_equals(loose_change(91),  {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3})
test.assert_equals(loose_change(0),   {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
test.assert_equals(loose_change(-2),  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
test.assert_equals(loose_change(3.9), {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0})
