# Program to print prime numbers from 1 to 100

print("Prime numbers between 1 and 100 are:")

for num in range(2,101):
    for i in range(2, num):
        if num % i ==0:
            break
    else:
        print(num)
