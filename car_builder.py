# car_builder.py
# Zack Steck
# 02-21-2018

''' helps calculate how much your dream car will cost you '''

car = "sports car"

cars_ingame = ["350z"]



def basePrice():
    new_or_current = input("Do you want to modify an [e]xisting car or build a [N]ew one? ")
    
    if new_or_current.lower() == "e":
        car_name = input("What's the name of the car? ")
    else:
        car_choice = input("Which car do you want to build? ")
        if car_choice not in cars_ingame:
            suggestions = open("suggestions", "r")
            
            print("Sorry, that car isn't in the game yet.")
            suggest = input("Do you want to add it to the suggestion list? ")
            if suggest.lower() == "y":
                already_suggested = False
                for line in suggestions:
                    if car_choice in line:
                        already_suggested = True
                    else:
                        already_suggested = False
                if not already_suggested:
                    suggestions = open("suggestions", "a")
                    suggestions.write(car_choice + "\n")
                    print("Suggestion added. ")
                else:
                    print("Suggestion added. ")
        else:
            print(car_choice, "selected.")
            name = input("What would you like to name this car? ")
            print(name)
            pickMods()

def pickMods():
    mod_half = input("Do you want to mod [V]isuals or [p]erformance? ")
    if mod_half.lower() == "p":
        category_p = input("Which part of the car's performance would you like to modify? ")
    else:
        print("mod visuals here")



        
while 1 + 1 != 3:
    basePrice()
