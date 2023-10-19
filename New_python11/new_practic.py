# size = int(input('enetr side: '))
# print(' * ' * size)
# for i in range(size - 2):
#     print(' * ' + '   ' * (size - 2) + ' * ')
# print(' * ' * size)

# for i in range(size):
#     pass

# for i in range(size):
#     if i == 0 or i == size - 1:
#         print(' * ' * size)
#     else:
#         print(' * ' + '   ' * (size - 2) + ' * ')

# side_1 = int(input("Enetr: "))
# side_2 = int(input("Enter second side: "))
# for i in range(side_1):
#     if i == 0 or i == side_1 - 1:
#         print(' * ' * side_2)
#     else:
#         print(' * ' + '   ' * (side_2 - 2) + ' * ')

# <--------------------------------------------------------->

num = int(input('Enter num: '))
choice = int(input('1 - \n2 - \n3 - \n4 - \nChoice: '))
while choice not in range(1, 5): 
    print('выбери один из вариков: ')
    choice = int(input('1 - \n2 - \n3 - \n4 - \nChoice: '))
if choice == 1:
    list = []
    while num != 0:
        list.append(num % 10)
        num = num // 10
    print(sum(list))
    print(len(list))
elif choice == 2:
    pass
elif choice == 3:
    pass
elif choice == 4:
    pass

print(num)
counter = 0
summa = 0
while num != 0:
    c = num % 10
    pass
    num = num // 10
    counter += 1
print(counter)
