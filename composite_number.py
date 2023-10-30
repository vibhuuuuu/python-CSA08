
def is_composite(num):
    if num < 4:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False


array_of_elements = [16, 18, 27, 16, 23, 21, 19]


composite_count = 0
for num in array_of_elements:
    if is_composite(num):
        composite_count += 1


print(f"Number of Composite Numbers = {composite_count}")
