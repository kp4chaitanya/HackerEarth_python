def freq_string(Str1):
    """ 
    This Function calculates the frequency of the words
    Input: String of words
    Output: Dictionary with frequency of words

    """

    print("Start executing")
    
    #String to list conversion
    l1=Str1.split()
    #List elements
    print(l1)
    # Using dictionary
    count = {}
    for i in l1:
        if i not in count:
            count[i] = 0
        count[i] += 1

    return count   

#Input string
s1='Airbnb and Airbnb are two Airbnb companies and are independent'
#Function call
print(freq_string(s1))
