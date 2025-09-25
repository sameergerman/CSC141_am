# 5-1. Conditional Tests

car = 'suburu'
print("Is car == 'suburu'? I predict True.")
print(car == 'suburu')  # True

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # False

age = 20
print("\nIs age >= 18? I predict True.")
print(age >= 18)  # True

print("\nIs age < 18? I predict False.")
print(age < 18)  # False

name = "Sameer"
print("\nIs name == 'Sameer'? I predict True.")
print(name == "Sameer")  # True

print("\nIs name.lower() == 'sameer'? I predict True.")
print(name.lower() == "sameer")  # True

print("\nIs name == 'Chris'? I predict False.")
print(name == "Chris")  # False

fruits = ["apple", "banana", "watermelon"]
print("\nIs 'banana' in fruits? I predict True.")
print("banana" in fruits)  # True

print("\nIs 'blueberry' in fruits? I predict False.")
print("grape" in fruits)  # False

score = 95
print("\nIs score > 90 and score < 100? I predict True.")
print(score > 90 and score < 100)  # True


# 5-2. More Conditional Tests

# --- Tests for equality and inequality with strings ---
car = "suburu"
print("Is car == 'suburu'? I predict True.")
print(car == "suburu")  # True


print("\nIs car != 'suburu'? I predict False.")
print(car != "suburu")  # False

# --- Tests using the lower() method ---
name = "Sameer"
print("\nIs name.lower() == 'sameer'? I predict True.")
print(name.lower() == "sameer")  # True

print("\nIs name.lower() == 'chris'? I predict False.")
print(name.lower() == "chris")  # False

# --- Numerical tests (==, !=, >, <, >=, <=) ---
age = 20
print("\nIs age == 21? I predict True.")
print(age == 21)  # True

print("\nIs age != 21? I predict False.")
print(age != 21)  # False

print("\nIs age > 18? I predict True.")
print(age > 18)  # True

print("\nIs age < 18? I predict False.")
print(age < 18)  # False

print("\nIs age >= 21? I predict True.")
print(age >= 21)  # True

print("\nIs age <= 18? I predict False.")
print(age <= 20)  # False

# --- Tests using 'and' and 'or' ---
score = 85
print("\nIs score > 80 and score < 90? I predict True.")
print(score > 80 and score < 90)  # True

print("\nIs score > 90 and score < 100? I predict False.")
print(score > 90 and score < 100)  # False

print("\nIs score > 80 or score < 60? I predict True.")
print(score > 80 or score < 60)  # True

print("\nIs score > 90 or score < 70? I predict False.")
print(score > 90 or score < 70)  # False

# --- Test whether an item is in a list ---
fruits = ["apple", "banana", "watermelon"]
print("\nIs 'banana' in fruits? I predict True.")
print("banana" in fruits)  # True

print("\nIs 'blueberry' in fruits? I predict true.")
print("banana" in fruits) # True

print("\nIs 'mango' in fruits? I predict False.")
print("mango" in fruits)  # False

# --- Test whether an item is not in a list ---
print("\nIs 'mango' not in fruits? I predict True.")
print("mango" not in fruits)  # True

print("\nIs 'apple' not in fruits? I predict False.")
print("apple" not in fruits)  # False


# -------------------------
# 5-3. Alien Colors #1
# -------------------------

# Version that passes (alien is green)
alien_color = 'green'

if alien_color == 'green':
    print("The player just earned 5 points!")

# Version that fails (no output)
alien_color = 'red'

if alien_color == 'green':
    print("The player just earned 5 points!")

# -------------------------
# 5-4. Alien Colors #2
# -------------------------

# Version that runs the if block
alien_color = 'green'

if alien_color == 'green':
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points.")

# Version that runs the else block
alien_color = 'yellow'

if alien_color == 'green':
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points.")

# -------------------------
# 5-5. Alien Colors #3
# -------------------------

# Version with green alien
alien_color = 'green'

if alien_color == 'green':
    print("The player just earned 5 points.")
elif alien_color == 'yellow':
    print("The player just earned 10 points.")
elif alien_color == 'red':
    print("The player just earned 15 points.")

# Version with yellow alien
alien_color = 'yellow'

if alien_color == 'green':
    print("The player just earned 5 points.")
elif alien_color == 'yellow':
    print("The player just earned 10 points.")
elif alien_color == 'red':   # <- colon is here
    print("The player just earned 15 points.")

# 5-7. Favorite Fruit

favorite_fruits = ["banana", "apple", "strawberries"]

if "banana" in favorite_fruits:
    print("You really like bananas!")

if "apple" in favorite_fruits:
    print("You really like apples!")

if "strawberries" in favorite_fruits:
    print("You really like strawberries!")

if "grape" in favorite_fruits:
    print("You really like watermelon!")

if "strawberries" in favorite_fruits:
    print("You really like strawberries!")


# -------------------------
# 5-7. Favorite Fruit
# -------------------------

favorite_fruits = ["banana", "apple", "watermelon"]

if "banana" in favorite_fruits:
    print("You really like bananas!")

if "apple" in favorite_fruits:
        print("You really like apples!")

if "watermelon" in favorite_fruits:
    print("You really like watermelon!")

if "grape" in favorite_fruits:
    print("You really like grapes!")

if "strawberry" in favorite_fruits:
    print("You really like strawberries!")


# -------------------------
# 5-8. Hello Admin
# -------------------------

usernames = ["admin", "Chris", "sean", "dakota", "sarah"]

for user in usernames:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")


# -------------------------
# 5-9. No Users
# -------------------------

usernames = []  # Try changing this to a list with names to test both cases

if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")


# -------------------------
# 5-10. Checking Usernames
# -------------------------

current_users = ["sameer", "sarah", "chris", "camryn", "admin"]
new_users = ["sameer", "quincy", "sarah", "jackson", "SARAH"]

# Convert all current usernames to lowercase for case-insensitive check
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new one.")
    else:
        print(f"The username '{new_user}' is available!")


# -------------------------
# 5-11. Ordinal Numbers
# -------------------------

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

#5-13 I would like to be able to make a stat checker for sports such as the nba, mlb and nfl. this could be helpful for betting sites.
