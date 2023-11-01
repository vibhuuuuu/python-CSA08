n = int(input("Enter the number of elements in the list: "))


elements = []


for i in range(n):
    element = int(input(f"Enter element{i + 1}: "))
    elements.append(element)

non_duplicate_items = list(set(elements))


print("Non-duplicate items:", non_duplicate_items)

