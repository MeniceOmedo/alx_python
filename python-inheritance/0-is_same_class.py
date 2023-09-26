def is_same_class(obj,a_class):
    """This fuction is to test whether an object
    is an instance of a given class
    Args:
        obj(object): The first parameter.
        a_class(class): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.

    """
    if isinstance(obj,a_class):
        return True
    else:
        return False
    
a=1
if is_same_class(a,int):
    print("{} is an instance of the class {}".format(a,int.__name__))
if is_same_class(a,float):
    print("{} is an instance of the class {}".format(a,float.__name__))

if is_same_class(a,object):
    print("{} is an instance of the class {}".format(a,object.__name__))

