test_list=[1,4,5,8,10]
list1=[10,8,5,4,1]
flag=1
i=0
j=-1
while i<len(test_list):
    if(test_list[j]==list1[j]):
        flag=1
        j=j=+(-1)
        i+=1
    else:
        flag=0
        break
    if(not flag):
        print("not exact reverse")
    else:          
         print("yes exact reverse")
test_list=[1,4,5,8,10]
print("original list:"+str(test_list))
flag=0
i=1
while i<len(test_list):
    if(test_list[i]<test_list[i-1]):
     flag=0
i+=1
if(not flag):
       print("tes,it is sorted")
else:
        print("no,list is not sorted")

