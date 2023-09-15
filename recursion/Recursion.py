def find_uppercase(input_str, idx=0):
    """find uppercase letter in string"""
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:  # not found any uppercase letter in string
        return None
    return find_uppercase(input_str, idx + 1)


def find_len_string(input_str):
    if input_str == '':
        return 0
    return 1 + find_len_string(input_str[1:])


# print(find_len_string(input_str="abc"))

vowels = "aeiou"


def iterative_count_consonants(input_str):
    consonant_count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowels and input_str[i].isalpha():
            consonant_count += 1
    return consonant_count


def recursion_count_consonants(input_str):
    if input_str == '':
        return 0
    # if not in vowels then increment by 1 and continue process
    if input_str[0].lower() not in vowels:
        return 1 + recursion_count_consonants(input_str[1:])
    return recursion_count_consonants(input_str[1:])


def recursive_multiply(x, y):
    if y == 1:
        return x
    if x < y:
        return recursive_multiply(y, x)
    return x + recursive_multiply(x, y - 1)


print(recursive_multiply(2, 3))
