print("enter the size of array : ")
n=int(input())
print("enter array value: ")
input_array=[]
for i in range(n):
    input_array.append(int(input()))
print("enter the non integer value")
k=int(input())

#create empty array to store the difference of array element and non iteger value
Condition_array=[]

temp=[]
for i in range(n):
    temp.append(2*input_array[i]-k)
    if temp[i]>=0:
          Condition_array.append(temp[i])
    #print(Condition_array)
    # craete c array to count the similar elemnt of array condition_array and array given array
c=[]
     
a_set=set(input_array)
b_set=set(Condition_array)
c=a_set.intersection(b_set)
if len(c)>0:
    #c.append(1)
    #print(c)
    print("The number of instances when condition  is True : ",len(c))
