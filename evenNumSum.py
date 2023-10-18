# Write a Python program to find the sum of all even numbers from 1 to n, where n is a positive integer provided by the user.

# Function definition
def evenNumSum(N):
    #Initialize sum to 0
    sum = 0
    
    #Check if i is even
    for i in range(2, N+1):
        if(i%2==0):
            #Add i to sum
            sum += i

    #Return sum        
    return sum

#Function call
print(evenNumSum(5))