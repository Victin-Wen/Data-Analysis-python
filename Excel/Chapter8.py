"""Chapter8 数据运算"""
import pandas as pd

df = pd.DataFrame([[1, 2, 3], [4, 5, 6]],
                  columns=["C1", "C2", "C3"],
                  index=["S1", "S2"])
print("df = ")
print(df)
print("sum=")
print(df["C1"] + df["C2"])
