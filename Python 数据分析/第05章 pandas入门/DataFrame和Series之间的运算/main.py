import numpy as np
import pandas as pd

# 先来看一个具有启发性的例子，计算一个二维数组与其某行之间的差：


arr = np.arange(12.).reshape((3, 4))

print(arr, arr[0])

print(arr - arr[0])

# 当我们从arr减去arr[0]，每一行都会执行这个操作。这就叫做广播（broadcasting）

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])

series = frame.iloc[0]

series3 = frame['d']

minus = frame - series
minus2 = frame.sub(series3, axis="index")

print("")
