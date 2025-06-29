# # Input values
# X = int(input("Enter the base (X): "))
# N = int(input("Enter the exponent (N): "))

# # Calculate power
# result = X ** N

# # Print the result
# print(f"{X} raised to the power {N} is: {result}")


X = int(input("Enter the base (X): "))
N = int(input("Enter the exponent (N): "))

# Manual power calculation using loop
result = 1
for i in range(N):
    result *= X

print(f"{X} raised to the power {N} is: {result}")




