import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")
df_customers = pd.read_sql("SELECT * FROM customers", conn)
df_invoices = pd.read_sql("SELECT * FROM invoices", conn)
df_merged = pd.merge(df_customers, df_invoices, on="CustomerId", how="inner")

invoice_counts = df_merged.groupby("CustomerId")["InvoiceId"].count().reset_index()
invoice_counts.rename(columns={"InvoiceId" : "Total invoices"}, inplace=True)

df_movies = pd.read_csv("movie.csv")
df_1 = df_movies[['director_name', 'color']].dropna()
df_2 = df_movies[['director_name', 'num_critic_for_reviews']].dropna()
df_left_join = pd.merge(df_1, df_2, on="director_name", how="left")
df_outer_join = pd.merge(df_1, df_2, on="director_name", how="outer")

if __name__ == '__main__':
    print(df_merged.head())
    print(invoice_counts.head())
    print("\nRows in LEFT JOIN result: ", len(df_left_join))
    print("\nRows in OUTER JOIN results: ", len(df_outer_join))