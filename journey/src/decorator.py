import inspect

def strict(func):
    """ 
    Check the type for each parameter 
    This decorator will raise an exception if the type does not match what was expected
    """
    def wrapper(*args, **kwargs):
        functionDetails = inspect.getfullargspec(func)
        
        # Make sure that the parameter's are specified
        if len(args) > 1:
            raise Exception("When using the decorator '@strict', you must specify the parameter and argument when you call the function. Example: myFunction(x=5)")
        
        # Check the type for the functions parameters
        for parameter in functionDetails.args:
            try:
                functionType = func.__annotations__[parameter]
                functionValue = kwargs[parameter]
                if not isinstance(functionValue,functionType):
                    raise TypeError(f"The parameter '{parameter}' has to be of type {functionType}, the value given was of type {type(functionValue)}")
            except KeyError:
                pass

        # If the type check succeeds, execute the function and check return value if it exists
        returnVal = func(*args, **kwargs)

        if returnVal and "return" in func.__annotations__:
            functionType = func.__annotations__["return"]
            if not isinstance(returnVal,functionType):
                raise TypeError(f"The return value has to be of type {functionType}, the value returned was of type {type(returnVal)}")

        return returnVal

    return wrapper


# def multiply(*args,**kwargs):

#     # Check if we did not received arguments in the decorater
#     if not callable(args[0]):
#         def inner(func):
#             def wrapper(*wargs,**wkwargs):
#                 print(func.__annotations__)
#                 return func(*wargs,**wkwargs) * args[0]
#             return wrapper
#         return inner

#     # Check if we received arguments in the decorater
#     if callable(args[0]):
#         def wrapper(*wargs,**wkwargs):
#             return args[0](*wargs,**wkwargs) * 2
#         return wrapper
