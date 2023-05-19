given_array=[4,2,2,8,3,3,1]
max=0
for i in given_array:
    if i>max:
        max=i
count_array=[]
for i in range(max+1):
    count_array.append(0)

output_array=[]
for i in range(len(given_array)):
    output_array.append(0)


for i in given_array:
    count=0
    for j in given_array:
        if i==j:
            count+=1
    count_array[i]=count
sum=0
for i in range(max+1):
    sum+=count_array[i]
    count_array[i]=sum
print("count array-->",end=" ")
print(count_array)
for i in given_array:
    count_array[i]=count_array[i]-1
    output_array[count_array[i]]=i
print("sorted array-->",end=" ")
print(output_array)
