def spreadsheet_encode_col(str_col):
    count = len(str_col) - 1
    result = 0
    for s in str_col:
        result += (26 ** count) * (ord(s) - ord("A") + 1)
        count -= 1
    return result


print(spreadsheet_encode_col("AB"))
