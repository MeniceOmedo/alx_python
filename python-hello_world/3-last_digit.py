import random
number= random.randint(-10000,10000)
number=str(number)
last_digit=number[-1]
if( int(last_digit)>5):
    print("last digit of {} is {} and is greater than 5".format(number,last_digit))
elif(int( last_digit)==0):
    print("last digit of {} is {} and is 0".format(number,last_digit))
elif( (int(last_digit)<6) and   (int (last_digit)!=0)) :
    print("last digit of {} is {} and is less than 6 and not 0".format(number,last_digit)) 
else:
    print("in else block")

print()