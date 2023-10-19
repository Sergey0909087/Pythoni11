# 1
# num = int(input("Enter num 0-10: "))
# if num in range(0, 11):
#     for i in range(1, 11):
#         print(num, '*', i, '=', num * i)
# else:
#     print("Ввел не то число")

# 2
# import time

# start = time.time()
# time.sleep(3)
# stop = time.time()
# print(int(stop - start))

# # 2
# amount = int(input("Enter amount or 0 to finish"))
# while amount > 0:
#     cur_1 = int(input('Ваша валюта:\n1 - Rub\n2 - Eur\n3 - usd\nEnter: '))
#     cur_2 = int(input('В какую конвертируем:\n1 - uan\n2 - Eur\n3 - usd\nEnter'))
# #ниже представлены условия для конвертации рублей в другую валюту, вне зависимости от выбора стартовой валюты оно будет конвертировать только по рублям
#     if cur_1 in range(1, 4) and cur_2 in range(1, 4):
#         if cur_1 == cur_2:
#             print(amount)
#         elif cur_1 == 1:
#             if cur_2 == 2:
#                 print(amount / 105)
#             elif cur_2 == 3:
#                 print(amount / 99)
#         elif cur_1 == 2:
#             if cur_2 == 1:
#                 print(amount * 105)
#             elif cur_2 == 3:
#                 print(amount / 1.05)
#         elif cur_1 == 3:
#             if cur_2 == 1:
#                 print(amount * 100)
#             elif cur_2 == 2:
#                 print(amount * 1.05)
#     else:
#         print('Incorrect')
#     amount = int(input("Введи 0 и я прекращю работу: "))
# else:
#     print('See you soon!')

#3
# start = int(input('Enter start of range: '))
# stop = int(input('Enter and of range: '))
# num = int(input('Enter num: '))
# while num not in range(start, stop + 1):
#     print('\n' + str(num), 'not in range')
#     num = int(input('Enter num: '))
# for i in range(start, stop + 1):
#     if num == i:
#         print('!' + str(i) + '!', end=' ')
#     else:
#         print(i, end=' ')

#4
# import random


# number = random.randint(1, 501)
# print(number)

# from random import randint
# number = randint(1, 501)
# print(number)

# import time

# start = time.time()
# time.sleep(4)
# stop = time.time()
# print(int(stop - start))

# from time import time
# start = time()

#4
from random import randint
from time import time

start = time()
secret_num = randint(1, 501)
quess = int(input("Try to quess: "))
attempts = 1
while quess != secret_num and quess != 0:
    if quess < secret_num:
        print('My number is lagger')
    else:
        print('My number is laser!')
    quess = int(input("Try to quess: "))
    attempts += 1
stop = time()
if quess == secret_num:
    print('Поздравляю! you quess it!\nAttempts:', attempts, '\nTime:', int(stop - start), 'seconds')
else:
    print('Better luck next time...\nAttempts:', attempts, '\nTime:', int(stop - start), 'seconds')