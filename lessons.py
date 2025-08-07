x = 3;y= 21
sum = x + y
print("the sum is",sum)
x=3;y=4;print(x+y)
fruits=["orange",
        "mango",
        "banana"]
print(fruits)
if 5>6:
    x="hello world!"
    print(x)
name="killer ntua"
name="offei"
print("hello" + name)
my_favorite_food="rice"
print(my_favorite_food)
bool=True
print(bool)
bool=False
print(bool)
print(10>5)
print(6>3)
print(4<2)
print(5==5)
print(5==6)
# an integer is a kind of data type in python
# floating numbers are decimals
# strings are text
# a string must be surronded by a single or double quotes
fruit="mango"
print(fruit)
# use single quotes when ur string contains double quotes
# use double quotes when ur string contains single quote
x="I told u 'python is fun'"
print(x)
z="Let's learn pythom!"
print(z)
# a boolean value is a true or false value
# a list is an ordered collection of data
# it can contain a string,numbers,etc
# it is represented by []
MyList=["money","happy","life"]
print(MyList)
a= 3j
b= 4.21j
c= 5.33j

print(a)
print(b)
print(c)
a="school"
b=21
c=5<4
d=5.21
e=4.21j
f=5.33j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
x=4/2
print(x)
print(type(x))
# the round function is used to round floating points to specific decimal places
# round(digit,ndigits)-synthax
pi= 3.1415926535897
TwoDecimals=round(pi,2)
print(TwoDecimals)
# THE POWER FUNCTION pow() is used to raise a number to a specific power
# synthax pow(base,exponent)
s=pow(4,2)
print(s)
# the abs() function returns the absolute value of a number
a=abs(-45)
print(a)
# the divmod() function takes a numerator and a denominator and returns two numbers which are the quotients and the remainder
c=divmod(5,2)
print(c)
print(type(c))
# to write a multiple string surround the string with single or dounble quotes thriple times
speech='''kwadwo is a boy,
kwadwo goes to school
kwadwo is a good boy'''
print(speech)
# concatenating strins simply means combining strings together
a="great"
b="world"
text= a+b
print(text)
# to escape a character in a string a backlash is placed right before the character
text='let\'s learn python'
print(text)
# You can access part of a string by using the indexing method
a=("I AM RICH")
print(text[0])
print(text[1])
print(text[2])
# slicing is also used to access parts of a string it also makes use of a square bracket with two integers seperated by a colon 
# with the first int being the starting point of the splicing and the second the end point
text="python lover" 
print(text[2:5])
# when splicing the end index is not included
text="uranus"
print(text[2:])
# the capitalize() function capatalizes the first letter of a text
text="kwame is great"
print(text.capitalize())
print(text.upper())
# the upper()turns all the elements in the string to capital and viceversa for the lower()
print(text.lower())
print(len(text))
# the len() function shows the length of a string
print(text.replace("is","was"))
text="gr gr gr"
print(text.replace("gr","by",2))
print("gr"in text)
print("gr"not in text)
# the above are self explanatory
x=4
print("my favorite nuber is"+str(x))
# the str() function is used to change integers into strings when combining an integer to a string
y=4.999
print(int(y))
# The int() function converts any data type to an integer
x=25
print(float(x))
# the float() function converts other data type to floats
# boolean dATA types are true or false data types
a=True
b=False
print(a)
print(b)
# the first lettter of a boolean later is capaital
age=19

if age>18:
 print("you are allowed to enter.")
 print(type(a))
 # operators are symbols that peprform operations on operands
 # the % operation in python is the remainder or modulo operation in python
 # // operation means floor division in -
 a=6/5
 print(a)
 b=4**2
 print(b)
 b=5//2
 print(b)
 # operator sequence shows the other eith which arithmetric operations are carried out
 j=10+3*5
 print(j)
 # java script uses MDAS wHICH IS multiplication,division,addition and subtraction
 # python assignment operators are used to assign values to variables
 x="hello";y="world"
 x+=y
 print(x)
 x="python" == "python"
 print(x)
 x="python"!="python"
 print(x)
 # the inequality operator compares two values and brings out true if their not the same and false if their the same
 # the equality == does the exact opposite of the inequality
 x=5%2
 print(x)
 y="kweku"!="kwame"
 print(y)
 u=(3+10)*5
 print(u)
 # you can group terms in a bracket to suit your order in which u want the operands to work
 x=6
 x+=3
 print(x)
 f="hello"
 f+="kwame"
 print(f)
 # the operator 'and' is like the end logic gate
 maths=(300==300)and(400!=699)
 print(maths)
 # the "or" operator is also just like the or logic gate
 food="fufu waakye jollof fried rice friedrice"
 print("friedrice" in food)
 # the in checks if an object of a string exists
 print("tz"not in food)
 # the not in operator returns true if the element before it does not exist
 x=" kofi is a boy"
 y=34
 print(x,y)
 fruit=["kweku","kofi","yaw","Ama"]
 print(fruit)
 # a list can contain mixed data types and is made up of square bracket with the objects seperated by brackets
 # an example of indexing
 print(fruit[0])
 print(fruit[1])
 print(fruit[2])
 # negative indexing can also be used where -1 means the last term and follow let's try one
 print(fruit[-1])
 print(fruit[-2])
 # a list can contain mixed data
 print(fruit[0:2])
 # this is interpreted as print from the object indexed 0 to the object indexed 3 
 # the end part of the range is not included
 # if u dont specify the range starts ffrom index zero same applies to the lst range and includes it
 print(fruit.append("okanta"))
 pets=["dog","cat"]
 pets.append("rabbit")
 print(pets)
 pets.insert(0, "rabbit")
 pets.insert(1, "hen")
 print(pets)
 # the pop item is the exact opposite of the append
pets.remove("rabbit")
print(pets)
del pets[2]
print(pets)
print(len(pets))
# the len method is used to get th number of items in the list
pets[2]="fish"
print(pets)
num1=[1,2,3,4]
num2=[5,6,7,8]
num1.extend(num2)
print(num1)
for pet in pets:
   print(pet)
names=list((34,5,6,7))
# this method of making a list is called the contractor method
# a tuple is created by using round brackets
cars=("bmw","toyota","benz","honda")
print(cars[0:2])
# the end part of the rande is not included
# in combining tuples we use addition operators instead of the extend method in lists
# tuples are unchangeable
h={"kweku",78,True}
print(h)
for h in h:
    print(h)
    # the add method is used to add one item to the set
pets={"june",67,True}
pets.add("loki")
print(pets)# the items of a set cannot be changed
# to remove something u can use the remove metrhod and discard method
y={1,2,3,4}
x={3,4,5,6}
x.update(y)
print(x)
print("x-y",x-y)
print("y-x",y-x)
# dictionaries contains the key value pair and starts with curly brackets
dictionary={
   "name":"kwame",
   "age":17,
   "height":"174cm"
}
dictionary["school"]="KNUST"
x=dictionary["name"]
y=dictionary["height"]
z=dictionary["age"]
print(x)
print(y)
print(z)
print(dictionary.get('height'))
print(dictionary.get("school"))
dictionary.pop("age")
#del is also used ti remove.
# to chang e an items value it is done by using the same key name and chsnging the value by using the a ssignment operator
# to access an item we specify the key name in square brackets
# the get method is also uded to access items in a dictionary
# the len method is also used to get the length of the items in the dictionary
students={
   "name":"bobby",
   "class":"five",
   "age":10
}
for key in students:
   print(students[key])
if "height" in students:
   print("height is in the dictionary")
else:
   print("heigt cannot be foung in the dictionary")
   # functions are group of words that performs a specific function
def my_func():
   x="hello world!"
   print(x)

my_func()
# in a function we need the def keyword the function name and round brackets and a colon and a group of statements
def myHobby():
   hobby="python is love"
   print(hobby)

myHobby()# this calls the function for it to be executed
def add_nums(num1,num2):
   x=num1+num2
   return x
   print(x)

add_nums(4,3)# the num1 and 2 are the parameters and 4 and 3 are arguments
def hello(name="offei"):
   x="hello"+name
   print(x)

hello("john")
hello()
def myFunc(fruit1,fruit2,fruit3):
   print("I love",fruit1)
   print("I love",fruit2)
   print("I love",fruit3)

myFunc(fruit3="grapes",fruit2="orange",fruit1="bannana")# this is the keyword argument
def add_nums(num1,num2):
   sum=num1+num2
   return sum# the return statements stops the execution of a function
   print(x)

#add=nums(4,3)
#lambda functions
#add= lambda x,y:x+y
#print(add(10,5))
# lambda can have only one expression but plenty argument
#pytho if else statements
age=15
if age>15:
   print("user is old enough to enter")
else:
   print("user cannot enter")
# an if else statement can be converted to a short hand version
x=10
print("x is 10")if x==10 else print("x is not 10")
# the above is called a tenary operator
x="kweku is 10" if x==10 else {"kweku is not 10"}
print(x)
pets=["cats","dogs","hen"]
for i in pets:
   print(f"{i} is my favorite pet")

txt="kwame is a boy"
for x in txt:
   print(x)
for i in range(5):
   print("hello kwame")
animal =["tiger","cat","dog"]
sound=["roars","meows","barks"]
for x in animal:
   for y in sound:
      print("the"+ x + "" + y)
j=[1,2,3]
for j in j:
   print(j)
else:
   print("loop has ended")
i=1
while i<=5:
   print("hello world")
   i+=1 
else:
   print("loop has ended")

# the python break and continue ststement
names=["Zak","kwame","kweku","kwabena"]
for name in names:
   if name=="kweku":
      break
   print(name)
i=1
while i<=5:
   if 1==3:
      break
   print(i)
   i+=1
# the continue statement
cars=["bmw","lamborghini","bugatti","ferrari","kantanka"]
for car in cars:
   if cars=="bugatti":
      continue
   print(car)





