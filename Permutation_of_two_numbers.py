'''
Permutation of two numbers 
'''

def Permutation(list1, list2):
    # Check if the lengths of the two lists are different
    if len(list1) != len(list2):
        # If the lengths are not the same, they cannot be permutations of each other
        return False
    
    # Sort both lists to compare their elements in a standardized order
    list1.sort()
    list2.sort()
    
    # Compare the sorted lists
    if list1 == list2:
        # If the sorted lists are the same, then list1 is a permutation of list2
        return True
    else:
        # If the sorted lists are different, then list1 is not a permutation of list2
        return False

# Example list of numbers to test the function
list1 = [22, 14, 20, 2, 4, 6, 8, 12, 9, 16, 18, 10]
list2 = [2, 4, 6, 8, 10, 12, 9, 14, 16, 18, 20, 22]

# Example list of strings to test the function
list1 = ['a', 'c', 'e', 'f', 'z']
list2 = ['c', 'a', 'z', 'e', 'f']

# Print the result of the permutation check
print(Permutation(list1, list2))  # This should print True as the lists are permutations of each other


'''
#Explaination:

#Function Definition: The function Permutation takes two lists as input parameters list1 and list2.

#Length Check: It first checks if the lengths of the two lists are different. 
If they are, it returns False because lists of different lengths cannot be permutations of each other.

#Sorting: The function sorts both lists. 
Sorting the lists ensures that if they contain the same elements in any order, 
they will be identical after sorting.

#Comparison: It then compares the sorted lists. 
If they are identical, it returns True indicating that list1 is a permutation of list2. 
Otherwise, it returns False.

#Example Lists: Two pairs of example lists are provided, one for numbers and one for strings.

#Print Result: The function is called with the example lists, 
and the result is printed to show whether the lists are permutations of each other.


'''

