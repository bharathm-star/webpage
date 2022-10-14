def if_odd(num):
    if(num==0):
         print("nil")
    else:
        for iterl in range(1,num):
             num=num*iterl 
             iterl+=1
    return num

def if_even(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        print("the given number is pallindrome")
    else:
        print("the given number is not pallindrome")


num=int(input ("enter a number :"))
if(num%2==0):
    if_even(num)
else:
    output=if_odd(num)
    print("the factorial of a given number in :",output)
    digt=0
    while(output>0):
        output//=10
        digt+=1
    print("the no of digits is :",digt)
