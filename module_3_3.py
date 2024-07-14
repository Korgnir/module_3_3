# Задача 1.

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

print() # Задача 2.

values_list = (40, False, 'poker')
values_dict = {'a': True, 'b': 'chest', 'c': 1000}
print_params(*values_list)
print_params(**values_dict)

print() # Задача 3.

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)