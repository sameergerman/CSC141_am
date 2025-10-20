# ---------------------------
# 7-1. Rental Car
# ---------------------------
print("7-1. Rental Car")
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.\n")

# ---------------------------
# 7-2. Restaurant Seating
# ---------------------------
print("7-2. Restaurant Seating")
group_size = int(input("How many people are in your dinner group? "))
if group_size > 8:
    print("You'll have to wait for a table.\n")
else:
    print("Your table is ready.\n")

# ---------------------------
# 7-3. Multiples of Ten
# ---------------------------
print("7-3. Multiples of Ten")
number = int(input("Enter a number: "))
if number % 10 == 0:
    print(f"{number} is a multiple of 10.\n")
else:
    print(f"{number} is not a multiple of 10.\n")

# ---------------------------
# 7-4. Pizza Toppings
# ---------------------------
print("7-4. Pizza Toppings")
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")
print()

# ---------------------------
# 7-5. Movie Tickets
# ---------------------------
print("7-5. Movie Tickets")
while True:
    age_input = input("Enter your age (or 'quit' to stop): ")
    if age_input.lower() == 'quit':
        break
    age = int(age_input)
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"Your ticket price is ${price}.")
print()

# ---------------------------
# 7-6. Three Exits
# ---------------------------
print("7-6. Three Exits")
active = True
while active:
    topping = input("Enter a pizza topping (or 'quit' to stop, 'stop' to end loop): ")
    if topping.lower() == 'quit':  # break statement
        break
    if topping.lower() == 'stop':  # conditional test
        active = False
        continue
    print(f"I'll add {topping} to your pizza.")
print()

# ---------------------------
# 7-7. Infinity (commented out to avoid running forever)
# ---------------------------
# print("7-7. Infinity")
# while True:
#     print("This loop will never end!")

# ---------------------------
# 7-8. Deli
# ---------------------------
print("7-8. Deli")
sandwich_orders = ['turkey', 'breakfast', 'tuna', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("All sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)
print()

# ---------------------------
# 7-9. No Pastrami
# ---------------------------
print("7-9. No Pastrami")
sandwich_orders = ['pastrami', 'turkey', 'pastrami', 'breakfast', 'pastrami', 'tuna']
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print()

# ---------------------------
# 7-10. Dream Vacation
# ---------------------------
print("7-10. Dream Vacation")
responses = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")
    responses[name] = vacation

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, vacation in responses.items():
    print(f"{name} would like to visit {vacation}.")
