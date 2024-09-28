immutable_var = (1, True, 'str')
print(immutable_var)

# immutable_var[0] = 5
# print(immutable_var)
# кортеж не изменяемый тип
# кортеж статичный тип, но если необходимо заменить элемент кортежа,
# то мы можем заменить кортеж целиком на другой кортеж
# для изменяемых типов лучше создавать list

mutable_list = [1, 2 , True, 'str']
mutable_list[0] = 2
mutable_list[1] = 999
mutable_list[2] = False
mutable_list[3] = "any str"
print(mutable_list)