# check the person can vote or not 
number = 0
if number >18 :
   print ("he can vote")
else :
   print("he didnot vote")
print("******************")
# check can we add multiple statment in if and can we write if with out else 
x= 1;
total = 20
if x!=0 and x>=0 :  # we can write the conditinal statment without else 
   total= total+x
   print(total)
print("*******************")

# Nested if or if else and else if 
# check weather number is negetive or postive or an zero 
if number > 0:
   print("The Number is positive")
elif number < 0 :
   print(" The number is negetive")
else :
   print("The number is Zero")
print("*************************")

# nested if with if and else 
age = 30

if age >= 18:
    print("You are an adult.")
    if age >= 60:
        print("You are a senior citizen.")
    else:
        print("You are not a senior citizen.")
else:
    print("You are a minor.")
print("********************************")
# Operators use case  and or 
# Check wheather the number is with in the range or not 
if number >20 and number <10 :
   print("The number is with in the range of 10 and 20")
else :
   print ("The number is not with in the range")

print("*********************************")
# Terinery Operators  which we can add all the if else logic in single line  
no=10
result ="Even" if no % 2 ==0 else "odd"
print (result);
print("***********************")
# Terinary Operators with  dict
num1 =10
num2 =20
maximum ={True:num1,False:num2}[num1>num2]
print(maximum)
print("**********************")

# Terinary Operators with Tuple
num3=7
result=("odd","even")[num3 %2 ==0] # it will take first Nearest value 
print(result)
