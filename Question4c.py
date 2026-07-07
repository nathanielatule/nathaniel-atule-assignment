# Demonstrating between continue and break

print("using continue:")

for i in range (1, 11):
    if i == 5:
        continue
    print(i)

print("\nUsing break:")

for i in range(1, 11):
    if i == 5:
        break
    print(i)
    
