import pandas as pd
import numpy as np
from pydataset import data
# Create a function named get_db_url. It should accept a username, hostname, password, and database name and 
# return a url connection string formatted like in the example at the start of this lesson.
from env import host, password, username
def get_connection(db, user=username, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
url = get_connection('employees', username, host, password)

# Use your function to obtain a connection to the employees database.

# Once you have successfully run a query:
pd.read_sql('SELECT * FROM employees', url).head()

# a. Intentionally make a typo in the database url. What kind of error message do you see?
# Intentionally misspelled 'employees' and got an access denied on that database

# b. Intentionally make an error in your SQL query. What does the error message look like?
# Misspelled 'SELECT' and got: (1064, "You have an error in your SQL syntax; check the manual that 
# corresponds to your MySQL server version for the right syntax to use near 'SELCT * FROM employees' at 
# line 1") [SQL: SELCT * FROM employees]

# Read the employees and titles tables into two separate DataFrames.
employees_df = pd.read_sql('SELECT * FROM employees', url)
titles_df = pd.read_sql('SELECT * FROM titles', url)

# How many rows and columns do you have in each DataFrame? Is that what you expected?
employees_df
# 300024 rows × 6 columns
titles_df
# 443308 rows × 4 columns

# Display the summary statistics for each DataFrame.
employees_df.describe()
# count	300024.000000
# mean	253321.763392
# std	161828.235540
# min	10001.000000
# 25%	85006.750000
# 50%	249987.500000
# 75%	424993.250000
# max	499999.000000
titles_df.describe()
# count	443308.000000
# mean	253075.034430
# std	161853.292613
# min	10001.000000
# 25%	84855.750000
# 50%	249847.500000
# 75%	424891.250000
# max	499999.000000

# How many unique titles are in the titles DataFrame?
titles_df.title.unique()
# array(['Senior Engineer', 'Staff', 'Engineer', 'Senior Staff',
#       'Assistant Engineer', 'Technique Leader', 'Manager'], dtype=object)

# What is the oldest date in the to_date column?
titles_df.sort_values(by='to_date').head(1)
# 16064	20869	Engineer	1985-02-17	1985-03-01

# What is the most recent date in the to_date column?
titles_df.sort_values(by='to_date', ascending=False).head(1)
# 0	10001	Senior Engineer	1986-06-26	9999-01-01