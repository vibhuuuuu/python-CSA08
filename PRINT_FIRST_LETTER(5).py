def get_first_letters(sentence):
    words = sentence.split()
    first_letters = [word[0] for word in words]
    result = '.'.join(first_letters).upper()
    return result


input_sentence = "The cat on the wall"
output = get_first_letters(input_sentence)
print(output)
