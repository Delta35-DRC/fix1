result = []


def processor(a, b):
    try:
        return a / b
    except Exception as error:
        print(error)


data = [10, 2, 2, 5, '123', 4, 18, 0, [], 15, 8, 4]
for i in range(5):  # does not count if 'data.count(any)' instead of 5
    res = processor(data.pop(0), data.pop(1))
    result.append(res)

print(data.count(any))
print(data)
print(result)
