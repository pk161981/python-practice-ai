 #Tuples
    #A tuple is a collection of items that are ordered and unchangeable.
    #Tuples are defined using parentheses () and can contain elements of different data types.
    #Tuples are Immutable whereas Lists are Mutable. 
    # This means that once a tuple is created, its elements cannot be changed, added, or removed. 
    # In contrast, lists can be modified after creation.
    #Create a tuple for RGB color values

purple_rgb = (128, 0, 128)
print("Purple RGB tuple is:", purple_rgb)

#Accessing elements in a tuple
red_value = purple_rgb[0]
green_value = purple_rgb[1]
blue_value = purple_rgb[2]
print(f"Red: {red_value}, Green: {green_value}, Blue: {blue_value}")

#try to change an element in the tuple (this will raise an error)
#purple_rgb[0] = 255 # This will raise a TypeError

#Unpacking a tuple means assigning the values of a tuple to individual variables 
# in a single statement.
#individual variables can then be used to access the values of the tuple elements.
r, g, b = purple_rgb
print(f"Red: {r}, Green: {g}, Blue: {b}")

#iterating through a tuple
for value in purple_rgb:
    print(value)

#I want to mix colors using tuples without function
red_rgb = (255, 0, 0)
green_rgb = (0, 255, 0)
blue_rgb = (0, 0, 255)

#Mixing colors by adding their RGB values
mixed_rgb = (red_rgb[0] + green_rgb[0], red_rgb[1] + green_rgb[1], red_rgb[2] + green_rgb[2])
print("Mixed RGB tuple is:", mixed_rgb)

yellow_rgb = (255, 255, 0)
print("Yellow RGB tuple is:", yellow_rgb)
#Mixing colors by averaging their RGB values. 
# //means integer division, which discards the decimal part of the result. 
# which is Floor Division - Ex: 7 // 2 = 3 , 191.5 = 191
mixed_rgb2 = ((purple_rgb[0] + yellow_rgb[0]) // 2, (purple_rgb[1] + yellow_rgb[1]) // 2, 
              (purple_rgb[2] + yellow_rgb[2]) // 2)
print("Mixed RGB tuple is:", mixed_rgb2)