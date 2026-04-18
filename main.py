
# function to calculate the sphere volume
import string
def volume_of_sphere(radius):
    pi = 3.14159
    volume = (4/3) * pi * radius ** 3
    return volume
print(volume_of_sphere(9))

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


fruit = "banana"
if 'n' in fruit:
    print('found it')


greet= "hello WORLD"
zap= greet.upper()
print(zap)

greet="hello world"
nstr=greet.replace("world","adan")
print(nstr)


xfile= open('MONGODB adammoha0987 db.txt')
count=0
for line in xfile:
    count= count +1
    print('line count: ',count)

xfile= open('MONGODB adammoha0987 db.txt')
inp= xfile.read()
print(len(inp))
print(inp[:20])

xfile=open('MONGODB adammoha0987 db.txt')
for line in xfile:
    if line.startswith("adam"):
        print(line)
        
xfile=open('MONGODB adammoha0987 db.txt')
for line in xfile:
    line=line.lstrip()
    if not line.startswith("adam"):
        continue
    print(line)


fname= input("enter the file name:")
fhand=open (fname)
count=0
for line in fhand:
    if line.startswith("m"):
        count= count + 1
print("there were", count, "m line in", fname)
