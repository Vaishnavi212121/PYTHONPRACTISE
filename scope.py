# 1. Demonstrate a local variable.
def local_example():
    local_var = "I am a local variable"
    print(local_var)

local_example()


# 2. Demonstrate a global variable.
global_var = "I am a global variable"

print(global_var)


# 3. Access a global variable inside a function.
global_var = "I am a global variable"

def access_global():
    print(global_var)

access_global()


# 4. Modify a global variable using global.
def modify_global():
    global global_var
    global_var = "I have been modified"

modify_global()

print(global_var)


# 5. Demonstrate nested function scope.
def outer_function():
    outer_var = "I am from the outer function"

    def inner_function():
        inner_var = "I am from the inner function"

        print(outer_var)  # Accessing outer function's variable
        print(inner_var)  # Accessing inner function's variable

    inner_function()

outer_function()


# 6. Use nonlocal with nested functions.
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()

    print(x)


outer()