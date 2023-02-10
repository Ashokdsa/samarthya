def reverse_string(s):
    reversed_string = ""
    for i in range(len(s) - 1, -1,-1):
        reversed_string += s[i]
    return reversed_string

s = input("Enter a string: ")
reversed_string = reverse_string(s)
for i in range(0,len(s)):
    if(s[i]!=reversed_string[i]):
        print("It's not a Palindrome.")
        exit(0)
print("The String is a Palindrome")