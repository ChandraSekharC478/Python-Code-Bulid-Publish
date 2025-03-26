number=1
total=0
while total<=10:
    total=total+number #total=0+1=1, total=1+2=3, total=3+3=6, total=6+4=10, total=10+5=15
    number=number+1
print("The total amount if the total is less than equal to 10:",total)
print("*******************************************************************")
number=1
total=0
while number<=10:
    total=total+number #total=0+1=1 , total=1+2=3 ,total=3+3=6 ,total=6+4=10 ,total=10+5=15,total=15+6=21,number=21+7=28....total=45+9=55
    number=number+1         #number=1+1=2, number=2+1=3, number=3+1=4, number=4+1=5,number=5+1=6, num=6+1=7........ number=9+1=10
print("The total amount if the number is less than equal to 10:",total)

print("*******************************************************************")

# Remove the Vowles in the word and print the consonants only by given the String 
word = "Learnbay" 
vowels = "aeiouAEIOU"  # Define vowels
result = ""

for char in word:
    if char=='i' or char=='a' or char=='u' or char=='e' or char=='o':
        continue# If the character is not a vowel
    result = result+ char  

print("Consonants only:", result)
print("*******************************************************************")

# Remove the Vowles in the word and print the consonants only by given the String
word = "Chandra is an python coder and Devops Engineer"
vowels = "aeiouAEIOU"  # Define vowels
result=""
for char in word:
    if char  in vowels:
     continue
    result=result+char
print("Consonants only with inbuilt Function:",result)

print("*******************************************************************")

# Remove the Vowles in the word and print the consonants only by given the String
result=""
index=0;
while index<len(word):
    if word[index] not in vowels:
        result=result+word[index]
    index=index+1
print("Consonants only with while loop:",result)

# febnocci Numbers 
print("*******************************************************************")
a=0
b=1
n=100
while a<n:
    print(a,end=' ')
    a,b=b,a+b

# Key Observations
# The first two numbers are 0 and 1.

# Each number is the sum of the previous two numbers.

# The values of a and b keep shifting (like a sliding window).

# The loop stops after 10 iterations.


