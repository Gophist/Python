import numpy as np
import pandas as pd

obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
# print(obj)

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', "New York"],
                    columns=["one", "two", "three", "four"])

print1 = data['two']
print2 = data[['three', 'one']]

# 通过切片或布尔型数组选取数据
slice = data[:2]
bool = data[data['three'] > 5]

# 另一种用法是通过布尔型DataFrame 进行索引：
bool2 = data < 5
print(bool2)

set_less_than_5_to_zero = data
set_less_than_5_to_zero[set_less_than_5_to_zero < 5] = 0
print(set_less_than_5_to_zero)

# 用 loc 和 iloc 进行选取
loc = data.loc["Colorado", ["two", "three"]]

# 然后用 iloc 进行选取：
iloc = data.iloc[2, [3, 0, 1]]
iloc2 = data.iloc[2]
iloc3 = data.iloc[[1, 2], [3, 0, 1]]

# 这两个索引函数也适用于一个标签或多个标签的切片：
data.loc[:'Utah', 'two']


print('')
