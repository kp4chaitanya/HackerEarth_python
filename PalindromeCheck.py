#Write a Python program to check if a given string is a palindrome

def palindrom_check(S1):
    S2=""
    #Reverse the string
    for i in range(len(S1)-1, -1, -1):
        S2=S2+str(S1[i])
    
    # Check if the original string is equal to the reversed string
    return S1 == S2

#function call
S1='raar'
Result=palindrom_check(S1)
if Result:
    print("Yes, the given string is a palindrome")
else:
    print("No, the given string is not a palindrome")