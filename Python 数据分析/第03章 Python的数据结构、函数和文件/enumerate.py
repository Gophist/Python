# Python内建了一个enumerate函数，可以返回(i, value)元组序列：

some_list = ['foo', 'bar', 'baz']

mapping = {}

for i, v in enumerate(some_list):
    mapping[i] = v

print(mapping)
