import random
number= random.randint(-10000,10000)
number=int(number)
last_digit=(abs(number))%10
if number<0:
     last_digit=last_digit*-1
     print=("last digit of {} is {} and is less than 0".format(number,last_digit))
elif number>0:     

    if last_digit>5:
         print("last digit of {} is {} and is greater than 5".format(number,last_digit))
    elif last_digit==0:
        print("last digit of {} is {} and is 0".format(number,last_digit))
    elif( last_digit<6) and   (last_digit!=0) :
        print("last digit of {} is {} and is less than 6 and not 0".format(number,last_digit)) 
    #elif(int((number<0))):
       #last_digit=(last_digit)*-1
       #print("last digit of {} is {} and is less than 0".format(number,last_digit))        

else:
         print("in else block")

