import pandas as pd

# (1) DataFrame:
# Dictionary of columns { "column_1": [...], "columns_2": [...] }
# DataFrame-Keys are Column-Names: Column
# Sequence-Index are Row-Indices: Index

# (2) Sequence:
# Lists of Rows

# load csv file as DataFrame
df = pd.read_csv("cdc-pfizer-covid-19-vaccine-distribution-by-state.csv")

# get columns:
df.columns

# get rows:
df.index

# stats:
df.describe()

####### Creating Dataframes:

my_dict = {
    "column_1": ["brummer", "beller", "miauer"],
    "column_2": [33, 44, 22]
}
df_new = pd.DataFrame(index=range(0, 3), data=my_dict)

####### Selecting data from DataFrame:

# get subset of Dataframe by Index/Rows and Column-Names:
df_subset = df.loc[50:60, ['jurisdiction', 'week_of_allocations']]

# get subset of Dataframe by Index-Number and Column-Number:
df_subset_2 = df.iloc[50:60, [1, 2]]

####### CRUD-Operation on DataFrame:

####### DELETE

# delete rows from Dataframe:
df.drop(index=[2, 3], inplace=True)

# delete columns from Dataframe:
df.drop(columns=["jurisdiction"], inplace=True)

# delete duplicate rows from Dataframe with identical columns:
df.drop_duplicates(subset=["jurisdiction"], inplace=True, keep="last")

####### INSERT

# insert rows into Dataframe:

# At the end:
df.append(df_new, ignore_index=True)

# append columns to a Dataframe:
df["gender"] = df.jurisdiction.str.contains("ad")

####### UPDATE

# update entry in row 100 & column "jurisdiction"
df.loc[100, 'jurisdiction'] = "Alabama"
# check entry
df.loc[100, :]

###### Data Read Operation

# group by column: Returns a series
df.groupby(by="week_of_allocations")["_2nd_dose_allocations"].sum()

# sort rows by column:
df.sort_values(by="_2nd_dose_allocations", ascending=False)

# example: group by "jurisdiction" and sum column: "_2nd_dose_allocations"
# Finds the jurisdiction with highest vaccination with 2nd shot
group_series = df.groupby(by="jurisdiction")["_2nd_dose_allocations"].sum()
group_series.sort_values(ascending=False)
