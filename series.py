def slices(series, length):
    if length > len(series):
        raise ValueError("The input string is too short")
    elif length < 1:
        raise ValueError("The length must be positive")
    else:
        return [series[i:i+ length] for i in range (len(series) - length + 1)]
        