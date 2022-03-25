def find_even_1to50():
    result = []
    for num in range(1, 51):
        if num % 2 == 0:
            result.append(num)
    return result

print(find_even_1to50())