"""
when we create a variable inside a function, it is local by default
when we define a variable outside of a function, it is global by default
we use global keyword to read and write a global var inside a function


"""

x = "awesome"


def my_func():
    print("Python is " + x)


# if you create a variable with the same name inside a function => will be local, use only inside that function
# the global variable with the same name will remain as it was - global and with the original value


"""
to create a global variable inside a function, you can use global keyword

if you want to change the value of global variable, you can use global keyword
"""

x = "awesome"


def my_func_2():
    global x
    x = "fantastic"


my_func_2()
