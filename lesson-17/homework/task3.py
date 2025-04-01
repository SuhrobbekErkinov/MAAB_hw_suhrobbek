import pandas as pd

df_titanic = pd.read_excel("titanic.xlsx")
df_employee = pd.read_csv("employee.csv")
df_movie = pd.read_csv("movie.csv")

def classify_age(age):
    if age < 18:
        return "Child"
    else:
        return "Adult"

df_titanic["age_group"] =  df_titanic['Age'].apply(classify_age)

def normalize(group):
    group['BASE_SALARY'] = (group['BASE_SALARY'] - group['BASE_SALARY'].min()) / (group['BASE_SALARY'].max() - group['BASE_SALARY'].min())
    return group
df_employee = df_employee.groupby("DEPARTMENT", group_keys=False).apply(normalize, include_groups=False)

def duration_type(duration):
    if duration < 60:
        return "Short"
    elif 60 <= duration <= 120:
        return "Medium"
    else:
        return "Long"
df_movie["duration_type"] = df_movie['duration'].apply(duration_type)

if __name__ == '__main__':
    print(df_titanic[["Age", "age_group"]].head())
    print(df_employee.head())
    print(df_movie[['duration', 'duration_type']].sample(10))
