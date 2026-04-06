# function to calculate the sphere volume
import string
def volume_of_sphere(radius):
    pi = 3.14159
    volume = (4/3) * pi * radius ** 3
    return volume
print(volume_of_sphere(5))

# function to calculate the area of a circle
def area_of_circle(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area
print(area_of_circle(5))

# function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    area = length * width
    return area
print(area_of_rectangle(5, 3))
# function that counts the number of words in a string
def count_words(string):
    words = string.split()
    return len(words)
print(count_words("Hello world! This is a test and my name is Adam."))
