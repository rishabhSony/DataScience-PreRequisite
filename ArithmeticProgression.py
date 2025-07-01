# Get three A.P. terms from the user
a1 = int(input("Enter the first term: "))
a2 = int(input("Enter the second term: "))
a3 = int(input("Enter the third term: "))

# In an A.P., the difference between consecutive terms is the same
# So, the common difference can be found as:
d1 = a2 - a1
d2 = a3 - a2

# Check if it's a valid A.P.
if d1 == d2:
    print("The common difference is:", d1)
else:
    print("The entered numbers are not in Arithmetic Progression.")
