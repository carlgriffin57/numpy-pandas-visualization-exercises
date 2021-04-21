import pandas as pd
import numpy as np
from pydataset import data


# Copy the code from the lesson to create a dataframe full of student grades.
np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})




# Create a column named passing_english that indicates whether each student has a passing grade in english.
df['passing_english'] = df.english > 70
#        name  math  english  reading  passing_english
# 0     Sally    62       85       80             True
# 1      Jane    88       79       67             True
# 2     Suzie    94       74       95             True
# 3     Billy    98       96       88             True
# 4       Ada    77       92       98             True
# 5      John    79       76       93             True
# 6    Thomas    82       64       81            False
# 7     Marie    93       63       90            False
# 8    Albert    92       62       87            False
# 9   Richard    69       80       94             True
# 10    Isaac    92       99       93             True
# 11     Alan    92       62       72            False

# Sort the english grades by the passing_english column. How are duplicates handled? Sorts by index
df.sort_values(by='passing_english')
#        name  math  english  reading  passing_english
# 6    Thomas    82       64       81            False
# 7     Marie    93       63       90            False
# 8    Albert    92       62       87            False
# 11     Alan    92       62       72            False
# 0     Sally    62       85       80             True
# 1      Jane    88       79       67             True
# 2     Suzie    94       74       95             True
# 3     Billy    98       96       88             True
# 4       Ada    77       92       98             True
# 5      John    79       76       93             True
# 9   Richard    69       80       94             True
# 10    Isaac    92       99       93             True

# Sort the english grades first by passing_english and then by student name. All the students that are 
# failing english should be first, and within the students that are failing english they should be ordered 
# alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to 
# the .sort_values method)
df.sort_values(by=['passing_english', 'name'])
#        name  math  english  reading  passing_english
# 11     Alan    92       62       72            False
# 8    Albert    92       62       87            False
# 7     Marie    93       63       90            False
# 6    Thomas    82       64       81            False
# 4       Ada    77       92       98             True
# 3     Billy    98       96       88             True
# 10    Isaac    92       99       93             True
# 1      Jane    88       79       67             True
# 5      John    79       76       93             True
# 9   Richard    69       80       94             True
# 0     Sally    62       85       80             True
# 2     Suzie    94       74       95             True


# Sort the english grades first by passing_english, and then by the actual english grade, similar to how we 
# did in the last step.
df.sort_values(by=['passing_english', 'english'])
#        name  math  english  reading  passing_english
# 8    Albert    92       62       87            False
# 11     Alan    92       62       72            False
# 7     Marie    93       63       90            False
# 6    Thomas    82       64       81            False
# 2     Suzie    94       74       95             True
# 5      John    79       76       93             True
# 1      Jane    88       79       67             True
# 9   Richard    69       80       94             True
# 0     Sally    62       85       80             True
# 4       Ada    77       92       98             True
# 3     Billy    98       96       88             True
# 10    Isaac    92       99       93             True

# Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the
#  average of the math, english, and reading grades.
df['overall_grade'] = (df['math'] + df['english'] + df['reading']) / 3
#        name  math  english  reading  passing_english  overall_grade
# 0     Sally    62       85       80             True      75.666667
# 1      Jane    88       79       67             True      78.000000
# 2     Suzie    94       74       95             True      87.666667
# 3     Billy    98       96       88             True      94.000000
# 4       Ada    77       92       98             True      89.000000
# 5      John    79       76       93             True      82.666667
# 6    Thomas    82       64       81            False      75.666667
# 7     Marie    93       63       90            False      82.000000
# 8    Albert    92       62       87            False      80.333333
# 9   Richard    69       80       94             True      81.000000
# 10    Isaac    92       99       93             True      94.666667
# 11     Alan    92       62       72            False      75.333333
​
# Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
mpg = data('mpg')

# How many rows and columns are there?
# [234 rows x 11 columns]

# What are the data types of each column?
mpg.dtypes
# manufacturer     object
# model            object
# displ           float64
# year              int64
# cyl               int64
# trans            object
# drv              object
# cty               int64
# hwy               int64
# fl               object
# class            object
# dtype: object

# Summarize the dataframe with .info and .describe
mpg.info()
<class 'pandas.core.frame.DataFrame'>
# Int64Index: 234 entries, 1 to 234
# Data columns (total 11 columns):
#  #   Column        Non-Null Count  Dtype  
# ---  ------        --------------  -----  
#  0   manufacturer  234 non-null    object 
#  1   model         234 non-null    object 
#  2   displ         234 non-null    float64
#  3   year          234 non-null    int64  
#  4   cyl           234 non-null    int64  
#  5   trans         234 non-null    object 
#  6   drv           234 non-null    object 
#  7   cty           234 non-null    int64  
#  8   hwy           234 non-null    int64  
#  9   fl            234 non-null    object 
#  10  class         234 non-null    object 
# dtypes: float64(1), int64(4), object(6)
# memory usage: 21.9+ KB

mpg.describe()
# 	displ	year	cyl	cty	hwy
# count	234.000000	234.000000	234.000000	234.000000	234.000000
# mean	3.471795	2003.500000	5.888889	16.858974	23.440171
# std	1.291959	4.509646	1.611534	4.255946	5.954643
# min	1.600000	1999.000000	4.000000	9.000000	12.000000
# 25%	2.400000	1999.000000	4.000000	14.000000	18.000000
# 50%	3.300000	2003.500000	6.000000	17.000000	24.000000
# 75%	4.600000	2008.000000	8.000000	19.000000	27.000000
# max	7.000000	2008.000000	8.000000	35.000000	44.000000

# Rename the cty column to city.
mpg = mpg.rename(columns={'cty': 'city'})

# Rename the hwy column to highway.
mpg = mpg.rename(columns={'hwy': 'highway'})

# Do any cars have better city mileage than highway mileage?
mpg[(mpg.city > mpg.highway)]
# None

# Create a column named mileage_difference this column should contain the difference between highway and 
# city mileage for each car.
mpg['mileage_difference'] = abs(mpg.highway - mpg.city)
# 	manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference
# 1	audi	a4	1.8	1999	4	auto(l5)	f	18	29	p	compact	11
# 2	audi	a4	1.8	1999	4	manual(m5)	f	21	29	p	compact	8
# 3	audi	a4	2.0	2008	4	manual(m6)	f	20	31	p	compact	11
# 4	audi	a4	2.0	2008	4	auto(av)	f	21	30	p	compact	9
# 5	audi	a4	2.8	1999	6	auto(l5)	f	16	26	p	compact	1

# Which car (or cars) has the highest mileage difference?
mpg.sort_values(by='mileage_difference', ascending=False)
# 	manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference
# 107	honda	civic	1.8	2008	4	auto(l5)	f	24	36	c	subcompact	12
# 223	volkswagen	new beetle	1.9	1999	4	auto(l4)	f	29	41	d	subcompact	12

# Which compact class car has the lowest highway mileage? The best?
mpg.loc[mpg['class'] == 'compact'].sort_values(by=['highway']).head(1)
# 	manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference
# 220	volkswagen	jetta	2.8	1999	6	auto(l4)	f	16	23	r	compact	7

mpg.loc[mpg['class'] == 'compact'].sort_values(by=['highway'], ascending=[False]).head(1)
# 	manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference
# 213	volkswagen	jetta	1.9	1999	4	manual(m5)	f	33	44	d	compact	11

# Create a column named average_mileage that is the mean of the city and highway mileage.
mpg['average_mileage'] = (mpg.highway + mpg.city) / 2

# Which dodge car has the best average mileage? The worst?
mpg.loc[mpg['manufacturer'] == 'dodge'].sort_values(by=['average_mileage'], ascending=False).head(1)
# 	manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference	average_mileage
# 38	dodge	caravan 2wd	2.4	1999	4	auto(l3)	f	18	24	r	minivan	6	21.0
mpg.loc[mpg['manufacturer'] == 'dodge'].sort_values(by=['average_mileage']).head(1)
# manufacturer	model	displ	year	cyl	trans	drv	city	highway	fl	class	mileage_difference	average_mileage
# 70	dodge	ram 1500 pickup 4wd	4.7	2008	8	manual(m6)	4	9	12	e	pickup	3	10.5

# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

# How many rows and columns are there?
mammals.shape
# (107, 4)

# What are the data types?
# mammals.dtypes
# weight      float64
# speed       float64
# hoppers        bool
# specials       bool
# dtype: object

# Summarize the dataframe with .info and .describe
mammals.info()
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 107 entries, 1 to 107
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype  
# ---  ------    --------------  -----  
#  0   weight    107 non-null    float64
#  1   speed     107 non-null    float64
#  2   hoppers   107 non-null    bool   
#  3   specials  107 non-null    bool   
# dtypes: bool(2), float64(2)
# memory usage: 2.7 KB

mammals.describe()
# 	weight	speed
# count	107.000000	107.000000
# mean	278.688178	46.208411
# std	839.608269	26.716778
# min	0.016000	1.600000
# 25%	1.700000	22.500000
# 50%	34.000000	48.000000
# 75%	142.500000	65.000000
# max	6000.000000	110.00000

# What is the the weight of the fastest animal?
mammals.sort_values(by='speed', ascending= False).head(1)
# 	weight	speed	hoppers	specials
# 53	55.0	110.0	False	False

# What is the overall percentage of specials?
round(((mammals['specials'].values.sum() / len(mammals.index)) * 100), 2)
# 9.35

# How many animals are hoppers that are above the median speed? 
mammals[mammals.hoppers & (mammals.speed > median_speed)]
# 	weight	speed	hoppers	specials
# 96	4.6	64.0	True	False
# 97	4.4	72.0	True	False
# 98	4.0	72.0	True	False
# 99	3.5	56.0	True	False
# 100	2.0	64.0	True	False
# 101	1.9	56.0	True	False
# 102	1.5	50.0	True	False

# What percentage is this?
round(((len(mammals[mammals.hoppers & (mammals.speed > median_speed)].index) / len(mammals.index)) * 100), 2)
# 6.54
