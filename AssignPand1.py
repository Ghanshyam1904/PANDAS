import pandas as pd
#Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.
df = pd.Series({'a' : [4, 8, 15, 16, 23,42]})
print(df)

# Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
# variable print it.
lst = [1,2,3,4,5,6,7,8,9,10]
df2 = pd.Series(lst)
print(type(df2))

# Q3. Create a Pandas DataFrame that contains the following data:

df3 = pd.DataFrame({
    'Name' :['Alice','Bob','Claire'],
    'Age' :[25,30,27],
    'Gender' : ['Female','Male','Female']
})
print(df3)

# Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.
#Ans :- DataFrame :- DataFrame is combination of Series. DataFrame is mutable we mainly used Dataframe in pandas to manipulate operations on data
#Series :- Series is 1-Dimensional it is created by a single row and it is immutable
#Exap:-

# Datafreame
data = {
    'a' : [1,2,3,4],
    'b' : [5,6,7,8],
}
df4 = pd.DataFrame(data)
print(df4)

data1 = {
    'a' : [1,2,3,4]
}
df5 = pd.Series(data1)
print(df5)

# columns:- In a series we extact a single col. But in DataFrame we can extract multiple col
# Axis :- there is only row axis is avialble in series. In DataFrame row wise and col wise axis available


# Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
# you give an example of when you might use one of these functions?

# Columns :- To extract all the columns from data frame
# head() :- To get first five record by default. we can retriv no of record using pass a parameter
# Tail() :- To get last five record by default . we can retriv no of record using pass a parameter
# Categorical() :- this function remove duplicate entries from rows and count duplicate entries
# dtypes :- To get which type of column data

# Q6. Which of the following is mutable in nature Series, DataFrame, Panel?
# ans :- DataFrame and Panel is mutable in nature

# Q7. Create a DataFrame using multiple Series. Explain with an example.
df6 = pd.Series([1,2,3,4,5])
df7 = pd.Series([6,7,8,9,10])

df8 = pd.DataFrame({'a':df6,'b':df7})
print(df8)
