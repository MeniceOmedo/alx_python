def update_dictionary(a_dictionary,key,value):
    if key in a_dictionary:
         a_dictionary.update({key:value})
    else:
         a_dictionary[key]=value
    return a_dictionary
    
a_dictionary={'language':"C",
              'number':89,
              'track':"Lowlevel"
}
new_dict=update_dictionary(a_dictionary,"language","Python")
print(new_dict)

def print_sorted_dictionary(my_dict):
        keys=sorted(my_dict.keys())
        for k in keys:
            print("{}: {}".format(k,my_dict[k]))
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
print("--")
print("--")

new_dict=update_dictionary(a_dictionary,'City',"San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)