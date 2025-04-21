string_input=input("please Enter the string:")
count=0
for i in string_input:
    if i in "aeiouAEIOU":
        count+=1
        
#     print("The given string is not a vowel")
print(count);