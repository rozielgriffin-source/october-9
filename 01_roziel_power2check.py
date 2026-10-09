input("N & N-1 will clear the rightmost bit. press enter. ")
print("12 & 11: ", 12 & 11, " binary: ", bin(12 & 11)[2:])
print("8 & 7: ", 8 & 7)

n = int(input("Enter a number: "))
guess = input("Is " + str(n) + "a power of 2? (yes or no): ")
input("Power of 2: n &  (n-1) will equal 0 if it is a power of 2. Press enter. ")
if n > 0 and (n & (n-1)) == 0:
    print("N is ", n, "Binary of n: ", bin(n)[2:], n, "is a power of 2. your guess = ", guess)
else:
    print("N is ", n, "Binary of n: ", bin(n)[2:], n, "is not a power of 2. your guess = ", guess)