Myword="RADADAR"
is_Palindrome =  True

for char in range(len(Myword)//2): # Only check half of the string
    if Myword[char] != Myword[-(char+1)]:  # Compare front and back characters
        is_Palindrome = False 
        break          
    else:
        is_Palindrome = True
if is_Palindrome:     
    print("The given word is Palindrome")
else:
    print("The given word is not Palindrome")

# Key Observations  
# char = 0 → Myword[0] = 'R', Myword[-1] = 'R' ✅ Match
# char = 1 → Myword[1] = 'A', Myword[-2] = 'A' ✅ Match
# char = 2 → Myword[2] = 'D', Myword[-3] = 'D' ✅ Match

s1="chandhu"
s2="sekhar"
print(s1+s2)
str = "Python is very easy to learn and easy to adapt"
count=0
index=0
for char in str:
    if char=='a':
        count=count+1
    elif str.find("learn")!=-1:
        index=str.find("learn")
        
print("The count of a in the given string is:",count)
print("The index of learn in the given string is:",index)