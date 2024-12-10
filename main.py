# Ethan Lawrence
# dec 10 2024
# Try it python crash course

# 7-5
def findcost(age):
    if age < 3:
        return "Free!"
    elif 2 < age < 12:
        return '$10'
    else:
        return '$15'

while True:
    age = input('What is your age?  ')
    if age.isdigit():
        age = int(age)
        print(f'the tickets will be {findcost(age)}.')
    else:
        print('Error: Input must be a number.')
        break

# 7-6
counter = 0
while counter < 6:
    age = input('What is your age? (type "quit" to quit)  ')
    if age.isdigit():
        age = int(age)
        print(f'the tickets will be {findcost(age)}.')
        counter += 1
    elif age == 'quit':
        break
    else:
        print('Error: Input must be a number.')
        break