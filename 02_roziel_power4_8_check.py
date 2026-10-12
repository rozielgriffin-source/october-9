input("Power of 4 - n % 3 == 1, power of 8 - n % 7 == 1. Press enter. ")
print("Binary of 16: ", bin(16)[2:], "16 % 3: ", 16 % 3, "16 is a power of 4.")
print(" Binary of 8: ", bin(8)[2:], "8 % 7: ", 8 % 7, "8 is a power of 8.")

n = int(input("Enter a number (32 or 64): "))
guess = input("Is " + str(n) + " a power of 4?")

input("In powers of 4 n % 3 will return 1. press enter. ")
power = n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
if power:
    print("n is ", n, " Binary of n: ", bin(n)[2:], " Power of 4: yes, your guess: ", guess)
else:
    print("n is ", n, " Binary of n: ", bin(n)[2:], " Power of 4: no, your guess: ", guess)