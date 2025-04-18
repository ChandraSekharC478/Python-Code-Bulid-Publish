list=[10,10,10,20,20,30,40,50,60,70,80,90,100]
unique_list=[]
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print("Unique elements in the list are: ",unique_list)