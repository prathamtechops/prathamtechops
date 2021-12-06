user_input = int(input('How many starts do you want to print: '))
print('Type 1 or 04: ')
p = int(input())
new = bool(p)
if new ==True:
    for i in range(1,user_input+1):
        for j in range(1, i+1):
            print('*', end='')
        print()
elif new == False:
    for i in range(user_input,0, -1):
        for j in range(1, i+1):
            print('*', end='')
        print()
