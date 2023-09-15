def str_to_int(input_str):
    start_idx = 0
    is_negative = False
    result = 0

    if input_str[0] == '-':
        start_idx = 1
        is_negative = True

    for i in range(start_idx,len(input_str)):
        place = 10 ** (len(input_str) - (i + 1))
        digit = (ord(input_str[i]) - ord('0'))  # take the first digit of the input_str as a type int
        result += place * digit
    if is_negative:
        return result * -1
    return result


input_string = "529"
print(input_string)
print(type(input_string))
print(input_string)

print(type(str_to_int(input_string)))

