def no_c(my_string):
    new_list=list( my_string)
    while "c" in new_list:
        new_list.remove("c")
    while "C" in new_list:
        new_list.remove("C")   
        
    separator=""
    new_string=separator.join(new_list)
    return new_string

print(no_c("Holberton School"))
print(no_c("chicago"))
print(no_c("C is fun!"))