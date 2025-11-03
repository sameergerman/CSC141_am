# 9-1 Restaurant Class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # For exercise 9-4

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    # Methods added in 9-4
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, customers):
        self.number_served += customers


# Exercise 9-1
restaurant = Restaurant("Kiku", "Japanese")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2 Three Restaurants
restaurant1 = Restaurant("Chipotle", "Mexican")
restaurant2 = Restaurant("McDonald's", "Fast Food")
restaurant3 = Restaurant("Wendy's", "Fast Food")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# 9-3 User Class
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0  # For exercise 9-5

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}, "
              f"Location: {self.location}, Email: {self.email}")

    def greet_user(self):
        print(f"Welcome back, {self.first_name}!")

    # Methods added in 9-5
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Exercise 9-3
user1 = User("Chris", "Smith", 21, "PA", "Csmith@email.com")
user2 = User("Ava", "Kelly", 19, "NJ", "ava@email.com")
user3 = User("Ben", "Parker", 25, "NY", "ben@email.com")

for user in (user1, user2, user3):
    user.describe_user()
    user.greet_user()

# 9-4 Number Served
print("Customers served:", restaurant.number_served)
restaurant.number_served = 15
print("Updated customers served:", restaurant.number_served)
restaurant.set_number_served(250)
print("After setting number served:", restaurant.number_served)
restaurant.increment_number_served(100)
print("After incrementing:", restaurant.number_served)

# 9-5 Login Attempts
new_user = User("Aaron", "Wiggins", 21, "MD", "AW@example.com")
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print("Login attempts:", new_user.login_attempts)
new_user.reset_login_attempts()
print("Login attempts after reset:", new_user.login_attempts)


# 9-6 Ice Cream Stand (Inheritance)
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print("-", flavor)


icecream = IceCreamStand("Sweet Treats", "Ice Cream",
                         ["Vanilla", "Chocolate", "Butter Pecan"])
icecream.display_flavors()


# 9-7 Admin Class (Inheritance)
class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin privileges:")
        for p in self.privileges:
            print("-", p)


admin1 = Admin("Sarah", "Jones", 33, "TX", "admin@example.com")
admin1.show_privileges()


# 9-8 Privileges Class
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print("-", privilege)


class Admin2(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()


admin2 = Admin2("Mookie", "Betts", 34, "LA", "MB@example.com")
admin2.privileges.show_privileges()


# 9-9 Battery Upgrade / Electric Car
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh!")


class ElectricCar:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.battery = Battery()


e_car = ElectricCar("Tesla", "Model 3")
e_car.battery.get_range()
e_car.battery.upgrade_battery()
e_car.battery.get_range()


# 9-13 Dice
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


print("\nRolling a 6-sided die:")
for _ in range(10):
    Die().roll_die()

print("\nRolling a 10-sided die:")
for _ in range(10):
    Die(10).roll_die()

print("\nRolling a 20-sided die:")
for _ in range(10):
    Die(20).roll_die()


# 9-14 Lottery
print("\nLottery:")
import random
lottery_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                'A', 'B', 'C', 'D', 'E']
winning_ticket = random.sample(lottery_list, 4)
print("Any ticket matching", winning_ticket, "wins a prize!")


# 9-15 Lottery Analysis
my_ticket = ['A', 3, 5, 'E']
attempts = 0

while True:
    attempts += 1
    pull = random.sample(lottery_list, 4)
    if pull == my_ticket:
        break

print(f"It took {attempts} attempts to win with ticket {my_ticket}!")
