#Write a Python program that asks for the baggage weight and let the user know
#while it's weight exceeds the baggage limit of 15kg
#Each time it is checked, the user should be asked how much it is weight they have removed from the bag
#and the weight is updated.

val = float(input("Enter baggage weight: "))
limit = 15

while val > limit:
    print("Baggage exceeds the 15kg limit.")
    removed = float(input("Enter weight removed: "))
    val -= removed
    print("Updated weight:", val)