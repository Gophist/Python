import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))

df2.loc[1, "b"] = np.nan

df1.add(df2, fill_value=0)

print("")