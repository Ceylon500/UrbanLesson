#Работа с кортежем: создание и изменение
immutable_var='машинное обучение', 3, True
print(immutable_var)
#immutable_var[1]=13
print(immutable_var) #вывести кортеж с изменениями не получилось, так как данным тип объектов относится к неизменяемым
#Работа со списками
mutable_list=[1, 2, 3, 4, 5]
print(mutable_list)
mutable_list[2]=17
mutable_list[4]='Изменяемый объект'
print(mutable_list)

