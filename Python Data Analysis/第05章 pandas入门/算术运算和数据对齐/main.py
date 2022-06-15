import numpy as np
import pandas as pd

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'b', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'b', 'c', 'd', 'e'])

s3 = s1 + s2
print(s3)
print("")

# 自动的数据对齐操作在不重叠的索引处引入了NA值。缺失值会在算术运算过程中传播。
#
# 对于DataFrame，对齐操作会同时发生在行和列上：

# 把它们相加后将会返回一个新的DataFrame，其索引和列为原来那两个DataFrame的并集：

# 因为'c'和'e'列均不在两个DataFrame对象中，在结果中以缺省值呈现。行也是同样。
#
# 如果DataFrame对象相加，没有共用的列或行标签，结果都会是空：
