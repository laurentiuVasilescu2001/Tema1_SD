def radixSort(unsorted_list):
    maximum_value = max(unsorted_list)
    max_exponent = len(str(maximum_value))
    being_sorted = unsorted_list[:]
    for exponent in range(max_exponent):
        position = exponent + 1
        index = -position
        bucket = [[] for i in range(10)]
        for number in being_sorted:
            number_as_a_string = str(number)
            try:
                digit = number_as_a_string[index]
            except IndexError: 
                digit = 0
            digit = int(digit)
            bucket[digit].append(number)
        being_sorted = []
        for numeral in bucket:
            being_sorted.extend(numeral)
    return being_sorted