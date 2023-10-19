# # Задание 1
# line = int(input("Введи размер стороны квадрата:"))
# for i in range(line):
#     print('*' * line)

# # Второе задание

# line = int(input("Введи размер стороны квадрата: "))
# line_2 = int(input("Введи высоту: "))
# for i in range(line):
#     print(' * ' * line_2)

# Третье задание

line = int(input("Введи размер стороны квадрата: "))
for i in range(line):
    if i == 0 or i == line - 1:
        print(' * ' * line)
    else:
        print()