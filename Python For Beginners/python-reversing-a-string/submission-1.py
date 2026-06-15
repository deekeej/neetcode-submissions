def reverse_string(input_string: str) -> str:
    if (type(input_string) is not str):
        return ''
    return input_string[::-1]

# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))
