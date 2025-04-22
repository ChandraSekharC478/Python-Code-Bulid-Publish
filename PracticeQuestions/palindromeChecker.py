def palindromeChecker(string):
    is_Palindrome = False
    for char in range(len(string)//2):
        if string[char] != string[-char-1]:  # Compare front and back characters
            is_Palindrome = False 
            break
        else:
            is_Palindrome = True
    if is_Palindrome:
        print("The given word is Palindrome")
    else:
        print("The given word is not Palindrome")
# Test the function with a sample string
palindromeChecker("chandhu")  # Output: The given word is not Palindrome
palindromeChecker("madam") # Output: The given  word is Palindrome 
    
