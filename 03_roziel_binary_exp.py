input("Binary exponention uses bit of the exponent. press enter. ")
print("2^8 = 256   binary of exponent 8: ", bin(8)[2:])
print("2^5 = 32   binary of exponent 5: ", bin(5)[2:])

exp = int(input("Enter an exponent (try 3 or 6): "))
print(" Exponent: ", exp, "binary of exponent: ", bin(exp)[2:])
guess = input("What is 2^" + str(exp) + "?")
input("Biinary exponentiation reads bit of an exponent. press enter.")
print("2^", exp, "is: ", 2**exp, ". your guess was ", guess)