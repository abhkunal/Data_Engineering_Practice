#Reverse a string without using slicing ([::-1]).

#Solution 1
#Using reversed() and join(): This is a clean and Pythonic way to reverse a string. The reversed() function returns a reverse iterator, which is then joined into a string.

def reverse_string_reversed_join(s):
    reversed_chars = reversed(s)
    reversed_string = "".join(reversed_chars)
    return reversed_string

original = "Hello, World!"
reversed_text = reverse_string_reversed_join(original)
print(reversed_text)
# Output: !dlroW ,olleH


#Solution 2
#Using a for loop: You can iterate through the original string and prepend each character to a new, empty string.

def reverse_string_for_loop(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

original = "Hello, World!"
reversed_text = reverse_string_for_loop(original)
print(reversed_text)
# Output: !dlroW ,olleH


#Solution 3
#Using a while loop: This method involves iterating from the last index of the string down to the first index and concatenating characters to a new string.

def reverse_string_while_loop(s):
    reversed_string = ""
    index = len(s) - 1
    while index >= 0:
        reversed_string += s[index]
        index -= 1
    return reversed_string

original = "Hello, World!"
reversed_text = reverse_string_while_loop(original)
print(reversed_text)
# Output: !dlroW ,olleH

#Solution 4
#Using recursion: A function can call itself repeatedly, taking the last character of the string and appending it to the reverse of the remaining substring.

def reverse_string_recursion(s):
    if len(s) <= 1:
        return s
    else:
        # Recursively call with the substring excluding the first char, 
        # and append the first char at the end
        return reverse_string_recursion(s[1:]) + s[0]

original = "Hello, World!"
reversed_text = reverse_string_recursion(original)
print(reversed_text)
# Output: !dlroW ,olleH

#Solution 5
#Using list and its reverse() method: Since strings are immutable in Python, you can convert the string to a list of characters, use the built-in list.reverse() method (which works in-place), and then join the list back into a string.

def reverse_string_list_method(s):
    temp_list = list(s)
    temp_list.reverse()
    reversed_string = "".join(temp_list)
    return reversed_string

original = "Hello, World!"
reversed_text = reverse_string_list_method(original)
print(reversed_text)
# Output: !dlroW ,olleH

