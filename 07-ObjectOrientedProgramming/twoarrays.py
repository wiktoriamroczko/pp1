from arrays import arrays

a1 = arrays()
a2 = arrays()

array1 = a1.arr1(10,4)
array2 = a2.arr2(20,-7,8)

print(array1)
print(array2)

el = a2.szukaj(array2, -1, 1)
print(el, len(el))