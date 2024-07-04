def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [15,'17',{1,4}]
values_dict = {'a':116,'b':'217','c':True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [15,'20']
print_params(*values_list_2, 42)