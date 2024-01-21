def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1

        mid = (low + high) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
            # якщо x не останній елемент масиву використовуємо його як верхню межу
            upper_bound = arr[mid] if mid + 1 < len(arr) else None
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            upper_bound = arr[mid]
        else:
            high = mid - 1
            upper_bound = arr[mid]

    return iterations, upper_bound


# Тестування функції
arr = [1.2, 2.5, 3.7, 4.8, 5.9]
x = 4.0
print(binary_search(arr, x))
x2 = 1.2
print(binary_search(arr, x2))
x3 = 5.9
print(binary_search(arr, x2))
x4 = 6.0
print(binary_search(arr, x4))
x5 = 1.0
print(binary_search(arr, x5))
