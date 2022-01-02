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

###### Dataframe conversion

# Convert to dictionary of columns containing rows as dictionary with Indices as Keys
df_dict = df.head(2).to_dict("dict")
# {'column_1': {'Index_1': 'row_1", ... }, 'column_2': {'Index_1': 'row_1', ...}}
# {'_1st_dose_allocations': {0: 54360, 1: 21420},
#  '_2nd_dose_allocations': {0: 54360, 1: 21420},
#  'jurisdiction': {0: 'Connecticut', 1: 'Maine'},
#  'week_of_allocations': {0: '2021-06-21T00:00:00.000',
#   1: '2021-06-21T00:00:00.000'}}

# Convert to dictionary of columns with rows as lists:
df_dict_2 = df.head(2).to_dict("list")
# {'column_1': ['row_1", ... ], 'column_2': ['row_1', ...]}
# {'_1st_dose_allocations': [54360, 21420],
#  '_2nd_dose_allocations': [54360, 21420],
#  'jurisdiction': ['Connecticut', 'Maine'],
#  'week_of_allocations': ['2021-06-21T00:00:00.000', '2021-06-21T00:00:00.000']}

# Convert to list of dictionaries with each list item representing a row:
df_list = df.head(2).to_dict("records")
# [{'column_1': ..., 'column_2': ...}, {'column_1': ..., 'column_2': ...}]
# [{'_1st_dose_allocations': 54360,
#   '_2nd_dose_allocations': 54360,
#   'jurisdiction': 'Connecticut',
#   'week_of_allocations': '2021-06-21T00:00:00.000'},
#  {'_1st_dose_allocations': 21420,
#   '_2nd_dose_allocations': 21420,
#   'jurisdiction': 'Maine',
#   'week_of_allocations': '2021-06-21T00:00:00.000'}]

#### COLUMN & INDEX Manipulations

# Create a new column from Index in a DatFrame
# Index                 Col1    Col2
# 2021-12-31 00:30:00     1     "test"
# 2022-01-01 00:35:00     22    "me"
df.reset_index(inplace=True)
# Index     index                   Col1    Col2
# 1         2021-12-31 00:30:00       1     "test"
# 2         2022-01-01 00:35:00      99      "me"

# Rename columns in a DataFrame
df.rename(columns={"index": "timestamp"}, inplace=True)

# Map values in column to another value:
# for example: string "2021-12-31 00:30:00" to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"], format='%Y-%m-%d %H:%M:%S')
# datetime format patterns:
# %Y: Year (4 digits)
# %m: Month
# %d: Day of month
# %H: Hour (24 hour)
# %M: Minutes
# %S: Seconds
# %f: Microseconds
# https://stackabuse.com/converting-strings-to-datetime-in-python/

# set index on column for grouping data by timestamp:
# transforms datetime-column to DatetimeIndex
df.set_index("timestamp")
# Need to reset index after using set_index
df.reset_index()

# group by timestamp
df_grouped = df.groupby(pd.Grouper(key="timestamp", freq="5Min")).volume.sum()

# Working with datetimes: https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html
# Remember:
# (1) Valid date strings can be converted to datetime objects using to_datetime function or as part of read functions.
# (2) Datetime objects in pandas support calculations, logical operations and convenient date-related properties using the dt accessor.
# (3) A DatetimeIndex contains these date-related properties and supports convenient slicing.
# (4) Resample is a powerful method to change the frequency of a time series.

# Cast column to another datatype
# Example: str -> int
df["volume"] = df["volume"].astype(int)
