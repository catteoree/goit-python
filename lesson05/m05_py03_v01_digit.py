def sanitize(data):
    result = []
    for el in data:
        if el.isdigit():
            result.append(el)
    return result


def transform_to_int(data):
    result = []
    for el in data:
        result.append(int(el))
    return result


if __name__ == "__main__":
    numbers = ["123", "456", "100", "10", "13", "abc", "23a"]
    
    sanitize_numbers = sanitize(numbers)
    sanitize_numbers = transform_to_int(sanitize_numbers)

# Изменяет сам список, к которому применяется:
    sanitize_numbers.sort()
    print(sanitize_numbers)

# Не изменяет список, возвращает новый отсортированный список:
    sorted_sanitize_numbers = sorted(sanitize_numbers, reverse=True)

    print(max(sanitize_numbers))
    print(min(sanitize_numbers))
    print(sum(sanitize_numbers)/len(sanitize_numbers))
    print(sorted_sanitize_numbers)
