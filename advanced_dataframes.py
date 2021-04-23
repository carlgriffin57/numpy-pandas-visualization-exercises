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

# Copy the users and roles DataFrames from the examples above.
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})


# What is the result of using a right join on the DataFrames?
(roles.merge(users, left_on='id', right_on='role_id', how='right', indicator=True).drop(columns='role_id')
.rename(columns={'id_x': 'id', 
                'name_x': 'role',
                'id_y': 'role_id',
                'name_y': 'employee'}
        )
)

# 	id	role	role_id	employee	_merge
# 0	1.0	admin	1	bob	both
# 1	2.0	author	2	joe	both
# 2	3.0	reviewer	3	sally	both
# 3	3.0	reviewer	4	adam	both
# 4	NaN	NaN	5	jane	right_only
# 5	NaN	NaN	6	mike	right_only

# What is the result of using an outer join on the DataFrames?
(roles.merge(users, left_on='id', right_on='role_id', how='outer', indicator=True).drop(columns='role_id')
.rename(columns={'id_x': 'id', 
                'name_x': 'role',
                'id_y': 'role_id',
                'name_y': 'employee'}
        )
)
# 	id	role	role_id	employee	_merge
# 0	1.0	admin	1.0	bob	both
# 1	2.0	author	2.0	joe	both
# 2	3.0	reviewer	3.0	sally	both
# 3	3.0	reviewer	4.0	adam	both
# 4	4.0	commenter	NaN	NaN	left_only
# 5	NaN	NaN	5.0	jane	right_only
# 6	NaN	NaN	6.0	mike	right_only

# What happens if you drop the foreign keys from the DataFrames and try to merge them?
roles.merge(users, left_on=None, right_on=None, how='outer', indicator=True)
# 	id	name	role_id	_merge
# 0	1	admin	NaN	left_only
# 1	2	author	NaN	left_only
# 2	3	reviewer	NaN	left_only
# 3	4	commenter	NaN	left_only
# 4	1	bob	1.0	right_only
# 5	2	joe	2.0	right_only
# 6	3	sally	3.0	right_only
# 7	4	adam	3.0	right_only
# 8	5	jane	NaN	right_only
# 9	6	mike	NaN	right_only

# Load the mpg dataset from PyDataset.
mpg = data('mpg')

# Output and read the documentation for the mpg dataset.
data('mpg', show_doc=True)

# How many rows and columns are in the dataset?
mpg.shape
(234, 11)

# Check out your column names and perform any cleanup you may want on them.

# Display the summary statistics for the dataset.
mpg.describe()
# displ	year	cyl	cty	hwy
# count	234.000000	234.000000	234.000000	234.000000	234.000000
# mean	3.471795	2003.500000	5.888889	16.858974	23.440171
# std	1.291959	4.509646	1.611534	4.255946	5.954643
# min	1.600000	1999.000000	4.000000	9.000000	12.000000
# 25%	2.400000	1999.000000	4.000000	14.000000	18.000000
# 50%	3.300000	2003.500000	6.000000	17.000000	24.000000
# 75%	4.600000	2008.000000	8.000000	19.000000	27.000000
# max	7.000000	2008.000000	8.000000	35.000000	44.000000

# How many different manufacturers are there?
len(mpg.manufacturer.unique())
# 15

# How many different models are there?
len(mpg.model.unique())
# 38

# Create a column named mileage_difference like you did in the DataFrames exercises; this column should 
# contain the difference between highway and city mileage for each car.
mpg['mileage_difference'] = abs(mpg.hwy - mpg.cty)
# 	manufacturer	model	displ	year	cyl	trans	drv	cty	hwy	fl	class	mileage_difference
# 1	audi	a4	1.8	1999	4	auto(l5)	f	18	29	p	compact	11
# 2	audi	a4	1.8	1999	4	manual(m5)	f	21	29	p	compact	8
# 3	audi	a4	2.0	2008	4	manual(m6)	f	20	31	p	compact	11
# 4	audi	a4	2.0	2008	4	auto(av)	f	21	30	p	compact	9
# 5	audi	a4	2.8	1999	6	auto(l5)	f	16	26	p	compact	10

# Create a column named average_mileage like you did in the DataFrames exercises; this is the mean of the 
# city and highway mileage.
mpg['average_mileage'] = (mpg.hwy + mpg.cty) / 2
# 	manufacturer	model	displ	year	cyl	trans	drv	cty	hwy	fl	class	mileage_difference	average_mileage
# 1	audi	a4	1.8	1999	4	auto(l5)	f	18	29	p	compact	11	23.5
# 2	audi	a4	1.8	1999	4	manual(m5)	f	21	29	p	compact	8	25.0
# 3	audi	a4	2.0	2008	4	manual(m6)	f	20	31	p	compact	11	25.5
# 4	audi	a4	2.0	2008	4	auto(av)	f	21	30	p	compact	9	25.5
# 5	audi	a4	2.8	1999	6	auto(l5)	f	16	26	p	compact	10	21.0

# Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the 
# car has an automatic transmission.
mpg['is_automatic'] = np.where(mpg.trans.str.contains("auto"), 'True', 'False')
# 	manufacturer	model	displ	year	cyl	trans	drv	cty	hwy	fl	class	mileage_difference	average_mileage	is_automatic
# 1	audi	a4	1.8	1999	4	auto(l5)	f	18	29	p	compact	11	23.5	True
# 2	audi	a4	1.8	1999	4	manual(m5)	f	21	29	p	compact	8	25.0	False
# 3	audi	a4	2.0	2008	4	manual(m6)	f	20	31	p	compact	11	25.5	False
# 4	audi	a4	2.0	2008	4	auto(av)	f	21	30	p	compact	9	25.5	True
# 5	audi	a4	2.8	1999	6	auto(l5)	f	16	26	p	compact	10	21.0	True

# Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
mpg.sort_values(by='average_mileage', ascending=False).head(5)
# 	manufacturer	model	displ	year	cyl	trans	drv	cty	hwy	fl	class	mileage_difference	average_mileage	is_automatic
# 222	volkswagen	new beetle	1.9	1999	4	manual(m5)	f	35	44	d	subcompact	9	39.5	False
# 213	volkswagen	jetta	1.9	1999	4	manual(m5)	f	33	44	d	compact	11	38.5	False
# 223	volkswagen	new beetle	1.9	1999	4	auto(l4)	f	29	41	d	subcompact	12	35.0	True
# 197	toyota	corolla	1.8	2008	4	manual(m5)	f	28	37	r	compact	9	32.5	False
# 196	toyota	corolla	1.8	1999	4	manual(m5)	f	26	35	r	compact	9	30.5	False

# Do automatic or manual cars have better miles per gallon?
# Manual for the most part.  See above

# Use your get_db_url function to help you explore the data from the chipotle database.
url = get_connection('chipotle', username, host, password)

# What is the total price for each order?
orders_df['item_price'] = orders_df.item_price.str.replace('$', '').astype(float)
orders_df.groupby('order_id').sum('item_price')

# What are the most popular 3 items?
orders_df.groupby('item_name').quantity.sum().sort_values(ascending=False).head(3)
# item_name
# Chicken Bowl           761
# Chicken Burrito        591
# Chips and Guacamole    506

# Which item has produced the most revenue?
orders_df.groupby('item_name').item_price.sum().nlargest(1)
# item_name
# Chicken Bowl    7342.73

# Using the titles DataFrame, visualize the number of employees with each title.
titles_df['title'].value_counts()
# Engineer              115003
# Staff                 107391
# Senior Engineer        97750
# Senior Staff           92853
# Technique Leader       15159
# Assistant Engineer     15128
# Manager                   24

# Join the employees and titles DataFrames together.
all_employees_titles = employees.merge(titles_df, on='emp_no')

# Visualize how frequently employees change titles.
all_employees_titles.groupby('emp_no').title.count().value_counts()
# 1    159754
# 2    137256
# 3      3014

# For each title, find the hire date of the employee that was hired most recently with that title.
all_employees_titles.groupby('title').hire_date.max()
# title
# Assistant Engineer    1999-12-24
# Engineer              2000-01-28
# Manager               1992-02-05
# Senior Engineer       2000-01-01
# Senior Staff          2000-01-13
# Staff                 2000-01-12
# Technique Leader      1999-12-31

# Write the code necessary to create a cross tabulation of the number of titles by department. 
# (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas code to 
# perform the manipulations.)

