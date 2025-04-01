import pandas as pd

df_titanic = pd.read_excel("titanic.xlsx")

def filter_survivors(df):
    return df[df['Survived'] == 1].copy()

def fill_missing_age(df):
    df.loc[:,'Age'] = df['Age'].fillna(df['Age'].mean())
    return df

def add_fare_per_age(df):
    df.loc[:, "Fare_per_age"] = df["Fare"] / df["Age"]
    return df

df_titanic_filtered = (
    df_titanic.pipe(filter_survivors)
              .pipe(fill_missing_age)
              .pipe(add_fare_per_age)
)

if __name__ == '__main__':
    print(df_titanic_filtered.head())