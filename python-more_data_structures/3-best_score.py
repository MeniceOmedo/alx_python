def best_score(a_dictionary):
    if a_dictionary==None:
        return None
    else:
        biggest_value=a_dictionary["John"]
        for key,value in a_dictionary.items():
            if a_dictionary[key]>biggest_value:
                biggest_value=value
        #k=a_dictionary[biggest_value]   
        for key,value in a_dictionary.items() :
            if value==biggest_value:
                return key    
        
a_dictionary={'John':12,
              'Bob':14,
              'Mike':14,
              'Molly':16,
              'Adam':10
}
best_key=best_score(a_dictionary)
print('Best score: {}'.format(best_key))


best_key=best_score(None)
print('Best score: {}'.format(best_key))
