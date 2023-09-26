def inherits_from(obj,a_class):
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
    
a=True
if inherits_from(a,int):
    print("{} inherited from class {}".format(a,int.__name__))
if inherits_from(a,bool):
    print("{} inherited from class {}".format(a,bool.__name__))

if inherits_from(a,object):
    print("{} inherited from class {}".format(a,object.__name__))
