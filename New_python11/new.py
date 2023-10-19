# var = 1
# print(var > 0)
# print(not(var <= 0))

# print(var != 0)
# print(not(var == 0))

a = 1 
b = 10
c = int(input())
while c not in range(a, b):
    c = int(input())
else:
    print('succes')