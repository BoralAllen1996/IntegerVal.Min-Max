#This program only has minimun and maximum range of number...

#Create the number list
numlist= [int(input("\nPlease enter a number:"))for i in range(5)]

largest = smallest = numlist[1]

for i in numlist:
    if i >largest:    #This determine the largest number...
        largest=i
        
    if i<smallest:     #This determine the smallest number ...
        smallest=i
        
# This indicates the max and min of integers....
print("\nThe maximum of 5 numbers in the list=",largest,
    "\nThe minimum of 5 numbers in the list=",smallest)       

print("\nThank you!")

#End process......