# car_builder.py
# Zack Steck
# 02-21-2018

''' helps calculate how much your dream car will cost you '''

car = "sports car"

cars_ingame = ["sample"]

def createCar(car_model, car_name, p_mods, v_mods):

    newLine = lambda : car_file.write("\n")
    
    car_file = open(car_name, "w")
    model_string = "CAR MODEL = " + car_model + "\n"
    name_string = "CAR NAME = " + car_name + "\n"
    for i in range(30):
        car_file.write("#")
    newLine()
    car_file.write(model_string)
    car_file.write(name_string)
    for i in range(30):
        car_file.write("#")
    newLine()
    newLine()
    for i in range(30):
        car_file.write("#")
    newLine()
    car_file.write("VISUAL MODS")
    newLine()
    for i in range(30):
        car_file.write("-")
    newLine()
    newLine()
    for item in v_mods:
        car_file.write(item)
        newLine()
    newLine()
    for i in range(30):
        car_file.write("#")
    newLine()
    newLine()
    for i in range(30):
        car_file.write("#")
    newLine()
    car_file.write("PERFORMANCE MODS")
    newLine()
    for i in range(30):
        car_file.write("-")
    newLine()
    newLine()
    for item in p_mods:
        car_file.write(item)
        newLine()
    newLine()
    for i in range(30):
        car_file.write("#")
    newLine()

def basePrice():
    new_or_current = input("Do you want to modify an [e]xisting car or build a [N]ew one? ")

    performance_mods = []
    visual_mods = []
    
    if new_or_current.lower() == "e":
        car_name = input("What's the name of the car? ")
        try:
            car_name_file = open(car_name, "r")
        except FileNotFoundError:
            print("Sorry, this car doesn't exist yet. You can try again later or just create a new car. ")
            basePrice()
        else:
            for line in car_name_file:
                #print(line)
                if "MODEL" in line:
                    car_model = line[12:]
                elif "brakes" in line.lower():
                    performance_mods.append(line)
                elif "turbo" in line.lower():
                    performance_mods.append(line)
            pickMods(car_model, car_name, performance_mods, visual_mods)
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
            createCar(car_choice, name, [], [])
            pickMods(car_choice, name, [], [])

def pickMods(car_model, car_name, perf_mods, vis_mods):
    p_mods = []
    v_mods = []

    for item in perf_mods:
        p_mods.append(item)
    #print(p_mods)

    for item in vis_mods:
        v_mods.append(item)
    #print(v_mods)
        
    mod_half = input("Do you want to mod visuals or performance? ")
    if mod_half.lower() == "p":
        category_p = input("Which part of the car's performance would you like to modify? ")
        if category_p == "brakes" and "Brembo brakes" not in p_mods:
            print("Brakes have been upgraded!")
            p_mods.append("Brembo brakes")
            #print(p_mods)
            pickMods(car_model, car_name, p_mods, v_mods)
        elif category_p == "turbo" and "Turbocharged engine" not in p_mods:
            print("Turbocharged the engine!")
            p_mods.append("Turbocharged engine")
            #print(p_mods)
            pickMods(car_model, car_name, p_mods, v_mods)
        else:
            print("Sorry! That mod isn't in the game yet. ")
            pickMods(car_model, car_name, p_mods, v_mods)
    elif mod_half.lower() == "v":
        print("mod visuals here")
    else:
        createCar(car_model, car_name, p_mods, v_mods)
        print("Car file saved.")

basePrice()
