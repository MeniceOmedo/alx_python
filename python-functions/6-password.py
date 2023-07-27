def validate_password(password):
    password_length=len(password)
    for i in password:

        if (password_length>8)  and (i.isdigit()) and (i.isupper()) and(i.islowwer()) and (i.isspace()):
            return True
    return False   
            
    """ if i.isdigit():
               return True
        if i.isspace():
                 return False
        elif (i.isupper()) and (i.islowwer()):
            return True
                        
        else:
            return False                
                            
        
            
    return False"""
print(validate_password("Password 123"))
print(validate_password("abc123"))                 
print(validate_password("Password 123"))    
print(validate_password("password123"))    
       

    
    
