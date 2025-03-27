str = "Python is very easy to learn and easy to adapt"

# 1. indexing to find characters
print(str[10])
print(str[18])
print(str[-8])

#2. Slicing : extracting the small part of the parent string as output
print(str[2:21]) # 2= starting index / 21 = total length of the string

#3: Imuutability of the strings
#str[4] = 'Z'
#print(str)

#4: comparing the strings with each other
s1 = "Hello Python"
s2 = "Hello Python"
s3 = "We are into learning"
s4 = 3
s5 = "3"
print(s1 == s2)
print(s2 == s3)
print(s4 == s5)

#5: '+' operator = joining of the two or more strings
result = s1 + " " + s3
print(result)

#6: to find the length of the string
print(len(str))

#7: in / not in used inside ethe strings for chracters and words both
print('z' not in str)
print('very' in str)

#8: find() is used to find the substring present inside the parent string at what index
# -1: will get return if the particualr word is not present in the parent string
index = str.find("Learn")
print(index)

#9: capitilizae: to make the first letter of the first  word a capital and 
# rest all words are converetd to lowercase
t = "today Is THURSDAY"
res = t.capitalize()
print(res)

#10: endswith() method
res1 = s3.endswith("Learning")
print(res1)
f = "profile.jpg"
if f.endswith((".jpg",".PNG")):
     print(" File is matched")
else:
    print(" File is not matched")

#11: upper() is used to convert to uppercase and isupper() will check whether the complete string is upercase or not
r1 = t.upper()
res1 = r1.isupper()
print(res1)

#12: lower() is used to convert to my lowercase and islower() wil check whether the complete string is in lowercase or not
r = t.lower()
print(r)
r1 = r.islower()
print(r1)

#13: replace(): is used to reaplce all the occurances of a specified substring 
#in a given parent sintrg and it is applicable for both the letters and words
str = "python is easy , Python is open source and beginners can learn python fast"
rep = str.replace("Python","Java")
rep1 = str.replace("Python","Java",2)
print(rep)
print(rep1)

#14: partition(): is used to split the string into three parts 
#tuple(before_Seperator, seperator, after_seperator)
str2 = "Python is open source and python is Learning   "
t = str2.partition("is")
print(t)

str3 = "name : Viren"
t=str3.partition(":")
print(t)

#15: rfind(subsstring, start, end):
print(str2.rfind("i"))

#16: rstrip(chars): remove the extr trailing spaces from the ned of the string
print(len(str2))
y = str2.rstrip()
print(len(y))

#17: split(sep): it will split the string into the multiple sub strings and return as list
str4 = "Python is, open source and python, is Learning, very interesting"
p = str4.split(",", 1)
print(p)

#18:swapcase(): this will swap the uppercase to lowercase and vice versa
print(str2.swapcase())

#19: title(): it will convert the first character of each word to uppercase and rest all the chaters
# will be ine the lowercase only
print(str4.title())

#20: removeSuffix(suffix) 
str5 = "PythonIs, open sourceIs and we useIs in VisualStudio"
print(str5.removesuffix("Studio"))

#21: removePrefix(prefix)
print(str5.removeprefix("Python"))


