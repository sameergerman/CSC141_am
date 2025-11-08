#  10-1 — Learning Python

print("\n--- 10-1 Learning Python ---")

with open(lp_file) as file:
    print(file.read())

with open(lp_file) as file:
    for line in file:
        print(line.rstrip())


#  10-2 — Replace Python → C
print("\n--- 10-2 Replace Python with C ---")
with open(lp_file) as file:
    for line in file:
        print(line.replace("Python", "C").rstrip())


#  10-3 — Loop using splitlines()
print("\n--- 10-3 Simpler Code ---")
with open(lp_file) as file:
    for line in file.read().splitlines():
        print(line)


#  10-4 — Guest
print("\n--- 10-4 Guest ---")
guest = input("What is your name? ")
with open(path("guest.txt"), "w") as file:
    file.write(guest)
print("Your name has been written to guest.txt!")


#  10-5 — Guest Book
print("\n--- 10-5 Guest Book (type 'quit' to stop) ---")
while True:
    name = input("Enter your name: ")
    if name.lower() == "quit":
        break
    with open(path("guest_book.txt"), "a") as file:
        file.write(name + "\n")
    print(f"Welcome, {name}!")


#  10-6 — Addition w/ Error Handling
print("\n--- 10-6 Addition ---")
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"The sum is: {a + b}")
except ValueError:
    print("Please enter valid numbers only!")


#  10-7 — Addition Calculator Loop
print("\n--- 10-7 Calculator ('q' to quit) ---")
while True:
    x = input("First number: ")
    if x == "q":
        break
    y = input("Second number: ")
    if y == "q":
        break

    try:
        print(f"Result: {int(x) + int(y)}")
    except ValueError:
        print("Error: Only numbers please!")


#  Create cats.txt and dogs.txt if missing
cats_file = path("cats.txt")
dogs_file = path("dogs.txt")

if not os.path.exists(cats_file):
    with open(cats_file, "w") as f:
        f.write("Juju\nTiny\nLulu\n")

if not os.path.exists(dogs_file):
    with open(dogs_file, "w") as f:
        f.write("Rex\nPepper\nMaple\n")


#  10-8 — Cats and Dogs (friendly error)
print("\n--- 10-8 Cats & Dogs ---")
for f in [cats_file, dogs_file]:
    try:
        with open(f) as file:
            print(f"\n{os.path.basename(f)}:")
            print(file.read())
    except FileNotFoundError:
        print(f"Sorry, {f} not found.")


#  10-9 — Silent Errors
print("\n--- 10-9 Silent Cats & Dogs ---")
for f in [cats_file, dogs_file]:
    try:
        with open(f) as file:
            print(file.read())
    except FileNotFoundError:
        pass


#  10-10 — Count “the ” in placeholder book files
print("\n--- 10-10 Count 'the ' in books ---")

books = ["book1.txt", "book2.txt", "book3.txt"]
for b in books:
    bf = path(b)
    if not os.path.exists(bf):
        with open(bf, "w") as f:
            f.write("The quarrel is between our masters and us their men..\n"
                    "Tis all one, I will show myself a tyrant: when I have fought with the men I will be civil with the maids, I will cut off their heads..\n")

    with open(bf) as file:
        text = file.read().lower()
        print(f"{b}: 'the ' appears {text.count('the ')} times")


#  10-11 & 10-12 — Favorite Number Remembered
print("\n--- 10-11 & 10-12 Favorite Number Remembered ---")
fav_file = path("favorite_number.json")
try:
    with open(fav_file) as file:
        fav_num = json.load(file)
except FileNotFoundError:
    fav_num = input("What is your favorite number? ")
    with open(fav_file, "w") as file:
        json.dump(fav_num, file)
    print("Thanks! I'll remember that.")
else:
    print(f"I know your favorite number! It's {fav_num}.")


#  10-13 — User Dictionary
print("\n--- 10-13 User Dictionary ---")
user_info = {
    "name": input("Your name: "),
    "age": input("Your age: "),
    "city": input("City: ")
}

with open(path("user_info.json"), "w") as file:
    json.dump(user_info, file)

with open(path("user_info.json")) as file:
    saved = json.load(file)
print("Saved info:", saved)


#  10-14 — Verify User

print("\n--- 10-14 Verify User ---")
username_file = path("username.json")

def get_new_username():
    username = input("What is your name? ")
    with open(username_file, "w") as file:
        json.dump(username, file)
    return username

def greet_user():
    try:
        with open(username_file) as file:
            username = json.load(file)
    except FileNotFoundError:
        username = get_new_username()
        print(f"We will remember you, {username}!")
    else:
        check = input(f"Are you {username}? (yes/no): ")
        if check.lower() == "yes":
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We will remember you, {username}!")

greet_user()

print("\n ALL EXERCISES COMPLETE ")
