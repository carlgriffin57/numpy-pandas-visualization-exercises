import pandas as pd 
# Name the variable that holds the series fruits.
fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# Determine the number of elements in fruits.
fruits.count()
# 17

# Output only the index from fruits.
fruits.index
# RangeIndex(start=0, stop=17, step=1)

# Output only the values from fruits.
fruits.values
# array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
    #    'honeycrisp apple', 'tomato', 'watermelon', 'honeydew', 'kiwi',
    #    'kiwi', 'kiwi', 'mango', 'blueberry', 'blackberry', 'gooseberry',
    #    'papaya'], dtype=object)

# Confirm the data type of the values in fruits.
fruits.dtype
# dtype('O')

# Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
fruits.head(5)
# 0          kiwi
# 1         mango
# 2    strawberry
# 3     pineapple
# 4    gala apple
# dtype: object

fruits.tail(3)
# 14    blackberry
# 15    gooseberry
# 16        papaya
# dtype: object

fruits.sample(2)
# 1     mango
# 6    tomato
# dtype: object

# Run the .describe() on fruits to see what information it returns when called on a Series with string values.
fruits.astype('string').describe
# 0                 kiwi
# 1                mango
# 2           strawberry
# 3            pineapple
# 4           gala apple
# 5     honeycrisp apple
# 6               tomato
# 7           watermelon
# 8             honeydew
# 9                 kiwi
# 10                kiwi
# 11                kiwi
# 12               mango
# 13           blueberry
# 14          blackberry
# 15          gooseberry
# 16              papaya
# dtype: string

# Run the code necessary to produce only the unique string values from fruits.
fruits.unique()
# array(['kiwi', 'mango', 'strawberry', 'pineapple', 'gala apple',
#        'honeycrisp apple', 'tomato', 'watermelon', 'honeydew',
#        'blueberry', 'blackberry', 'gooseberry', 'papaya'], dtype=object)

# Determine how many times each unique string value occurs in fruits.
pd.Series(fruits).value_counts()
# kiwi                4
# mango               2
# blueberry           1
# gooseberry          1
# blackberry          1
# gala apple          1
# strawberry          1
# pineapple           1
# honeydew            1
# watermelon          1
# papaya              1
# tomato              1
# honeycrisp apple    1
# dtype: int64

# Determine the string value that occurs most frequently in fruits.
fruits.value_counts().nlargest(n=1)
# kiwi    4
# dtype: int64

# Determine the string value that occurs least frequently in fruits.
fruits.value_counts().nsmallest(n=1, keep='all')
# blueberry    1
# dtype: int64

# Exercises 2

# Capitalize all the string values in fruits.
fruits.str.capitalize()
# 0                 Kiwi
# 1                Mango
# 2           Strawberry
# 3            Pineapple
# 4           Gala apple
# 5     Honeycrisp apple
# 6               Tomato
# 7           Watermelon
# 8             Honeydew
# 9                 Kiwi
# 10                Kiwi
# 11                Kiwi
# 12               Mango
# 13           Blueberry
# 14          Blackberry
# 15          Gooseberry
# 16              Papaya
# dtype: object

# Count the letter "a" in all the string values (use string vectorization).
fruits.str.count('a').sum()
# 14

# Output the number of vowels in each and every string value.
fruits.str.count('[aeiou]')
# 0     2
# 1     2
# 2     2
# 3     4
# 4     4
# 5     5
# 6     3
# 7     4
# 8     3
# 9     2
# 10    2
# 11    2
# 12    2
# 13    3
# 14    2
# 15    4
# 16    3
# dtype: int64

# Write the code to get the longest string value from fruits.
max(fruits, key=len)
# 'honeycrisp apple'

# Write the code to get the string values with 5 or more letters in the name.
fruits[(fruits.str.len() >= 5)]
# 2           strawberry
# 3            pineapple
# 4           gala apple
# 5     honeycrisp apple
# 6               tomato
# 7           watermelon
# 8             honeydew
# 13           blueberry
# 14          blackberry
# 15          gooseberry
# 16              papaya
# dtype: object

# Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
fruits[fruits.apply(lamda string: True if string.count('o') >= 2 else False)]
# 6         tomato
# 15    gooseberry
# dtype: object

# Write the code to get only the string values containing the substring "berry".
fruits[fruits.str.contains('berry')]
# 2     strawberry
# 13     blueberry
# 14    blackberry
# 15    gooseberry
# dtype: object

# Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]
# 3           pineapple
# 4          gala apple
# 5    honeycrisp apple
# dtype: object

# Which string value contains the most vowels?
fruits[max(fruits.str.count('[aeiou]'))]
# 'honeycrisp apple'

# Exercises 3

letters = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'

# Which letter occurs the most frequently in the letters Series?
pd.Series(list(letters)).value_counts().idxmax()
# 'y'

# Which letter occurs the Least frequently?
pd.Series(list(letters)).value_counts().idxmin()
# 'l'

# How many vowels are in the Series?
letters = pd.Series(['hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'])
letters.str.count('[aeiou]')
# 0    34
# dtype: int64

# How many consonants are in the Series?
letters.str.len() - letters.str.count('[aeiou]')
# 0    166
# dtype: int64

# Create a Series that has all of the same letters but uppercased.
letters.str.upper()

# Create a bar plot of the frequencies of the 6 most commonly occuring letters.
pd.Series(list(letters)).value_counts().head(6).plot.bar(rot=0)

# What is the data type of the numbers Series?

# How many elements are in the number Series?

# Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.

# Run the code to discover the maximum value from the Series.

# Run the code to discover the minimum value from the Series.

# What is the range of the values in the Series?

# Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.

# Plot the binned data in a meaningful way. Be sure to include a title and axis labels.


