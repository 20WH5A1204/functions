# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(13, 5)


####
def update(x):
     x = 8
     print("X", x)

a = 10
update(a)
print("a", a)

####

def update(lst):
    print(id(lst))


    lst[1]=25
    print(id(lst))
    print("x",lst)


lst = [10,20,30]
print(id(lst))
update(lst)
print(lst)
