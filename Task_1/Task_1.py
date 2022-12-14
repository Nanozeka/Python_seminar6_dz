# # Семинар 3. Задача 1
# # Задайте список из нескольких чисел. Напишите программу,
# #  которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# # *Пример:*

# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# import random # Вызываем функцию рандом


# arr = [] # Создаем пустой список(туда будут записываться рандомные значения)

# for i in range(0, 6): # Для длины списка(6 индексов)
#    arr.append(random.randint(0, 10)) # Задаем интервал чисел от 0 до 10


# def sum_neg_elem(array):
#     res = 0
#     for i in range(len(array)):
#         if i % 2 != 0: # Если индекс находится на нечетной позиции
#             res += array[i] # то к нему прибавляем индекс на такой же позиции
#     return(res) 

# print(arr)        
# print(f'Сумма элементов на нечетных позициях: {sum_neg_elem(arr)}') 

# # Улучшеный код с функцией map(без рандом)

new_list = list(map(int, input('Задайте список чисел через пробел: ').split())) # Создаем
# список из заданых пользователем чисел.Применяем функцию map(к каждому индексу)

print(f'Сумма элементов на нечетных позициях: {sum(new_list[1::2])}') # Применяем функцию 
# сумма для каждого индекса начиная с 1го с шагом 2. Т.е. для нечетных индексов