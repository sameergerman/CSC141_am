# -------------------------------
# 8-1. Message
# -------------------------------
def display_message():
    print("I’m learning about functions in this chapter!")

display_message()


# -------------------------------
# 8-2. Favorite Book
# -------------------------------
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Harry Potter")


# -------------------------------
# 8-3. T-Shirt
# -------------------------------
def make_shirt(size, message):
    print(f"The shirt size is {size} and it says '{message}'.")

make_shirt("Large", "Just Do It")
make_shirt(size="Small", message="Work Hard Play Hard")


# -------------------------------
# 8-4. Large Shirts (Defaults)
# -------------------------------
def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and it says '{message}'.")

make_shirt()                     # Large with default message
make_shirt(size="Medium")        # Medium with default message
make_shirt(size="Small", message="All I play is baseball")  # Custom


# -------------------------------
# 8-5. Cities
# -------------------------------
def describe_city(city, country="USA"):
    print(f"{city.title()} is in {country.title()}.")

describe_city("Reykjavik", "Iceland")
describe_city("New York")
describe_city("Ontario", "Canada")


# -------------------------------
# 8-6. City Names
# -------------------------------
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

print(city_country("San Juan", "Puerto Rico"))
print(city_country("paris", "france"))
print(city_country("tokyo", "japan"))


# -------------------------------
# 8-7. Album
# -------------------------------
def make_album(artist, title, num_songs=None):
    album = {"artist": artist.title(), "title": title.title()}
    if num_songs:
        album["songs"] = num_songs
    return album

print(make_album("drake", "views"))
print(make_album("Giveon", "Beloved"))
print(make_album("Young Thug", "Punk", 12))


# -------------------------------
# 8-8. User Albums
# -------------------------------
def make_album(artist, title, num_songs=None):
    album = {"artist": artist.title(), "title": title.title()}
    if num_songs:
        album["songs"] = num_songs
    return album

while True:
    print("\nEnter album info (or type 'quit' to stop):")
    artist = input("Artist name: ")
    if artist.lower() == "quit":
        break
    title = input("Album title: ")
    if title.lower() == "quit":
        break

    album_info = make_album(artist, title)
    print(album_info)


# -------------------------------
# 8-9. Messages
# -------------------------------
def show_messages(messages):
    for message in messages:
        print(message)

messages = ["Hey!", "How are you?", "See you soon."]
show_messages(messages)


# -------------------------------
# 8-10. Sending Messages
# -------------------------------
def send_messages(messages, sent_messages):
    while messages:
        msg = messages.pop(0)
        print(f"Sending message: {msg}")
        sent_messages.append(msg)

messages = ["Hello!", "What's up?", "Good luck today!"]
sent_messages = []

send_messages(messages, sent_messages)

print("Original messages:", messages)
print("Sent messages:", sent_messages)


# -------------------------------
# 8-11. Archived Messages
# -------------------------------
def send_messages(messages, sent_messages):
    while messages:
        msg = messages.pop(0)
        print(f"Sending message: {msg}")
        sent_messages.append(msg)

messages = ["Let's go!", "See you!", "Take care!"]
sent_messages = []

send_messages(messages[:], sent_messages)  # use copy

print("Original messages:", messages)
print("Sent messages:", sent_messages)


# -------------------------------
# 8-12. Sandwiches
# -------------------------------
def make_sandwich(*items):
    print("\nMaking a sandwich with:")
    for item in items:
        print(f"- {item}")

make_sandwich("turkey", "cheese")
make_sandwich("turkey", "lettuce", "tomato")
make_sandwich("bacon", "egg", "cheese", "avocado")


# -------------------------------
# 8-13. User Profile
# -------------------------------
def build_profile(first, last, **info):
    info["first_name"] = first
    info["last_name"] = last
    return info

user_profile = build_profile(
    "Sameer", "German",
    college="Albright College",
    sport="Baseball",
    hometown="Delaware"
)

print(user_profile)


# -------------------------------
# 8-14. Cars
# -------------------------------
def make_car(manufacturer, model, **details):
    details["manufacturer"] = manufacturer
    details["model"] = model
    return details

car = make_car("Chevorlet", "Camaro", color="Grey", tow_package=True)
print(car)


# -------------------------------
# 8-15. Printing Models
# -------------------------------
# File: printing_functions.py
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)


# File: printing_models.py
from printing_functions import print_models, show_completed_models

unprinted_designs = ["phone case", "keys", "cube"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# -------------------------------
# 8-16. Imports
# -------------------------------
# module: greet_module.py
def greet_user():
    print("Hello from the greet module!")


# main program
import greet_module
from greet_module import greet_user
from greet_module import greet_user as gu
import greet_module as gm
from greet_module import *

greet_module.greet_user()
greet_user()
gu()
gm.greet_user()
greet_user()


# -------------------------------
# 8-17. Styling Functions
# (Check that all functions follow PEP 8 — they do!)
# -------------------------------
print("\nAll functions are styled properly following PEP 8 conventions.")
