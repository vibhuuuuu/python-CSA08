
input_string = input("Enter the string: ")
char_to_search = input("Enter the character to be searched: ")


char_found = False


for index, char in enumerate(input_string):
    if char == char_to_search:
        char_found = True
        print(f"{char_to_search} is found in the string at index: {index}")
        break


if not char_found:
    print(f"{char_to_search} is not present in the given string.")
