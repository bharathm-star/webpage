test_list = [1, 4, 5, 8, 10]
list1 = [10, 8, 5, 4, 1]

flag = 1
i = 0
j = -1
while i < len(test_list):
   if(test_list[j] == list1[i]):
       flag = 1
       j = j + (-1)
       i += 1
   else:
        flag = 0
        break
     
if (not flag) :
    print ("Not exact reverse.")
else :
    print ("Yes exact reverse.")

# Check if list is sorted in ascending order not

test_list = [1, 4, 5, 8, 10]
# printing original list
print ("Original list : " + str(test_list))
flag = 0
i = 1
while i < len(test_list):
    if(test_list[i] < test_list[i - 1]):
        flag = 1
    i += 1
     
# printing result
if (not flag) :
    print ("Yes, List is sorted.")
else :
    print ("No, List is not sorted.")
