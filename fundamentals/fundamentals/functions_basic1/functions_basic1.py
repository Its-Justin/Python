#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) # will print 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) # this will print an error because only one function was defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) #it will return 5 because once the fist return is run it ends the function 

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers()) #it will return 5 because once the fist return is run it ends the function therefore the 10 will not print 

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x) # it will print 5 and nothing because x was never defined 

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3)) #it will print an error because the function never added the variables

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5)) # it will return 25 because the numbers were identified as a string and put then together

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents()) #it will print 100 and 10 

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # will print 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #will print 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # will print 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5)) # will print 8

#11
b = 500
print(b) # will print 500
def foobar():
    b = 300
    print(b)
print(b) #will print 500
foobar() #will print 300
print(b) #will print 500

#12
b = 500
print(b) #will print 500
def foobar():
    b = 300
    print(b)
    return b
print(b) #will print 500
foobar() #will print 300
print(b) #will print 500 because the variable was never changed

#13
b = 500
print(b) #will print 500
def foobar():
    b = 300
    print(b)
    return b
print(b) #will print 500
b=foobar() #will print 300 and set the variable b=300
print(b) #will print 300

#14
def foo():
    print(1) #will print 1
    bar() #will print 3
    print(2) #will print 2
def bar():
    print(3)
foo()

#15
def foo():
    print(1) #will print 1
    x = bar() #will print 3 and return 5. x=5
    print(x) #will print 5
    return 10
def bar():
    print(3)
    return 5
y = foo() # y=10
print(y) #will print 10

