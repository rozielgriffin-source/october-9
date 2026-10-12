"""
1) Add the file and topic details.
   a) Mention the file name as `02-power-of-4-8.py`.
   b) Mention the topic as "Power of 4 and Power of 8".
   c) Introduce the program as a way to check powers using bitwise and modulus rules.

2) Explain the power rules.
   a) Pause before showing the examples.
   b) Show that powers of 4 follow `n % 3 == 1`.
   c) Show that powers of 8 follow `n % 7 == 1`.

3) Show fixed examples.
   a) Print the binary form of 16.
   b) Show that `16 % 3` equals 1.
   c) Print the binary form of 8.
   d) Show that `8 % 7` equals 1.

4) Ask for a number.
   a) Ask the user to enter a number.
   b) Suggest example values like 64 or 32.
   c) Convert the input into an integer.

5) Ask for a prediction.
   a) Ask whether the number is a power of 4.
   b) Store the user's guess.

6) Check power of 4.
   a) Pause before running the check.
   b) Check that the number is greater than 0.
   c) Use `(n & (n - 1)) == 0` to confirm only one bit is ON.
   d) Use `n % 3 == 1` to confirm it is a power of 4.

7) Display the final result.
   a) Print the number.
   b) Print its binary form.
   c) Print whether it is a power of 4.
   d) Show the user's original guess.
"""