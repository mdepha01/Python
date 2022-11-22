# This section covers the basics of pandas dataframes and series
# to use pandas we start by importing the pandas library
import pandas as pd

# converting a dictionary/list into a Dataframe we use pd.DataFrame(dictionary)

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
      'Salary':[100000, 80000, 50000, 60000]}

# converting Dictionary to dataframe and printing the results
# Keys are turned into coloums and values are turned into rows
_DataFrame = pd.DataFrame(x)
print(_DataFrame)

#selecting a dataframe coloum: using DataFrame[['colomn name']]
print('\n--------------Selected Column--------------\n')
IDColomn = _DataFrame[['ID']]
print(IDColomn)

# Selecting Multiple colomns in a data frame : DataFrame[['column_1', 'column_2',..., 'column_n']]
MultipleColomns = _DataFrame[['ID', 'Department']]
print(MultipleColomns)
# finding variable type using the type() function
print(type(IDColomn))

# when viewing a column as a series a single square bracket should be used
Seriez = _DataFrame['Department']
print(Seriez)
print(type(Seriez))

# accessing DataFrame data using loc() and iloc() functions
# using iLoc to access data int index [0,0]

iLoc = _DataFrame.iloc[0,0]
print('\n-----------------iLoc-------------------\n')
print(iLoc)

# using Loc using [0, Name] labels
_DataFrame2 = _DataFrame
_DataFrame2= _DataFrame2.set_index("Name") # making name index
Loc = _DataFrame2.loc['Jane', 'Department']
print(Loc)
print(type(Loc))
