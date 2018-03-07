# !/usr/bin/env python3
# Program name:          car_wrapper.py
# Author(s):                 Zack Steck
#Date:                          03/05/2018

''' Works with car_builder, will handle both painting and wrapping a car '''

import time
from PIL import Image

def start():
    print("This program only works with cars taht already exist. It cannot create new cars for you. ")
    print("If you do not already have a car, please use 'car_builder' to create one and then come back. ")
    getCar()

def stockPicGenerator(car_name, car_model):
    car_file_name = car_name + ".png"
    car_file_model = car_model + ".png"

    try:
        car_image = Image.open(car_file_name)
    except FileNotFoundError:
        print("No picture with that car's name are found.")
        create_stock = input("Do you want to create a stock image of the car to use? [y/N] ")
        if create_stock.lower() == "y":
            try:
                car_image = Image.open(car_file_model)
            except FileNotFoundError:
                print("No picture's of that car model are found. The model might not be in the game yet.")
                print("Sorry, but there is nothing this program can do for you. ")
                time.sleep(2)
                print("Goodbye.")
                time.sleep(3)
                exit()
        else:
            print("Okay. There is nothing this program can do for you. ")
            time.sleep(2)
            print("Goodbye.")
            time.sleep(3)
            exit()

    rgb_car_image = car_image.convert("RGB")

    #r, g, b = rgb_car_image.getpixel((100, 100))

    #print(r, g, b)

    pixeldata = car_image.load()

    #car_image.show()

    print("Perparing the car for paint/wrap", end="")
    for i in range(5):
        time.sleep(0.5)
        print(".", end="")
    print("")
    print("Done!")
    
    
    for x in range(car_image.size[0]):
        for y in range(car_image.size[1]):
            r, g, b = rgb_car_image.getpixel((x, y))
            if r == 10 and g == 35 and b == 118:
                pixeldata[x, y] = (0, 100, 0, 255)
            elif r == 5 and g == 20 and b == 71:
                pixeldata[x, y] = (0, 100, 0, 255)
            elif r == 10 and g == 35 and b == 118:
                pixeldata[x, y] = (0, 100, 0, 255)
            elif r > 6 and r < 100:
                if g > 21 and g < 125:
                    if b > 71 and b < 232:
                        pixeldata[x, y] = (0, 255, 0, 255)
                

    car_image.save(car_file_name)

    #car_image.show()

def getCar():
    car_model = input("What model car do you want to work on? ")
    car_name = input("What's the name of the car you want to work on? ")

    colors = ["red", "yellow", "blue"]

    #car_file = open(car_name, "r")

    modded = input("Does your car have any visual mods? [y/N] ")
    if "y" in modded.lower():
        modded = True
    else:
        modded = False

    print("Getting the image of the car", end="")
    for i in range(5):
        time.sleep(0.5)
        print(".", end="")
    print("")
    print("Done! ")
    stockPicGenerator(car_name, car_model)
    
    if modded:
        print("Applying visual mods to the car", end="")
        for i in range(5):
            time.sleep(0.5)
            print(".", end="")
        print("")
        print("Done! ")

    paint_or_wrap = input("Do you want to [P]aint or [w]rap the car? ")
    if paint_or_wrap.lower() == "w":
        print("wrap")
    else:
        print("paint")
        color = input("What color would you like to paint the car? Type 'list' to view all of the colors. ")
        while color:
            if color.lower() == "list":
                print("There's several colors to choose from, and more added with each update.")
                print("Right now, you can choose from this list: ")
                print(colors[0], end="")
                for i in range(len(colors) - 1):
                    print(", ", end = "")
                    print(colors[i + 1], end= "")
                print("")
            else:
                print("Painting the car", end="")
                paintCar(car_name, color)
                for i in range(5):
                    time.sleep(0.5)
                    print(".", end="")
                print("")
                print("Done! ")
                break
                
            color = input("What color would you like to paint the car? Type 'list' to view all of the colors. ")
        
    
def paintCar(car_name, color):
    car_file_name = car_name + ".png"

    car_image = Image.open(car_file_name)
    rgb_car_image = car_image.convert("RGB")
    pixeldata = car_image.load()

    for x in range(car_image.size[0]):
        for y in range(car_image.size[1]):
            r, g, b = rgb_car_image.getpixel((x, y))

            if g == 255:
                if color == "red":
                    pixeldata[x, y] = (255, 0, 0)
                elif color == "blue":
                    pixeldata[x, y] = (0, 0, 255)
                elif color == "yellow":
                    pixeldata[x, y] = (255, 255, 0)
            elif g == 100:
                if color == "red":
                    pixeldata[x, y] = (100, 0, 0)
                elif color == "blue":
                    pixeldata[x, y] = (0, 0, 100)
                elif color == "yellow":
                    pixeldata[x, y] = (100, 100, 0)

    file_path = "/home/zsteck/Desktop/car_builder/finished_cars/"

    if color == "red":
        car_new_name = file_path + "red_" + car_file_name
    elif color == "blue":
        car_new_name = file_path + "blue_" + car_file_name
    elif color == "yellow":
        car_new_name = file_path + "yellow_" + car_file_name
        
    #car_image.show()
    car_image.save(car_new_name)
    
def wrapCar():
    #temp
    print("", end="")
    
def showCar():
    #temp
    print("", end="")
