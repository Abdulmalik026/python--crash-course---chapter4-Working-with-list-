multiples3 = list(range(3,31,3))
for value in multiples3:
    print(value)
print(multiples3)

print('\n \033[36m another style\033[0m')
multiple_3 = [ ]   
for value in range(3,31,3):
    multiple_3.append(value)
    print(value)
print(multiple_3)

print('\n When value is not attached to a list')
for value in range(3,31,3):
    print(value)

print('\n using comprehension list')
multiples = [value*1 for value in range(3,31,3)]
print(multiples)

    