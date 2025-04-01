import pandas as pd

df_titanic = pd.read_excel("titanic.xlsx")
df_movies = pd.read_csv("movie.csv")

df_titanic_grouped = df_titanic.groupby('Pclass').agg(
    average_age = ('Age', 'mean'),
    total_fare = ('Fare', 'sum'),
    passenger_count = ('PassengerId', 'count')
).reset_index()

df_movies_grouped = df_movies.groupby(['color', 'director_name']).agg(
    total_reviews = ('num_critic_for_reviews', 'sum'),
    avg_duration = ('duration', 'mean')
).reset_index()

if __name__ == '__main__':
    print(df_titanic_grouped)
    print(df_movies_grouped.head())