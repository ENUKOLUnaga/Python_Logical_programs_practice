import pandas as pd
"""s=pd.Series([10,20,30])
print(s)
"""

"""data = {
    "name":["A","B","C"],
    "age":[20,25,30]
}

df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.loc[0,"name"])
print(df.iloc[0,"A"])
"""

"""data = {
    "dept": ["IT", "HR", "IT", "HR"],
    "salary": [1000, 2000, 1500, 2500]
}

df = pd.DataFrame(data)

print(df.groupby("dept")["salary"].mean())
"""

df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["A", "B", "C"]
})

df2 = pd.DataFrame({
    "id": [1, 2, 4],
    "salary": [1000, 2000, 3000]
})

print(pd.merge(df1, df2, on="id", how="inner"))

