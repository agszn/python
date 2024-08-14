v1, v2 = map(int, input('Enter v1 and v3 separated by a space: ').split())
print('Values entered:', v1, v2)

list_of_values = [4, 5, 6, 27, 3, 9, 1, 11, 15, 13]

if v1 in list_of_values and v2 in list_of_values:
    print('Both values found in the list.')
    for i in list_of_values:
        pass
elif v1 in list_of_values or v2 in list_of_values:
    print('At least one value found in the list.')
else:
    print('No values found in the list.')
