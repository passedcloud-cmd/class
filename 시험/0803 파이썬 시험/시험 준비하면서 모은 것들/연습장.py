# from collections import defaultdict

# fruits = [('red', 'apple'), ('yellow', 'banana'), ('red', 'cherry')]
# fruit_by_color = defaultdict(list) # 그룹핑/리스트 모으기
# for a, b in fruits:
#     fruit_by_color[a].append(b)

# print(fruit_by_color)
# print(dict(fruit_by_color))




def my_all(elements):
    if bool(elements) is False:
        result = True
    else:
        for element in elements:
            if element:
                result = True
            elif bool(element) is False:
                result = False
                break
    return result

print(my_all([]))
print(my_all([1, 2, 5, '6']))
print(my_all([[], 2, 5, '6']))
print(all([]), all([1, 2, 5, '6']), all([[], 2, 5, '6']))