import numpy as np
import pandas as pd

data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

#           one  two  three  four
# Ohio        0    1      2     3
# Colorado    4    5      6     7
# Utah        8    9     10    11
# New York   12   13     14    15

# 用标签序列调用drop 会从行标签（axis 0）删除值：

# print(data.drop(['Colorado', 'Ohio']))
#           one  two  three  four
# Utah        8    9     10    11
# New York   12   13     14    15

# 通过传递axis=1或axis='columns'可以删除列的值：
# print(data.drop('two', axis=1))
# print(data.drop('two', axis="columns"))

#           one  three  four
# Ohio        0      2     3
# Colorado    4      6     7
# Utah        8     10    11
# New York   12     14    15


print(data)
