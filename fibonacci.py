n = int(input("Enter the number of terms: "))

a, b = 0, 1  # First two terms

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b  # Update values
