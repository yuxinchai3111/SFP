name = input("What is your name? ")
import random
adjectives = ["Sneaky", "Caring", "Sly", "Fearless", "Rich", "Hungry"]
animals = ["Fish", "Axolotl", "Dragon", "Rabbit", "Bird", "Ladybug"]
print(name + ", your codename is: " + random.choice(adjectives) + " " + random.choice(animals))
print("Your lucky number is: " + random.randint(0,100))