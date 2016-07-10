# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 


def cost_with_tax(cost, state, tax=0.05):
    """This function calculates an item cost by adding tax.

    The function's default tax amount is 5%; however, the function also accepts
    a state abbreviation. If that state is California (CA), the tax is set to 7%.
    The arguments for this function: (cost, state, tax=0.05)"""

    if state == 'ca':
        tax = 0.07
        total = (cost * tax) + cost
        return "The total cost of the item, including tax, is $%0.02f" %total
    else:
        total = (cost * tax) + cost
        return "The total cost of the item, including tax, is $%0.02f" %total




#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

def is_berry(fruit):
    """This function checks to see if the input is a berry.

    Specifically, this function checks to see whether the argument (fruit) is
    a strawberry, cherry, or blackberry."""

    berries = ["strawberry", "cherry", "blackberry"]
    if isinstance(fruit,str) == False:
        return "Please use a string argument."
    elif fruit.lower() in berries:
        return True
    elif fruit.lower() not in berries:
        return False
    else:
        return "Please use quotes to make your argument a string."

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def shipping_cost(fruit):
    """Calculates the shipping cost based on the fruit argument.

    This function calculates shipping cost by taking a fruit name as a string, 
    calling the is_berry() function within and returns 0 if is_berry() == 
    True, and 5 if is_berry() == False."""

    if is_berry(fruit) == True:
        return 0
    elif is_berry(fruit) == False:
        return 5
    else: 
        return "Please use quotes to make your argument a string"


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.

def is_hometown(town):
    """Tests whether the argument is Jess' hometown of Rockford, IL.

    Specifically, this function takes a town name as a string and evaluates to 
    `True` if it is Jessica Petersen's hometown, and `False` otherwise."""

    if isinstance(town, str) == False:
        return "Please use a string argument."
    elif town.lower() == "rockford":
        return True
    else:
        return False
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.

def full_name(first, last):
    """Takes a first and last name and creates a full name. 

    Specifically, this function takes a first and last name as arguments as 
    strings (first, last) and returns the concatenation of the two names in one 
    string."""

    full = first[0].capitalize() + first[1:] + " " + last[0].capitalize() + last[1:]
    return full
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def hometown_greeting(town, first, last):
    """Provides unique greeting to user based on hometown.

    Specifically, this function takes a home town, a first name, and a last name 
    as strings as arguments, calls both `is_hometown()` and `full_name()` and 
    prints "Hi, 'full name here', we're from the same place!", or "Hi 'full name 
    here', where are you from?" depending on what `is_hometown()` evaluates to""" 
    if is_hometown(town) == True:
        full = full_name(first, last)
        print "Hi, %s, we're grom the same place!" %full
    elif is_hometown(town) == False:
        full = full_name(first, last)
        print "Hi, %s, where are you from?" %full

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def add(y, x):
    """This function adds two arguments (y, x) together and returns the sum."""
    z = x + y
    return z

def increment(y, x = 1):
    """This function takes two int arguments and calls the add function to add them.

    Specifically, this `increment()` function has a nested inner function, `add()`
    inside of it. The outer function takes ``x``, an integer which defaults to 1
    as well as y. The inner function "add(y,x) " takes ``y`` and add ``x`` and ``y`` 
    together."""
    y = int(y)
    return add(y, x)

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20. 

def addfive(y):
    """This function adds five to the argument given.

    Specifically, this function takes one argument (y) and provides that argument to 
    the nested function increment(y, 5), which will add 5 to any argument integer (y)."""
    return increment(y, 5)

addfive(5)
addfive(20)

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def add_num_to_list(num, list):
    """Takes a number and adds it to the end of a given list.

    This function takes in a number and a list of numbers (num, list). It append 
    the number to the list of numbers and return the list"""

    list.append(num)
    return list


#####################################################################