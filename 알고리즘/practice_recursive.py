def factorical(n):
    if n == 1:
        return 1

    return n * factorical(n - 1)

print(factorical(5))





 

def sum_of_list(arr):
    if not arr:
        return 0

    return arr[0] + sum_of_list(arr[1::])

numbers = [1, 2, 3, 4, 5]
print(sum_of_list(numbers))





def gcd(a, b):
    if b == 0 :
        return a
    # print(a, b)
    
    return gcd(b, a % b)

print(gcd(24, 16))
