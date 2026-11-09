def range_of_numbers(start_num, end_num):
    if start_num == end_num:
        return [start_num]

    if start_num > end_num:
        return "The start number is big"

    serie = range_of_numbers(start_num + 1, end_num)
    serie.append(start_num)
    return sorted(serie)


print(range_of_numbers(1, 5))
