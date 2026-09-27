count = 1
total = 0

# BUG: Missing colon after while condition. Added colon to make it valid syntax.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Condition was count < 5 which only sums 1 to 4 (answer 10). Changed to count <= 5 to include 5 and get correct answer 15. This bug had no error message.
# BUG: Cannot concatenate string and integer with +. Fixed by converting total to string with str(total).
print("Sum of 1 to 5 is: " + str(total))
