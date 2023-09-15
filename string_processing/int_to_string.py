def int_to_str(input_int):
    is_negative = False
    if input_int < 0:
        is_negative = True
        input_int = input_int * -1

    result = []
    if input_int == 0:
        result.insert(0, input_int)
    else:
        while input_int > 0:
            result.insert(0, chr(ord('0') + input_int % 10))
            input_int //= 10

    result = ''.join(result)

    if is_negative:
        return '-' + result
    else:
        return result


num = -123
print(num)
print(type(num))
print(num)
print(type(int_to_str(123)))
