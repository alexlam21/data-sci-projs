import pandas
commute_df = pandas.read_csv("commute_data.csv")
print(commute_df.head())
commute_df.columns = ["NAME", "COMMUTERS", "90+ MIN", "CODE", "C CODE"]

print(commute_df.head())
