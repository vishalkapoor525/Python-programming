#Program for finding odd and even number from list of numbers
numbers = [20,30,40,50,60,7,5,3,6]
print("created list is : ", numbers)

choice = int(input("Menu item \n 1. print even numbers \n 2. Print odd numbers \n"))
if choice == 1:
    for i in numbers:
        if (i%2==0):
            print(i)
else:
    for i in numbers:
        if (i%2!=0):
            print(i)
