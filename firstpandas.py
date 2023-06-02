import pandas
commute_df = pandas.read_csv("commute_data.csv")
print(commute_df.head())
commute_df.columns = ["COUNTY", "NAME", "TOTAL COMMUTER COUNT", "STATE CODE", "COUNTY CODE"]

print(commute_df.head())
