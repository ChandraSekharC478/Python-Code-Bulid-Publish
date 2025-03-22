# if we do the same task in muntliple times we can use loops
# For Loops 
languages =['Java','Js','Python','C','C++','Rubby','Node Js']
for a in languages :
    print(a)
print("*************************************************")
# we can  print single value as well
hobby ='PlayingCircket '
for b in hobby:
    print(b)
print("*************************************************")
# Range function in for loop
for i in range(1,10):
    print(i);
print("*************************************")
# Loop with conditional Statments
for i in range(1,10):
    if i % 2 == 0:
        print(f'{i} is even')
        print("********")
    else :
        print(f'{i} is odd')
        print("********")
print("************************************")

# lets print odd and even in single line 
Even=[] # empty  even list 
Odd=[] # empty odd list
for i in range (1,20):
    if i%2 ==0 :
        Even.append(i)
    else :
        Odd.append(i)
print("Even number is:",Even);
print("Odd number is:",Odd);
print("************************")
#### Break and Continue statements

for a in languages :
    if (a=='Js'):
        break  # if the conditions is Macthed it will break the loop and doesnt Execute anything after this
    print(a)
###### Continue - it will skip the conditioanl staments it will run next 

for a in languages :
    if(a=="C++"):
        continue
    print( "continue statment:",a)