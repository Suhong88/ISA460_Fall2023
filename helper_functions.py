# create a function to display sample records by a group of columns

import numpy as np

def displayByGroup(df, group_size, sample_size=5):
    column_split=np.array_split(df.columns, len(df.columns)//group_size)
    for X in column_split:
        df.select(*X).show(sample_size,False)