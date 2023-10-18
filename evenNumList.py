"""
Write a Python function that takes a list of numbers as input and returns a new list that contains only the even numbers from the input list.
For example, if the input list is [1, 2, 3, 4, 5, 6], the function should return [2, 4, 6].
"""
def evenNumList(L1):
    L2=[i for i in L1 if i%2==0]
    return L2

new_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result=evenNumList(new_list)
print(result)
