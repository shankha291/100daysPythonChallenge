#function with return_type
def fun(name):
    return name.title() #for title case capitalizing
string1=fun("shan")
print(string1)
#multiple return values
def fun2(fname,lname):
    """
    Returns the capitalized title case form of the name
    """
    if fname=="" or lname=="":
        return "Use valid input please"
    formated_fname=fname.title()
    formatted_lname=lname.title()
    return f"Result:{formated_fname} {formatted_lname}"
print(fun2("raHul","dAs"))
#docstrings-->>You can use it for multi-line comments.Also for a method it helps for documentation of the function
"""
hello
i am a docstring

"""
