#Python is fun to learn.
#All comments are done starting with a # 

#STRINGS

name = 'Justine'

#to print the string we use the print function

print(name)

#FUNCTIONS

def calcArea(radius):
    #area of a circle is Pi * r * r
    area = 3.142 * radius **2


#DICTIONARIES.
def listFriendsColors(dictionary):
    for key, val in dictionary.items():
        print(f"{key}'s favourite color is {val} ")

favouriteColors = {}

while True:
    name = input("Enter your friend's name : ")
    color = input("Enter your friend's favourite color : ")
    favouriteColors[name] = color

    another = input('Do you want to add another friend ? (y/n)')
    if another == 'y':
        continue
    else:
        break

listFriendsColors(favouriteColors)