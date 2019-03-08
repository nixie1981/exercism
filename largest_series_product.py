from numpy import prod


def largest_product(series, size):
    if size > len(series):
        raise ValueError("The input string is too short")
    elif size < 0:
        raise ValueError("The length must be positive")
    elif size == 0:
        return 1
    else:
        lists = ([series[i:i + size] for i in range(len(series) - size + 1)])
        output = []
        for l in lists:
            numbers = [int(n) for n in list(l)]
            output.append(numbers)
        return max([prod(item) for item in output])
    