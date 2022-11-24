pizzas = ['Domino', 'La Veranda', 'La Pizza', 'Red peppe', 'Pepperoni', 'Umutu coffee']
friend_pizzas= pizzas[ : ]
pizzas.append('chicago pizza')
friend_pizzas.append('adai pizza')
print(pizzas)
print(friend_pizzas)
print('My favourite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favourite pizzas are:")
for value in friend_pizzas:
    print(value)
