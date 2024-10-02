#Первый вариант без применения операторов continue и break
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# a = 0 #index
# while a<len(my_list) and my_list[a] >= 0:
#         if my_list[a] > 0:
#             print(my_list[a])
#         a += 1

#Второй вариант с применением оператора contnue
# my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# a = 0 #index
# while a<len(my_list):
#         if my_list[a] <= 0:
#             a += 1
#             continue
#         print(my_list[a])
#         a += 1

# #Третий вариант с применением оператора break
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0 #index
while a<len(my_list) and my_list[a] >= 0:
    if my_list[a] < 0:
        break
    if my_list[a] != 0:
        print(my_list[a])
    a += 1